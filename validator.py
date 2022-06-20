from fastapi import FastAPI, Query # Query를 통해서 req.query에 대한 validation지정
from typing import Union, Optional , List # 리스트 파라미터를 받기위해서 import추가

app = FastAPI()

@app.get("/items")
async def read_items(q: str | None = Query(default=None,min_length=3, max_length=50, regex="^fixedquery$")): 
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
    
#str | None = Union[str,None]
#defalut = ... <=> defalit = None (...은 무조건 값이 들어가야한다는 명시적인 표현)
#async def read_items(q: str = Query(min_length=3, max_length=50, regex="^fixedquery$")): 이와같이 default value를 선언하지않고 만들수도 있음 
#defalut None는 Query를 사용하지않고도 쓸수있지만 max_length, min_length, regex와 같은 부분은 Query를 사용해야가능함

#리스트를 파리미터로 넣는 방법
@app.get("/items/list/")
async def read_items(q: list[str] | None = Query(default=None)):
#async def read_items(q: list[str] = Query(default=["foo", "bar"])): #와 같이 리스트의 defalut value 설정가능
    #list에서는 = None 으로 default value를 넣으면 none이 뜨므로 Query(default=None) 로 defalut value를 설정할것
    print(q)
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#query를 list로 넣는다고 해서 http://127.0.0.1:8000/items/list/?q=[str1,str2] 로 하게되면 => {"items":[{"item_id":"Foo"},{"item_id":"Bar"}],"q":["[tes,rerer]"]} 와 같이 q부분이 문자열리스트가 되므로
# http://127.0.0.1:8000/items/list/?q=str1&q=str2 로 표현해야 리턴값이 리스트로 옴        => {"items":[{"item_id":"Foo"},{"item_id":"Bar"}],"q":["str1","str2"]}

@app.get("/items/list2/")
async def read_items(q: list= Query(default=None), 
                        title="Query string", 
                        description="Query string for the items to search in the database that have a good match",
                        alias = "item-query",
                        deprecated=True,):
#async def read_items(q: list= Query(default=[])): # 리턴값 =  {q: []}
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
#title 과 description alias, deprecated는 docs의  보충설명에 관한 내용
