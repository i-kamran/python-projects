import argparse

from task_tracker import utils

PATH = "./tasks.json"


def main():
    pass


def add(desc: str) -> None:
    """
    Add new task to the list.

    Parameters
    ----------
    desc: str
        Description of the task

    Returns
    -------
    None
    """

    tasks = utils.add_task(desc, utils.load_tasks(PATH))
    utils.write_tasks_to_json(tasks, PATH)
