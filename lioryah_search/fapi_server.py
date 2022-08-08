# This file is written by Yair Dar and cloned from https://github.com/yairdar/ydu-202-searchapp
# with minor changes to fit my environment

from typing import Optional
import uvicorn
from fastapi import FastAPI 
import lib_search_sdk
from urllib.parse import unquote
from pathlib import Path

_me_parent = Path(__file__).absolute().parent.parent

app = FastAPI()


class DjfedosDbFacade:
    """Adapter Class to underlying actual implementation
    currently we hardcoded djfedeos implementation from https://github.com/djfedos/djfedos-search
    """
    
    def __init__(self) -> None:
        
        self.lib_search_sdk = lib_search_sdk
        self._db: dict = self.lib_search_sdk.init_db()
        
    def add_to_db(self, token):
        self.lib_search_sdk.add_to_db(self._db, token)
        return self
        
    def load_db(self, path: str):
        self._db = self.lib_search_sdk.load_db(path=path)
        return self
    
    def get_suggestions(self, prefix, limit=10):
        res = self.lib_search_sdk.get_suggestions(self._db, prefix=prefix, limit=limit)
        return res


_impl_db = DjfedosDbFacade()


@app.get("/")
def read_root():
    res =  {
        "msg": {"Hello": "World"},
        "menu": {
            "recreate": [
              "/load_db?path=data/2466_tokens.txt",
            ],
            "update": [
              "/add_to_db/token1",
              "/add_to_db/token2",
            ],
            "query":[
              "/get_suggestions/token",
            ]
        }
    }
    return res


# fixed this method to take a path as a query like this: host   /load_db?path=folder/token_file.txt
@app.get("/load_db")
def load_db(path: str):
    p = unquote(path)
    token_path = f'{_me_parent}/{p}'
    _impl_db.load_db(path=token_path)
    resp = {"path": path, "len": len(_impl_db._db)}
    return resp


@app.get("/add_to_db/{token}")
def add_to_db(token: str, q: Optional[str] = None):
    _impl_db.add_to_db(token=token)
    resp = {"token": token, "len": len(_impl_db._db)}
    return resp


@app.get("/get_suggestions/{prefix}")
def read_item(prefix: str, limit: Optional[int] = 10):
    res = _impl_db.get_suggestions(prefix=prefix, limit=limit)
    resp = {"prefix": prefix, "limit": limit, "result": res}
    return resp


def main():
    uvicorn.run(app, host="0.0.0.0", port=18000)


if __name__ == "__main__":
    main()