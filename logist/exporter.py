import configparser
import todoist


def main(issues):
    print('todoist')
    config_file = configparser.ConfigParser()
    config_file.read('secrets')

    item_list = ['test1', 'test2']
    api = todoist.TodoistAPI(config_file['todoist']['ApiKey'])
    api.sync()
    for item in item_list:
        api.add_item(item)

    api.commit()
