import json
import os
import tempfile

import dropbox
from dropbox.files import WriteMode

with open('config.json', 'r') as f:
    config = json.load(f)

dbx = dropbox.Dropbox(config['apps']['dropbox']['accessToken'])

TODO_FOLDER = config['TODO_FOLDER']
EXTERNAL_TODO_FOLDER = config['EXTERNAL_TODO_FOLDER']

TODO_FILE = os.path.join(TODO_FOLDER, config['TODO_FILENAME'])
EXTERNAL_TODO_FILE = os.path.join(EXTERNAL_TODO_FOLDER, config['EXTERNAL_TODO_FILENAME'])

def push(src=TODO_FILE, dest=EXTERNAL_TODO_FILE):
    with open(src, 'rb') as f:
        dbx.files_upload(f.read(), dest, WriteMode('overwrite'))

def pull(src=EXTERNAL_TODO_FILE, dest=TODO_FILE):
    dbx.files_download_to_file(dest, src)

def sync(src=TODO_FILE, sync_with=EXTERNAL_TODO_FILE):
    """
    WIP: right now all this does is append the 'items' in external storage to the local todo file
    """
    external_json = None
    local_json = None

    # load file stored externally
    with tempfile.NamedTemporaryFile() as tmpfile:
        pull(src=sync_with, dest=tmpfile.name)
        external_json = json.load(tmpfile)

    # load file stored locally
    with open(src, 'r') as f:
        local_json = json.load(f)

    local_json['items'].extend(external_json['items'])

    with open(src, 'w') as f:
        json.dump(local_json, f)

    push(src=src, dest=sync_with)
