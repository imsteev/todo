import json
import os
import tempfile

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

def sync(src=TODO_FILE, sync_src=EXTERNAL_TODO_FILEPATH):
    """
    WIP: right now all this does is append the 'items' in external storage to the local todo file
    """
    external_json = None
    local_json = None

    # load file stored externally
    with tempfile.NamedTemporaryFile() as tmpfile:
        pull(dest=tmpfile.name, src=EXTERNAL_TODO_FILEPATH)
        external_json = json.load(tmpfile)

    # load file stored locally
    with open(src, 'r') as f:
        local_json = json.load(f)

    local_json['items'].extend(external_json['items'])

    with open(src, 'w') as f:
        json.dump(local_json, f)
