from typing import Any
from fastapi import FastAPI
import uvicorn
from datetime import datetime

from pydantic import BaseModel
app=FastAPI()
class Item(BaseModel):
    name:str
    description:str| None=None
    price:float
    tax:float      | None=None
    tags:list[str]=[] 
    bar:datetime


class Item2(BaseModel)
    a:Item

foo=Item2(a={name})


@app.post("/items/",response_model=Item)
def create_item(item:Item):
    return item


@app.get("/items/",response_model=list[Item])
def read_item():
    return[
        {"name":"aksh","price":32,"bar":datetime()

        {"name":"portal gun","price":42.0,"bar":datetime(2023,6,21)},
        {"name":"plumbus","price":32.0},

    ]










if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
