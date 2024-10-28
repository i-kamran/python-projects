import json
from pathlib import Path
from typing import Dict, List, Union


def load_tasks(path: str) -> List[Dict[str, Union[str, bool]]]:
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

