import dropbox
from dropbox.files import WriteMode
import json

with open('config.json', 'r') as f:
    config = json.load(f)

dbx = dropbox.Dropbox(config['apps']['dropbox']['accessToken'])

TODO_FILE = config['TODO_FILEPATH']
EXTERNAL_STORAGE_FILEPATH = config['EXTERNAL_STORAGE_FILEPATH']

def push(filepath):
    with open(filepath, 'rb') as f:
        dbx.files_upload(f.read(), EXTERNAL_STORAGE_FILEPATH, WriteMode('overwrite'))

def pull():
    dbx.files_download_to_file(TODO_FILE, EXTERNAL_STORAGE_FILEPATH)
