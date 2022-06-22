from fastapi import FastAPI
from pydantic import BaseModel # 클래스의 모델 정의
from enum import Enum #enum타입 선언
from typing import Union, Optional

class Item(BaseModel):
    name :str
    description : Union[str,None] = None
    price : float
    tax : Union[float,None]= None

app = FastAPI()

#req.query,params,body를 한번에 넣음
@app.post("/items/{item_id}")
async def create_item(item_id: int , item: Item, q : Optional[int]=None  ): #Item클래스에있는 모든 값을 가져옴
    # 파라미터 넣는 순서유의 해야함 => defalut밸류가 None인 애들은 맨 마지막에 선언해야 에러뜨지않음
    # why? 생략이 가능하기때문에 생략이 불가능한 매개변수보다 먼저 선언할 수 없음

    item = item.dict() #dict라는 내장함수로 딕셔너리화
    # item.dict()를 안했을때의 값 name='강용수' description='묘사' price=32.3 tax=12.3
    # item.dict()를   했을때의 값 {'name': '강용수', 'description': '묘사', 'price': 32.3, 'tax': 12.3}
    result = {"item_id":item_id , **item} # *
    if q:
        result.update({"q": q})

    return result
    

