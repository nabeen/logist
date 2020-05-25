import configparser
import click
import logist.setting as setting
import logist.libs.backlog_issues as backlog_issues
import logist.libs.todoist_tasks as todoist_tasks
from PyInquirer import style_from_dict, Token, prompt, Separator


def main():
    # read config before process
    try:
        backlog_host = setting.read_config('backlog', 'Host')
        backlog_api_key = setting.read_config('backlog', 'ApiKey')
        backlog_assignee_id = setting.read_config('backlog', 'AssigneeId')

        todoist_api_key = setting.read_config('todoist', 'ApiKey')
    except Exception as e:
        click.echo(e)
        click.secho('set config with command configure before export', fg='red')
        return

    # TODO: error handler
    data = backlog_issues.get_data(space_key=backlog_host.replace(
        ".backlog.com", ""), api_key=backlog_api_key, assignee_id=backlog_assignee_id)
    if len(data) == 0:
        click.secho('You have no issues:)', fg='magenta')
        return

    answers = prompt(set_questions(data=data, host=backlog_host))
    if not answers:
        return

    if len(answers['issues']) == 0:
        click.secho('You must choose at least one issues.', fg='red')
        return

    # TODO: error handler
    todoist_tasks.add_data(api_key=todoist_api_key, issues=answers['issues'])
    click.secho('SUCCESS!!', fg='green')


def set_questions(data, host):
    choices = []
    d = ''
    for v in data:
        if d is not v['dueDate']:
            # add separator another day
            choices.append(Separator(v['dueDate']))
        choices.append({'name': '['+v['summary']+']' +
                        '(https://'+host+'/view/'+v['issueKey']+')'})

    questions = [
        {
            'type': 'checkbox',
            'qmark': '✅',
            'message': 'Select issues',
            'name': 'issues',
            'choices': choices,
            'validate': lambda answer: 'You must choose at least one issues.'
            if len(answer) == 0 else True
        }
    ]

    return questions
