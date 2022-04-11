# lioryah-search
An implementation of a database completions of word by prefix application over a fastAPI web server.

## Prerequisites
fastAPI, uvicorn and pytest used for implementing  a web server and testing.  

```shell
pip install fastapi
pip install uvicorn
pip install pytest 
```

## Workflow of database completions of words 
### Creating a databse
First off we want to create a databse of tokens from a .txt file.  
For this purpose we use `load_db(path:str)`. 
This functions returns us the database in a form of nested dictionary.

### Updating (adding) database
We use `add_to_db(mdb:dict, token:str)` to add a `token` to `mdb`

### Searching for completions by prefix
In order to search the database `mdb` for `limit` number of tokens that began with `prefix` we'll use `get_suggestions(mdb:dict, prefix:str, limit:int=10)`
This function will return a list of tokens from our database.

### Creating a fastAPI server 
To create a fastAPI web server that eventually will support creating a server based database, update the db and response to `get_suggstion` queries from the db by a client.

``` shell
python fapi_server.py
```

## Tests
* `test_lib_search_sdk.py` contain all tests regarding to search functionality
* `test_web_api.py` contain all tests regarding web server API by using TestClient

  We use pytest to run tests as follows: 

  ```shell
  > pytest # while in working directory
  ```

  or via Testing sidebar GUI
## Overview
- `data` contains token sets of somekind
- `lioryah_search` server, client, search and tests



