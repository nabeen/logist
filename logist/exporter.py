import configparser
from todoist.api import TodoistAPI


def main(issues):
    print('todoist')
    config_file = configparser.ConfigParser()
    config_file.read('secrets')

    item_list = ['test1', 'test2']
    api = TodoistAPI(config_file['todoist']['ApiKey'])
    api.sync()
    for item in item_list:
        api.items.add(item, due={"string": "today"})

    api.commit()
