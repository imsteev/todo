import dropbox
from dropbox.files import WriteMode
import json

with open('config.json', 'r') as f:
    config = json.load(f)

dbx = dropbox.Dropbox(config['apps']['dropbox']['accessToken'])

DEFAULT_TODO_FILE = '/Users/Stephen/Developer/todo/todo.json'
EXTERNAL_STORAGE_FILE = '/steevetodo/todo.json'

def push(filepath):
    with open(filepath, 'rb') as f:
        dbx.files_upload(f.read(), EXTERNAL_STORAGE_FILE, WriteMode('overwrite'))

def pull():
    dbx.files_download_to_file(DEFAULT_TODO_FILE, EXTERNAL_STORAGE_FILE)
