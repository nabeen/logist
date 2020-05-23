from pybacklogpy.BacklogConfigure import BacklogComConfigure
from pybacklogpy.Issue import Issue
import json
import configparser


def main():
    print('backlog')
    config_file = configparser.ConfigParser()
    config_file.read('secrets')

    issue_api = Issue()
    # TODO: more filter
    response = issue_api.get_issue_list(
        assignee_id=[config_file['backlog']['AssigneeId']])

    if not response.ok:
        raise ValueError('failed get issues')

    data = json.loads(response.text)
    for v in data:
        print(v['summary'], 'https://'+config_file['backlog']
              ['Host']+'/view/'+v['issueKey'])
