# Dependencies
  - Python 3.7+
  - `pip3 install dropbox`

# To install:

  git clone https://github.com/imsteev/todo.git

  In .bashrc or .bash_profile..

    export PATH="<path_to_cloned_folder>:$PATH"

  source .bashrc | source .bash_profile

# Configuration

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
    "TODO_FILEPATH": "<path_to_todo.json>",
    "EXTERNAL_STORAGE_FILEPATH": "<path_in_storage_folder>"
}
```

# Usage

```
todo --add (or -a) text  # todo --add "get groceries at 3pm"
todo --update 2 new_text
todo --delete 5
todo --list  # show entire todo list
todo --push  # push todo to external storage
todo --pull  # pull todo from external storage

todo --help
```
