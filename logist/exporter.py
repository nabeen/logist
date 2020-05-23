import configparser
import setting
import click
from todoist.api import TodoistAPI


def main(issues):
    try:
        api_key = setting.read_config('todoist', 'ApiKey')
    except Exception as e:
        click.secho('set config with command configure before export', fg='red')
        return

    item_list = ['test1', 'test2']
    api = TodoistAPI(api_key)
    api.sync()
    for item in item_list:
        api.items.add(item, due={"string": "today"})

    api.commit()
    click.secho('SUCCESS!!', fg='green')
