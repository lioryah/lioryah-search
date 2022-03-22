#%%

from typing import Iterable, List
#import fire

'''
Methods list:
* init_db() -> dict
    return {} 

* add_to_db(mdb:dict, token:str) -> bool

* iterate_tokens(path:str)-> Iterable[str]:

* find_prefix(mdb:dict, prefix: str) -> dict
  start from root mdb and returns root for end of prefix

* iterate_suffixes(mdb:dict) -> Iterable[str]

* retrive_suffixes_by_prefix(mdb, prefix, limit) -> List[str]

declarared for outside use api:
* load_db(path: str = None):
  use init_db and then if path is not None`add_to_db` 

* add_to_db (from before)

* get_sugestions(mdb:dict, prefix: str, limit: int)
  * retrive_suffixes_by_prefix


'''


def init_db() -> dict:
    return {} 


def add_to_db(mdb:dict, token:str) -> bool:
    if token == '':
        mdb['_end'] = '_end'
        return True
    else:
        first = token[0]
        rest = token[1:] 
        if first not in mdb:
            mdb[first] = {}
        add_to_db(mdb[first], rest)
    

###################
def iterate_tokens(path:str)-> Iterable[str]:
    pass


def find_prefix(mdb:dict, prefix: str) -> dict:
   # start from root mdb and returns root for end of prefix
    if prefix == '':
        return mdb
    else:
        first = prefix[0]
        if first in mdb:
            return find_prefix(mdb[first], prefix[1:])


def recur_suffix(mdb:dict, end_flag=False, path_list=[]):
    if not end_flag: 
        
        if '_end' in mdb:
            end_flag = True
            if(len(mdb.keys()) != 1):
                mdb.pop('_end')
            return  ''.join(path_list)
        else:
            for k in mdb.keys():
                path_list.append(k)
                break
    return recur_suffix(mdb[k], end_flag, path_list)
            

def iterate_suffixes(mdb:dict) -> Iterable[str]:
    yield recur_suffix(mdb)


def iterate_suffixes2(mdb:dict, end_flag=False, path_list=[]) -> Iterable[str]:
    parent_dict = mdb
    for key_curr_dict in parent_dict.keys():
        curr_dict = parent_dict[key_curr_dict]
        path_list.append(key_curr_dict)
        while not end_flag: 
            
            if '_end' in curr_dict :
                end_flag = True
                
                #if(len(curr_dict.keys()) != 1):
                #if len(curr_dict) != 1:
                #    curr_dict.pop('_end')
                #else:
                
                
                yield  ''.join(path_list)
                
                curr_dict = remove_path_from_db(parent_dict,path_list)

                #curr_dict.pop('_end')
                end_flag = False
                break
                '''
                if len(curr_dict) == 1:
                    break
                else:
                    continue
                '''
            #if curr_dict == {}:
            #    curr_dict.pop(k)
            for k in curr_dict.keys():
                
                parent_dict = curr_dict
                curr_dict = curr_dict[k]
                path_list.append(k)
                
                break


def remove_path_from_db (db:dict, path:List[str])->dict:
    '''
    parent_db = db

    if '_end' in parent_db[path[0]] and len(path) > 1:
        return db.pop(path[0])
    
    else:
        db = db[path[0]]
        path = path[1:]
        return remove_path_from_db(db,path).popitem()
        '''


    '''
    if len(path) == 1:
        return db.pop(path[0])
    '''

    curr_db = db   
    
    for i in range(len(path)):
        curr_db = db[path[i]]
    
    if '_end' in curr_db:
        curr_db.pop('_end')


    '''
    if len(path) == 1:
        return db.pop('_end')
'''

def retrive_suffixes_by_prefix(mdb:dict, prefix:str, limit:int) -> List[str]:
    pass


# declarared for outside use api

def get_sugestions(mdb:dict, prefix: str, limit: int):
    completions = []
    suffix_dict = find_prefix(mdb,prefix)
    if suffix_dict == {}:
        return completions
    if suffix_dict == {'_end':'_end'}:
        return ['']

    single_suffix = iterate_suffixes2(suffix_dict)
    i=0
    while i<limit:
        completions.append(next(single_suffix))
        print(completions[i])
        i+=1
    print(completions)
    return completions
# retrive_suffixes_by_prefix
    
def load_db(path: str = None):
    db = init_db()
    if path is not None:
        ftokens = open(path, "r")
        for line in ftokens:
            if line.endswith('\n'): 
                token = line[:-1]
            else: 
                token = line
            add_to_db(db, token)
    return db

'''
def main_():
    #fire.Fire()
    my_db = load_db('lioryah_search/tokens1.txt')
    print(my_db)

if __name__ == '__main__':
    main_() 
'''


#%%
my_db = load_db('tokens1.txt')
print(my_db)

get_sugestions(my_db, 'ba', 4)
# %%
