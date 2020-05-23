"""Console script for logist."""
import sys
import click
import setting
import backlog
import todoist


@click.group()
def cmd():
    pass


@cmd.command(help='show issues from Backlog')
def show():
    click.echo('Start show...')
    backlog.main()


@cmd.command(help='export issues to Todoist')
@click.option('-id', '--issues-id', 'id', help='Input issues-id separated with comma', required=True)
def export(id):
    click.echo('Start export...')
    todoist.main()


@cmd.command(help='configure your setting')
def configure():
    click.echo('Start configure...')
    setting.main()


def main():
    cmd()


if __name__ == "__main__":
    main()  # pragma: no cover
