from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
app=FastAPI()
class friends(BaseModel):
    id: int
    FirstName: str
    LastName: str
    Mobile: str
@app.get("/friends",response_model=list[friends])
def friends_info():
    return[
        {"id":2,"FirstName":"Aksh","LastName":"Patel","Mobile":"Samsung"},
        {"id":4,"FirstName":"Ami","LastName":"Porter","Mobile":"Iphone"},
        {"id":5,"FirstName":"Akshay","LastName":"Pat","Mobile":"Apple"},
        {"id":6,"FirstName":"Amiy","LastName":"Portery","Mobile":"Ie"},
        {"id":3,"FirstName":"Aksh","LastName":"Petel","Mobile":"chen"},
        {"id":7,"FirstName":"Aiy","LastName":"Pety","Mobile":"sony"}
    ]







if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
