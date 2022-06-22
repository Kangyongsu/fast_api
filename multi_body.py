from fastapi import FastAPI, Body # 싱들 바디를 보내기 위해서 BODY 임포트
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User, importance: int = Body()):
    results = {"item_id": item_id, "item": item, "user": user,"importance": importance}
    return results

# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     },
#     "user": {
#         "username": "dave",
#         "full_name": "Dave Grohl"
#     },
#     "importance":"5"
# } => 보내는 body형태 


@app.put("/items/1/{item_id}")
async def update_item(item_id: int, item: Item=Body(..., embed =True)):
    results = {"item_id": item_id, "item": item}
    return results
#일반적으로 body가 하나면 통상적으로 키값을 넣지않는데 키값을 넣고 싶다면 embed= True를 넣어주자

#embed= True시에 body 값
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     }
# }

#embed= False시에 body 값
# {
#     "name": "Foo",
#     "description": "The pretender",
#     "price": 42.0,
#     "tax": 3.2
# }

