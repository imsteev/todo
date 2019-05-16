# To install:

  git clone https://github.com/imsteev/todo.git

  In .bashrc or .bash_profile..

    export PATH="<path_to_cloned_folder>:$PATH"

  source (.bashrc | .bash_profile)

# Configuration

Create a config.json, that looks like:

{
    "apps": {
        "dropbox": {
            "appKey": "yourAppKey",
            "appSecret": "yourAppSecret",
            "accessToken": "yourAccessToken"
        }
    }
}