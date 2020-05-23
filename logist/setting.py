from PyInquirer import style_from_dict, Token, prompt
import configparser
import click

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})

# TODO: add Validator
q_backlog = [
    {
        'type': 'input',
        'name': 'Host',
        'message': 'What\'s your Backlog Host?',
    },
    {
        'type': 'input',
        'name': 'ApiKey',
        'message': 'What\'s your Backlog ApiKey?',
    },
    {
        'type': 'input',
        'name': 'AssigneeId',
        'message': 'What\'s your Backlog AssigneeId?',
    },
]

# TODO: add Validator
q_todoist = [
    {
        'type': 'input',
        'name': 'ApiKey',
        'message': 'What\'s your Todoist ApiKey?',
    },
]


def main():
    config = configparser.ConfigParser()
    config.optionxform = str

    config = set_config(config, 'backlog', prompt(q_backlog, style=style))
    config = set_config(config, 'todoist', prompt(q_todoist, style=style))
    if write_config(config):
        click.secho('SUCCESS!!', fg='green')


def set_config(config, section, items):
    config.add_section(section)
    for k, v in items.items():
        config.set(section, k, v)
    return config


def read_config():
    pass


def write_config(config):
    with open('secrets', 'w') as file:
        config.write(file)

    return True
