#!/usr/local/bin/python3
import argparse
import json
import manager

class Todo(object):
    def __init__(self, source):
        self.source = source
        self.todo = self.get(self.source)

    def get(self, source):
        with open(source, 'r') as f:
            ret = json.load(f)
            if not isinstance(ret, dict):
                raise ValueError('todo currently only supports objects. are you using the right file?')

        if not 'today' in ret:
            ret['today'] = []

        return ret

    def save(self):
        with open(self.source, 'w') as f:
            json.dump(self.todo, f)

    def show(self):
        """
        1. item text
        2. item text
        ..
        """
        for i, text in enumerate(self.todo['today']):
            print("{i}. {text}".format(i=i+1, text=text))

    def add(self, item):
        self.todo['today'].append(item)

    def update(self, i, new_item):
        self.todo['today'][i] = new_item

    def delete(self, stuff):
        if isinstance(stuff, int):
            self.delete_by_index(stuff)
        else:
            raise ValueError('delete does not support deleting by {}'.format(type(stuff)))

    def delete_by_index(self, i):
        if i < 0 or i >= len(self.todo['today']):
            raise ValueError

        del self.todo['today'][i]

    def mark_complete(self, item):
        i = self.todo['today'].index(item)
        if i != -1:
            self.todo['today'][i] = {'complete': True, 'text': self.todo['today'][i]}

if __name__ == "__main__":
    todo = Todo(manager.DEFAULT_TODO_FILE)
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--add", nargs=1, metavar=('text'), action="store", help="add text to todo list")
    parser.add_argument("-u", "--update", nargs=2, metavar=('index', 'text'), action="store", help="update todo item at 1-indexed position i")
    parser.add_argument("-d", "--delete", type=int, help="delete text in todo list by 1-indexed position")
    parser.add_argument("-l", "--list", action="store_true", help="show todo list")
    parser.add_argument("--push", action="store_true", help="push todo to external storage")
    parser.add_argument("--pull", action="store_true", help="pull todo from external storage")
    args = parser.parse_args()

    if args.add:
        todo.add(args.add[0])
    elif args.delete:
        todo.delete_by_index(args.delete - 1)
    elif args.update:
        todo.update(int(args.update[0]) - 1, args.update[1])
    elif args.push:
        manager.push(todo.source)
    elif args.pull:
        manager.pull()
        todo = Todo(manager.DEFAULT_TODO_FILE)
        todo.show()
    elif args.list:
        todo.show()

    if any([args.add, args.delete, args.update]):
        todo.save()
