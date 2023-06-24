from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Session
from sqlalchemy import create_engine
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import declarative_base #fix this
from sqlalchemy.orm import sessionmaker
import uvicorn
from sqlalchemy import Table
# import schemas  # Make sure to import 'final' module
import urllib
import pyodbc
from urllib.parse import quote_plus


connection_string='mysql+pymysql://AKSHPATEL:Umasslowel24!@localhost:8000/Learning'
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234567!@localhost:5432/postgres"
params=quote_plus("Driver={SQL Server};"
            "Server=DESKTOP-9DHBJDE;"
            "Database=Learning;"
            "UID=sa;PWD=Umasslowel24!")
engine = create_engine(connection_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

class Student(Base):
     __tablename__='Student'
     ID=Column(Integer)
     Firstname=Column(String(50))
     Semester=Column(Integer)
# class book(Base):
#      __tablename__='book'
#      title= Column(String(50))
#      author = Column(String(50))
#      bookid = Column(Integer, primary_key=True)
@app.get("/student")
def calling():
    session = SessionLocal()
    return session.query(Student).all()
# @app.post("/books", response_model=schemas.bookSchema)
# def create_book(book_data: schemas.bookSchema, db: Session = Depends(get_db)):
#     new_book = book(title=book_data.title, author=book_data.author)
#     db.add(new_book)
#     db.commit()
#     db.refresh(new_book)  
#     return new_book
if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)
