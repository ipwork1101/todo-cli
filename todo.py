#!/usr/bin/env python3
"""A simple command-line to-do manager that stores tasks in a JSON file."""
import argparse
import json
from pathlib import Path

DB_PATH = Path.home() / ".todo-cli.json"


def load_tasks(path=DB_PATH):
    if path.exists():
        return json.loads(path.read_text())
    return []


def save_tasks(tasks, path=DB_PATH):
    path.write_text(json.dumps(tasks, indent=2))


def add_task(tasks, text):
    task = {"id": max((t["id"] for t in tasks), default=0) + 1, "text": text, "done": False}
    tasks.append(task)
    return task


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return True
    return False


def remove_task(tasks, task_id):
    before = len(tasks)
    tasks[:] = [t for t in tasks if t["id"] != task_id]
    return len(tasks) < before


def format_task(task):
    mark = "x" if task["done"] else " "
    return f"[{mark}] {task['id']}. {task['text']}"


def build_parser():
    parser = argparse.ArgumentParser(description="Simple to-do manager")
    sub = parser.add_subparsers(dest="command", required=True)
    add = sub.add_parser("add", help="add a task")
    add.add_argument("text")
    sub.add_parser("list", help="list all tasks")
    done = sub.add_parser("done", help="mark a task as done")
    done.add_argument("id", type=int)
    rm = sub.add_parser("remove", help="remove a task")
    rm.add_argument("id", type=int)
    return parser


def main():
    args = build_parser().parse_args()
    tasks = load_tasks()

    if args.command == "add":
        task = add_task(tasks, args.text)
        print(f"Added: {format_task(task)}")
    elif args.command == "list":
        if not tasks:
            print("No tasks yet.")
        for task in tasks:
            print(format_task(task))
    elif args.command == "done":
        print("Done!" if complete_task(tasks, args.id) else f"No task with id {args.id}")
    elif args.command == "remove":
        print("Removed." if remove_task(tasks, args.id) else f"No task with id {args.id}")

    save_tasks(tasks)


if __name__ == "__main__":
    main()
