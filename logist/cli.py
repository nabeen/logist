"""Console script for logist."""
import sys
import click
import logist.setting as setting
import logist.viewer as viewer
import logist.exporter as exporter
from pyfiglet import Figlet


@click.group()
def cmd():
    pass


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
    f = Figlet(font='slant')
    click.echo(f.renderText('logist'))

    cmd()


if __name__ == "__main__":
    sys.exit(main())
