from typing import Union

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0 , le = 1000),
    #int 파라미터validation시에 0~1000사이의 값을 넣음 
    q: str | None = Query(default=None,min_length=10, max_length =100)
    #string파라미터 검증시에는 max_length, min_length와 같은 부분 활용
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results