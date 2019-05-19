# Setup

  ```
  git clone https://github.com/imsteev/todo.git
  ```

  Add the project folder to your PATH

### Configuration

Create a config.json:

```
{
    "apps": {
        "dropbox": {
            "appKey": "yourAppKey",
            "appSecret": "yourAppSecret",
            "accessToken": "yourAccessToken"
        }
    },
    "TODO_FOLDER": "/Users/Stephen/Developer/todo/",
    "TODO_FILENAME": "todo.json",
    "EXTERNAL_TODO_FILEPATH": "<path_in_storage_folder>"
}
```

# Usage

```
todo --help

todo --add (or -a) text  # todo --add "get groceries at 3pm"
todo --update 2 new_text
todo --delete 5
todo --clear  # clear todo list
todo --link 1 'http://google.com'  # add a link to item 1
todo --show  # show entire todo list
todo --push  # push todo to external storage
todo --pull  # pull todo from external storage
```

# Dependencies
  - Python 3.7+
  - `pip3 install dropbox`
