# todo-cli

A minimal command-line to-do manager written in Python. No dependencies, tasks are saved to `~/.todo-cli.json`.

## Usage

```bash
python todo.py add "Buy groceries"
python todo.py list
python todo.py done 1
python todo.py remove 1
```

Example output:

```
[ ] 1. Buy groceries
[x] 2. Finish report
```

## Run the tests

```bash
python -m unittest
```

## Ideas for improvement
- Due dates and priorities
- Filtering (`list --pending`)
- Export to CSV

## License
MIT
