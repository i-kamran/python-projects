# Task Tracker

A lightweight and efficient task tracker for managing your daily to-dos and projects.  
Designed to be simple, fast, and easy to use.

---

## Features

- Add, edit, and delete tasks
- Mark tasks as complete or pending
- Filter and search tasks
- Organize tasks by due date, priority, or category
- Data persistence (saved locally)

---

## Installation

You can install Task Tracker directly from 'GitHub' using **pip**:

```bash
pip install "git+https://github.com/i-kamran/python-projects.git@main#egg=task-tracker&subdirectory=task_tracker"
```

## Usage

After installation, you can run CLI with:

```bash
task --help
```

## Examples

```bash
# Add a new task
task add "Write documentation"

# List all tasks
task list

# Mark a task as complete
task done 1

# Remove a task
task remove 1
```

## Project Structure

```text
task_tracker/
├── pyproject.toml      # Project metadata and dependencies
├── README.md
├── LICENSE
└── task_tracker/
    ├── __init__.py
    ├── main.py        # CLI entry point
    └── utils.py       # helper functions

```

## Development

Clone repository and install in editable mode:

```bash
git clone https://github.com/i-kamran/python-projects.git
cd task_tracker
pip install -e .
```

Now you can test changes locally with the ==task== command

## License

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).
