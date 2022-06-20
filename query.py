from fastapi import FastAPI
from pydantic import BaseModel #타입검열
from enum import Enum #enum타입 선언

app = FastAPI()

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
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]