#!/usr/local/bin/python3

import argparse
import json

from dataclasses import dataclass

DEFAULT_TODO_FILE = 'todo.json'

@dataclass
class TodoItem:
    text: str
    when: str = ""
    complete: bool = False

    def to_json(self):
        return {
            'text': self.text,
            'when': self.when,
            'complete': self.complete
        }

class Todo(object):
    def __init__(self, source=DEFAULT_TODO_FILE):
        self.todo_filepath = source
        self.todo = self.get(self.todo_filepath)

    def save(self, dest=DEFAULT_TODO_FILE):
        dest = dest or self.todo_filepath
        with open(dest, 'w') as f:
            json.dump(self.todo, f)

    def get(self, source=DEFAULT_TODO_FILE):
        try:
            with open(source, 'r') as f:
                ret = json.load(f)
                if not isinstance(ret, dict):
                    raise ValueError('todo currently only supports objects. are you using the right file?')
        except Exception:
            ret = {}

        if not 'today' in ret:
            ret['today'] = []

        return ret

    def add(self, item):
        self.todo['today'].append(item)

    def delete(self, stuff):
        if isinstance(stuff, int):
            self.delete_by_index(stuff)
        elif isinstance(stuff, str):
            self.delete_by_text(stuff)
        else:
            raise ValueError('delete does not support deleting by {}'.format(type(stuff)))

    def delete_by_index(self, i):
        if i < 0 or i >= len(self.todo['today']):
            raise ValueError

        del self.todo['today'][i]

    def delete_by_text(self, text):
        i = self.todo['today'].index(text)
        self.delete_by_index(i)

    def mark_complete(self, item):
        i = self.todo['today'].index(item)
        if i != -1:
            self.todo['today'][i] = {'complete': True, 'text': self.todo['today'][i]}

    def update(self, item, new_item):
        i = self.todo['today'].index(item)
        if i != -1:
            self.todo['today'][i] = new_item

    def show_todo(self):
        for i, text in enumerate(self.todo['today']):
            print("{i}. {text}".format(i=i, text=text))

    def sync(self):
        pass

if __name__ == "__main__":
    todo = Todo()
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--add", action="store", type=todo.add, help="add text to todo list")
    parser.add_argument("--delete-by-text", action="store", type=todo.delete_by_text, help="delete text in todo list")
    parser.add_argument("--delete-by-index", action="store", type=todo.delete_by_index, help="delete text in todo list by 0-indexed position")
    parser.add_argument("-l", "--list", action="store_true", help="show todo list")
    args = parser.parse_args()
    if args.list:
        todo.show_todo()
    else:
        todo.save()