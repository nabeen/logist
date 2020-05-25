import configparser
import click
import logist.setting as setting
import logist.libs.backlog_issues as backlog_issues


def main():
    # read config before process
    try:
        host = setting.read_config('backlog', 'Host')
        api_key = setting.read_config('backlog', 'ApiKey')
        assignee_id = setting.read_config('backlog', 'AssigneeId')
    except Exception as e:
        click.secho('set config with command configure before export', fg='red')
        return

    # TODO: error handler
    data = backlog_issues.get_data(space_key=host.replace(".backlog.com", ""), api_key=api_key,
                                   assignee_id=assignee_id)
    if len(data) == 0:
        click.secho('You have no issues:)', fg='magenta')
        return

    for v in data:
        click.echo(v['summary']+'\t=> https://'+host+'/view/'+v['issueKey'])

    click.secho('SUCCESS!!', fg='green')
