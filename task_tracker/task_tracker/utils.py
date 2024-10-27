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
