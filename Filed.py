from fastapi import Body, FastAPI
from pydantic import BaseModel, Field, HttpUrl 
# url주소에 대한 validation이 적용됨
#Field는 모델클래스에서 validation을 하기위해서 import함

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero") 
    # 사용법은 Query,Path와 동일함
    tax: float | None = None
    tags: list[str|int] = []
    #tags: set[str|int] = set() => set으로 선언하고플시 이와같이 선언가능함

    image: Image | None = None #nested model로서 위에 선언한 image클래스를 사용할 수 있음
    #ex2 images : list[Image] | None = None 

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

#위 api의 body 보면은 선언한 image가 끼어들어간걸 볼 수 있음
# {
#     "name": "Foo",
#     "description": "The pretender",
#     "price": 42.0,
#     "tax": 3.2,
#     "tags": ["rock", "metal", "bar"],
#     "image": {
#         "url": "http://example.com/baz.jpg",
#         "name": "The Foo live"
#     }
# }

# ex2
# {
#     "name": "Foo",
#     "description": "The pretender",
#     "price": 42.0,
#     "tax": 3.2,
#     "tags": ["rock", "metal", "bar"],
#      "images": [
#     {
#         "url": "http://example.com/baz.jpg",
#         "name": "The Foo live"
#     },
#     {
#         "url": "http://example.com/dave.jpg",
#         "name": "The Baz"
#     }
# ]
# }

@app.post("/items/{item_id}")
async def create_item(item_id: int, item:list[Item]):
    print(item)
    result = {"item":item}
    return result
    
#들어가는 body가 리스트로 들어가기 원하면 위와같이 표현가능
# [
#     {"name": "Foo",
#     "description": "The pretender",
#     "price": 42.0,
#     "tax": 3.2}
# ]

    




