from todoist.api import TodoistAPI


def add_data(api_key, issues):
    """ add tasks to Todoist INBOX due today """
    api = TodoistAPI(api_key)
    api.sync()
    for v in issues:
        api.items.add(v, due={"string": "today"})

    api.commit()
