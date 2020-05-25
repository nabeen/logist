from pybacklogpy.BacklogConfigure import BacklogComConfigure
from pybacklogpy.Issue import Issue
from logist.libs.time_manager import in_week
import json


def get_data(space_key, api_key, assignee_id):
    """ get issues list from Backlog due in week """
    config = BacklogComConfigure(space_key=space_key, api_key=api_key)
    issue_api = Issue(config)

    # TODO: status set to config file
    response = issue_api.get_issue_list(
        assignee_id=[assignee_id], status_id=[1], sort='dueDate', order='asc', due_date_until=in_week)

    if not response.ok:
        raise ValueError('failed get issues')

    data = json.loads(response.text)
    return data
