import json
from datetime import datetime
from pathlib import Path
from typing import List, TypedDict

VALID_STATUSES = ("todo", "in-progress", "done")
DESC_WIDTH = 24


class Task(TypedDict):
    """
    Typed dictionary representing a task.
    """

    id: int
    description: str
    status: str
    createdAt: str
    updatedAt: str


def add_task(task_description: str, task_list: List[Task]) -> List[Task]:
    """
    Add a new task to the in-memory list.

    Parameters
    ----------
    task_description: str
        Name of the task to add.
    task_list: List[Task]
        The list of tasks loaded from a JSON file into memory.

    Returns
    -------
    List[Task]
        Updated task list.

    Raises
    ------
    RuntimeError
        If the task could not be added.
    """
    new_task: Task = {
        "id": task_list[len(task_list) - 1]["id"] + 1,
        "description": task_description,
        "status": "todo",
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    try:
        task_list.append(new_task)
    except Exception as e:
        raise RuntimeError(f"Failed to add task '{task_description}'") from e

    return task_list


def update_task(
    task_id: int, task_description: str, task_list: List[Task]
) -> List[Task]:
    """
    Update a task with the given ID.

    Parameters
    ----------
    task_id: int
        Id of the task to update.
    task_description: str
        New name for the task
    task_list: List[Task]
        The list of tasks loaded from a JSON file into memory.

    Returns
    -------
    List[Task]
        Updated task list.

    Raises
    ------
    IndexError
        If the index is out of range.
    """
    idx = task_id - 1
    if 0 <= idx < len(task_list):
        task_list[idx]["description"] = task_description
        task_list[idx]["updatedAt"] = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        return task_list
    raise IndexError(f"There is no task with ID {task_id}")


def update_status(
    task_id: int, status: str, task_list: List[Task]
) -> List[Task]:
    """
    Update the status of a task in the in-memory task list.

    Parameters
    ----------
    ID : int
        ID of the task to update.
    status : Status
        New task status ("todo", "in-progress", or "done").
    task_list : List[Task]
        The list of tasks in memory.

    Returns
    -------
    List[Task]
        Updated task list.

    Raises
    ------
    IndexError
        If the task ID is out of range.
    ValueError
        If the given status is not valid.
    """
    idx = task_id - 1
    if not 0 <= idx < len(task_list):
        raise IndexError(f"There is no task with ID {task_id}")
    if status not in VALID_STATUSES:
        raise ValueError(
            f"Invalid status '{status}'. Must be one of {VALID_STATUSES}"
        )
    task_list[idx]["status"] = status
    task_list[idx]["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return task_list



def remove_task(task_id: int, task_list: List[Task]) -> List[Task]:
    """
    Delete a task with the given id from the in-memory task list.

    Parameters
    ----------
    task_list : List[Task]
        The list of tasks to be written into the JSON file.
    task_id: int
        ID of the task to delete.

    Returns
    -------
    List[Task]
        Updated task list.

    Raises
    ------
    IndexError
        If the index is out of range.
    """
    idx = task_id - 1
    if 0 <= idx < len(task_list):
        del task_list[idx]
        return task_list
    raise IndexError(f"There is no task with ID {task_id}")


def load_tasks(path: str) -> List[Task]:
    """
    Load tasks from a JSON file. If the file does not exist, it will
    be created with an empty list.

    Parameters
    ----------
    path : str
        Path to the JSON file containing tasks.

    Returns
    -------
    list
        A list of tasks loaded from the file. If the file does not
        exist, an empty list is created and returned.

    Raises
    ------
    json.JSONDecodeError
        If the file exists but does not contain valid JSON.
    """
    tasks_file = Path(path)

    if not tasks_file.exists():
        tasks_file.write_text("[]", encoding="UTF-8")
        return []

    with open(tasks_file, "r", encoding="UTF-8") as file:
        return json.load(file)


def write_tasks_to_json(task_list: List[Task], path: str) -> None:
    """
    Write the in-memory task list to a JSON file.

    Parameters
    ----------
    task_list : List[Task]
        The list of tasks to be written into the JSON file.
    path : str
        Path to the JSON file where tasks will be saved.

    Returns
    -------
    None

    Raises
    ------
    RuntimeError
        If writing to the JSON file fails.
    """
    task_file = Path(path)
    try:
        with open(task_file, "w", encoding="UTF-8") as file:
            json.dump(task_list, file, indent=2)
    except Exception as e:
        raise RuntimeError(f"Failed to write tasks to {path}") from e

