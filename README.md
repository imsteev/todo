# Setup
  ```
  git clone https://github.com/imsteev/todo.git
  cd todo
  pip3 install -r requirements.txt  # consider installing within a virtualenv
  ```

  Add the project folder to your PATH
  
### Configuration

Create a config.json:

```
{
    "3p": {
        "dropbox": {
            "appKey": "yourAppKey",
            "appSecret": "yourAppSecret",
            "accessToken": "yourAccessToken"
        }
    },
    "TODO_FOLDER": "/full/path/to/todo",
    "EXTERNAL_TODO_FOLDER": "/app/todos"
    "TODO_FILENAME": "todo.json"
}
```

# Usage

```
todo --help

todo --add text                    # add new item to the todo list
todo --update 2 "new text"         # update item 2 with text "new text"
todo --delete 5                    # delete item 5
todo --clear                       # clear todo list
todo --link 1 'http://google.com'  # add a link to item 1
todo --goto 1                      # if it exists, open browser for a link attached to item 1
todo --toggle-complete 1           # toggle the complete status for item 1
todo --show                        # show entire todo list
todo --push                        # push todo to external storage
todo --pull                        # pull todo from external storage
todo --sync                        # naive sync with external storage
```
