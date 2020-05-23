from PyInquirer import style_from_dict, Token, prompt, Separator
import configparser
import setting
import click
import viewer
from todoist.api import TodoistAPI


def main():
    try:
        host = setting.read_config('backlog', 'Host')
        backlog_api_key = setting.read_config('backlog', 'ApiKey')
        assignee_id = setting.read_config('backlog', 'AssigneeId')

        todoist_api_key = setting.read_config('todoist', 'ApiKey')
    except Exception as e:
        click.secho('set config with command configure before export', fg='red')
        return

    space_key = host.replace(".backlog.com", "")
    data = viewer.get_data(space_key=space_key, api_key=backlog_api_key,
                           assignee_id=assignee_id)
    questions = [
        {
            'type': 'checkbox',
            'qmark': '✅',
            'message': 'Select issues',
            'name': 'issues',
            'choices': [{'name': '['+v['summary']+']'+'(https://'+host+'/view/'+v['issueKey']+')'} for v in data],
            'validate': lambda answer: 'You must choose at least one issues.'
            if len(answer) == 0 else True
        }
    ]

    answers = prompt(questions)
    if not answers:
        return

    if len(answers['issues']) == 0:
        click.secho('You must choose at least one issues.', fg='red')
        return

    api = TodoistAPI(todoist_api_key)
    api.sync()
    for v in answers['issues']:
        api.items.add(v, due={"string": "today"})

    api.commit()
    click.secho('SUCCESS!!', fg='green')
