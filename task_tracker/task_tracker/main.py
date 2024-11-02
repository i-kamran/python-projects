import argparse

from task_tracker import utils

PATH = "./tasks.json"


def main():
    """
    CLI Task Tracker
    """
    parser = argparse.ArgumentParser(
        prog="task-tracker", description="Simple CLI Task Tracker"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("desc", type=str, help="Description of the task")

    # update command
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("task_id", type=int, help="ID of the task")
    update_parser.add_argument("desc", type=str, help="New description")

    # delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="ID of the task")

    # mark-status command
    status_parser = subparsers.add_parser(
        "mark-in-progress", help="Update status of a task to in-progress"
    )
    status_parser.add_argument("task_id", type=int, help="ID of the task")

    status_parser = subparsers.add_parser(
        "mark-done", help="Update status of a task to done"
    )
    status_parser.add_argument("task_id", type=int, help="ID of the task")

    # list command
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "--status",
        type=str,
        default="all",
        help="Filter tasks by status (default: all)",
    )

    args = parser.parse_args()

    # Command dispatch
    if args.command == "add":
        add(args.desc)
    elif args.command == "update":
        update(args.task_id, args.desc)
    elif args.command == "delete":
        delete(args.task_id)
    elif args.command == "mark-in-progress":
        mark_status(args.task_id, "in-progress")
    elif args.command == "mark-done":
        mark_status(args.task_id, "done")
    elif args.command == "list":
        tracker_list(args.status)


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


def update(task_id: int, desc: str) -> None:
    """
    Update description of the task with the given ID.

    Parameters
    ----------
    task_id: int
        ID of the task
    desc: str
        Description of the task

    Returns
    -------
    None
    """

    tasks = utils.update_task(task_id, desc, utils.load_tasks(PATH))
    utils.write_tasks_to_json(tasks, PATH)


def delete(task_id: int) -> None:
    """
    Delete a task with the given ID.

    Parameters
    ----------
    task_id: int
        ID of the task to delete

    Returns
    -------
    None
    """
    tasks = utils.remove_task(task_id, utils.load_tasks(PATH))
    utils.write_tasks_to_json(tasks, PATH)


def mark_status(task_id: int, status: str) -> None:
    """
    Update status of the task with the given ID.

    Parameters
    ----------
    task_id: int
        ID of the task
    desc: str
        Status of the task

    Returns
    -------
    None
    """

    tasks = utils.update_status(task_id, status, utils.load_tasks(PATH))
    utils.write_tasks_to_json(tasks, PATH)


def tracker_list(status: str = "all") -> None:
    """
    List tasks based on status.

    Parameters
    ----------
    status : str, optional
        The status to filter tasks by. If not provided, all tasks are listed.

    Returns
    -------
    None
    """

    tasks = utils.load_tasks(PATH)
    utils.list_tasks(tasks, status)


if __name__ == "__main__":
    main()
