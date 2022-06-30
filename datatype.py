from datetime import datetime, time, timedelta
from uuid import UUID

from fastapi import Body, FastAPI

app = FastAPI()

@app.put("/items/{item_id}")
#UUID는 128비트의 숫자이며, 32자리의 16진수로 표현된다. 여기에 8-4-4-4-12 글자마다 하이픈을 집어넣어 5개의 그룹으로 구분한다.
#ex) 550e8400-e29b-41d4-a716-446655440000
async def read_items(
    item_id: UUID,
    start_datetime: datetime | None = Body(default=None),
    end_datetime: datetime | None = Body(default=None),
    repeat_at: time | None = Body(default=None),
    process_after: timedelta | None = Body(default=None),
):
    # ISO 8601 포맷팅
    #datatime ex) 2008-09-15T15:53:00+05:00 
    #data ex ) 2008-09-15
    #time ex ) 14:23:55.003
    #timedelta datatime과의 날짜차이 float타입
    start_process = start_datetime + process_after
    duration = end_datetime - start_process

    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }