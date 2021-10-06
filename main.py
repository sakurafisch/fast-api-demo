from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root() -> dict:
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None) -> dict:
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8181, log_level="info")
