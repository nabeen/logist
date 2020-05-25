from PyInquirer import style_from_dict, Token, prompt
import configparser
import click
import os

config_path = os.environ['HOME']+'/.logist'

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

    # input for backlog
    click.secho('set for backlog', fg='magenta')
    a_backlog = prompt(q_backlog, style=style)
    if not a_backlog:
        return

    # input for todoist
    click.secho('set for todoist', fg='magenta')
    a_todoist = prompt(q_todoist, style=style)
    if not a_todoist:
        return

    # configure and write ConfigParser object
    config = set_config(config, 'backlog', a_backlog)
    config = set_config(config, 'todoist', a_todoist)
    if write_config(config):
        click.secho('SUCCESS!!', fg='green')


def set_config(config, section, items):
    config.add_section(section)
    for k, v in items.items():
        config.set(section, k, v)

    return config


def read_config(section, key):
    if not os.path.exists(config_path):
        raise FileNotFoundError('no such fie:', config_path)

    config = configparser.ConfigParser()
    config.read(config_path)

    if section not in config:
        raise KeyError('no such section:', section)

    arr = config[section]
    val = arr.get(key)

    if not val:
        raise KeyError('no such key or value:', key)

    return val


def write_config(config):
    with open(config_path, 'w') as file:
        config.write(file)

    return True
