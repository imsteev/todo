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
