#!/usr/local/bin/python3
import argparse
import json
import dropbox
from dropbox.files import WriteMode

with open('config.json', 'r') as f:
    config = json.load(f)

dbx = dropbox.Dropbox(config['apps']['dropbox']['accessToken'])

DEFAULT_TODO_FILE = '/Users/Stephen/Developer/todo/todo.json'
EXTERNAL_STORAGE_FILE = '/steevetodo/todo.json'

class Todo(object):
    def __init__(self, source=DEFAULT_TODO_FILE):
        self.source = source
        self.todo = self.get(self.source)

    def save(self, dest=DEFAULT_TODO_FILE):
        dest = dest or self.source
        with open(dest, 'w') as f:
            json.dump(self.todo, f)

    def show(self):
        for i, text in enumerate(self.todo['today']):
            print("{i}. {text}".format(i=i, text=text))

    def push(self):
        with open(self.source, 'rb') as f:
            dbx.files_upload(f.read(), EXTERNAL_STORAGE_FILE, WriteMode('overwrite'))

    def pull(self):
        pass

    def get(self, source=DEFAULT_TODO_FILE):
        with open(source, 'r') as f:
            ret = json.load(f)
            if not isinstance(ret, dict):
                raise ValueError('todo currently only supports objects. are you using the right file?')

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

    def update(self, i, new_item):
        self.todo['today'][i] = new_item

if __name__ == "__main__":
    todo = Todo()
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--add", action="store", type=todo.add, help="add text to todo list")
    parser.add_argument("-u", "--update", nargs=2, metavar=('index', 'text'), action="store", help="update todo item at 1-indexed position i")
    parser.add_argument("-d", "--delete", type=int, help="delete text in todo list by 1-indexed position")
    parser.add_argument("-l", "--list", action="store_true", help="show todo list")
    parser.add_argument("--push", action="store_true", help="push todo to external storage")
    parser.add_argument("--pull", action="store_true", help="pull todo from external storage")
    args = parser.parse_args()

    if args.delete:
        todo.delete_by_index(args.delete - 1)
    elif args.update:
        todo.update(int(args.update[0]) - 1, args.update[1])
    elif args.push:
        todo.push()
    elif args.pull:
        todo.pull()
    elif args.list:
        todo.show()

    todo.save()
