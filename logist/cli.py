"""Console script for logist."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for logist."""
    click.echo("Replace this message by putting your code into "
               "logist.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
