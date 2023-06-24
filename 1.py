from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
import urllib
import uvicorn
from fastapi import FastAPI

app=FastAPI()

conn=urllib.parse.quote_plus(

'Driver={SQL Server};'
'Server=DESKTOP-9DHBJDE;'
'Database=Learning;'
'UID=sa;PWD=Umasslowel24!'
)


try:
    engine=create_engine('mssql+pyodbc:///?odbc_connect={}'.format(conn))
    print("passed")
except:
    print("failed")

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()
session=SessionLocal()
class Student(Base):
    __tablename__="Studentdata"
    ID=Column(Integer,primary_key=True,index=True)
    SName=Column(String)
    Area=Column(String)
    Phone=Column(String)

@app.get("/")
async def root():
    students=session.query(Student).all()
    return students
@app.get("/{id}")
async def getById(id:int):
    student=session.query(Student).filter(Student.ID==id).first() # ID is from base and or sql heading. id path parameter
    return student

@app.get("/item")
async def getItems():
    return{"message":"From items"}



# @app.get("/hello")
# def hello():
#     return {"Hello world"}

# @app.get("/items/{item_id}")
# def read_item(item_id:int):
#     # return {"item_id":item_id}
#     return item_id



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

