from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/")
async def post():
    return {{"Hello": "World from post method"}}


@app.put("/")
async def put():
    return {{"Hello": "World from post method"}}


@app.get("/items")
async def list_items():
    return {"message": "List items route"}


@app.get("/items/{item_id}")
async def get_items(item_id: int):
    return dict(item={"item_id": item_id, "item_name": f'item sample {item_id}'})
