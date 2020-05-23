from pybacklogpy.BacklogConfigure import BacklogComConfigure
from pybacklogpy.Issue import Issue
import json
import configparser
import click
import setting


def main():
    try:
        host = setting.read_config('backlog', 'Host')
        api_key = setting.read_config('backlog', 'ApiKey')
        assignee_id = setting.read_config('backlog', 'AssigneeId')
    except Exception as e:
        click.secho('set config with command configure before export', fg='red')
        return

    space_key = host.replace(".backlog.com", "")
    data = get_data(space_key=space_key, api_key=api_key,
                    assignee_id=assignee_id)
    for v in data:
        print(v['summary'], 'https://'+host+'/view/'+v['issueKey'])
    click.secho('SUCCESS!!', fg='green')


def get_data(space_key, api_key, assignee_id):
    config = BacklogComConfigure(space_key=space_key, api_key=api_key)
    issue_api = Issue(config)
    # TODO: more filter
    response = issue_api.get_issue_list(assignee_id=[assignee_id])

    if not response.ok:
        raise ValueError('failed get issues')

    data = json.loads(response.text)
    return data
