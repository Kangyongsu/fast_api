from fastapi import FastAPI
from pydantic import BaseModel 
from enum import Enum 
from typing import Union, Optional

# class Item(BaseModel):
#     name :str
#     description : Union[str,None] = None
#     price : float
#     tax : Union[float,None]= None

app = FastAPI()

@app.post("/items/{item_id}")
async def create_item(item_id: int, item:dict[str,str,float,float]):
    print(item)
    result = {"item":item}
    return result
    

