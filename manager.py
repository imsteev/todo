import json
import os

import dropbox
from dropbox.files import WriteMode

with open('config.json', 'r') as f:
    config = json.load(f)

dbx = dropbox.Dropbox(config['apps']['dropbox']['accessToken'])

TODO_FOLDER = config['TODO_FOLDER']
TODO_FILE = os.path.join(TODO_FOLDER, config['TODO_FILENAME'])
EXTERNAL_TODO_FILEPATH = config['EXTERNAL_TODO_FILEPATH']

def push(dest=EXTERNAL_TODO_FILEPATH, src=TODO_FILE):
    with open(src, 'rb') as f:
        dbx.files_upload(f.read(), EXTERNAL_TODO_FILEPATH, WriteMode('overwrite'))

def pull(dest=TODO_FILE, src=EXTERNAL_TODO_FILEPATH):
    dbx.files_download_to_file(dest, src)
