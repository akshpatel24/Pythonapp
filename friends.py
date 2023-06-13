from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
app=FastAPI()
class friends(BaseModel):
    id: int
    FirstName: str
    LastName: str
    Mobile: str


@app.get("/friends",response_model=friends)
def friends_info():
    return[
        {"id":2,"FirstName":"Aksh","Lastname":"Patel","Mobile":"Samsung"}
    
    ]