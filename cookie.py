from fastapi import Cookie, FastAPI, Header

app = FastAPI()

@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}

@app.get("/item/")
async def read_items(ads_id:list[str] | None = Header(default=None, convert_underscores=True)):
    #리스트로받을수도있고 단일로 받을 수도있음
    #주의사항 header는 ads_id 가 ads-id로 변경되어서 들어가야하기때문에 자동으로 바뀌는데 
    #이걸 허용하기 싫다면 convert_underscores=False를 넣어주면됨
    return {"ads_id": ads_id}