"""Console script for logist."""
import sys
import click
import setting
import viewer
import exporter


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
    cmd()


if __name__ == "__main__":
    main()  # pragma: no cover
