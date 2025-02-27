"""Console script for logist."""
import sys
import click
import logist
import logist.setting as setting
import logist.viewer as viewer
import logist.exporter as exporter
from pyfiglet import Figlet


@click.group(invoke_without_command=True)
@click.option('-V', '--version', 'version', is_flag=True, help='Show version.')
@click.pass_context
def cmd(ctx, version):
    # nothing subcommand
    if ctx.invoked_subcommand is None:
        f = Figlet(font='slant')
        click.echo(f.renderText('logist'))

    # for option
    if ctx.invoked_subcommand is None and version:
        click.echo('v'+logist.__version__)


@cmd.command(help='show issues from Backlog')
def show():
    click.echo('Start show...')
    viewer.main()


@cmd.command(help='export issues to Todoist')
def export():
    click.echo('Start export...')
    exporter.main()


@cmd.command(help='configure your setting')
def configure():
    click.echo('Start configure...')
    setting.main()


def main():
    cmd()


if __name__ == "__main__":
    sys.exit(main())
