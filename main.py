from fastapi import FastAPI
from enum import Enum #enum타입 선언
from typing import Union ,Optional
from models import auto_complete
from mongoengine import connect
import json

connect(db = 'auto_complete', host='localhost', port=27017)

app = FastAPI()

@app.get("/test")
def get_test():
    autoComplete = auto_complete.objects().to_json()
    list_ = json.loads(autoComplete)

    return {"auto_complete":list_}

class enumTest(str,Enum):
    name1= "맥크리"
    name2= "트레이서"
    name3= "메이"

@app.get("/name/{name_id}") #req.params 방식으로 처리
async def root(name_id:str): #타입변환안되면 에러뜸
    return {"name":name_id}


#enum을 활용한 req.params설정
@app.get("/nameTest/{enum_test}") 
async def root(enum_test:enumTest): # enumTest에 있는 값을 받아옴
    
    if(enum_test.name1 =='맥크리'):
    #print(enum_test.value == '맥크리') .value로 사용해도 됨
        return {"name":enumTest.name1}
    else:
        return {"name":"맥크리가 아님"} #enum을 파라미터로 받았으니 enum값이 아니라면 오류

#일반적인 req.params설정
@app.get("/pathTest/{file_path:path}") 
async def root(file_path: str):
    return file_path

#일반적인 req.query설정
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10): #skip은 int형의 0 이라는 값을 가지고 limit은 int형의 10이라는 값을 가진다
    return fake_items_db[skip : skip + limit] 

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None): #Union을통해서 str이나 none을 넣어서 선택적 매개변수로 활용할 수 있음 =None는 디폴트밸류
    if q:
        print(q)                
        return {"item_id": item_id, "q": q}
    print(q)
    return {"item_id": item_id}

@app.get("/items/test/{item_id}")
async def read_item(item_id: str, q:Optional[str]=None, short :bool =True): #Union과 비슷하지만 Optional은 1개의 매개변수만 허용됨
    item = {"item_id":item_id}
    if q:
        item.update({"q":q}) #q가존재하면 item에 q를 추가함 ex) {"item_id":"tt","q":"tt"}
    if not short:
        item.update(
            {"description":'This is an amazing item that has a long description'}
        )
    return item

#http://127.0.0.1:8000/items/test/tt?short=1
#http://127.0.0.1:8000/items/test/tt?short=True
#http://127.0.0.1:8000/items/test/tt?short=true
#http://127.0.0.1:8000/items/test/tt?short=on
#http://127.0.0.1:8000/items/test/tt?short=yes
#bool형 타입은 이 5가지로 표현 할 수 있음