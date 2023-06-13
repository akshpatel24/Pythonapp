from typing import Any
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
app=FastAPI()
class Item(BaseModel):
    name:str
    description:str| None=None
    price:float
    tax:float      | None=None
    tags:list[str]=[] 


@app.post("/items/",response_model=Item)
def create_item(item:Item):
    return item


@app.get("/items/",response_model=list[Item])
def read_item():
    return[
        {"name":"portal gun","price":42.0},
        {"name":"plumbus","price":32.0},
    ]










if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
