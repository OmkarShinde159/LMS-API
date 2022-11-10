from pydantic import BaseModel
from datetime import datetime, date
from typing import List





class StudentBase(BaseModel):
    fname : str
    lname : str
    gender : str
    age : int
    contact : int
    std_email : str
    
  
class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    std_id : int

class Student(StudentBase):
    std_id : int
    admin_id : int

    class Config:
        orm_mode = True  
    

class BookBase(BaseModel):
    bk_title : str
    bk_name : str
    publisher : str
    author : str
    bk_num : int
    pub_date : date

class BookCreate(BookBase):
    pass 

class Book(BookBase):
    book_id : int
    admin_id : int

    class Config:
        orm_mode = True
    


class BorrowBase(BaseModel):
    book_id : int
    date_borrowed : date
    date_return : date

class BorrowCreate(BorrowBase):
    pass 

class Borrow(BorrowBase):
    borrowing_id : int
    stud_id : int

    class Config:
        orm_mode = True


# common attributes while creating and reading admin data
class AdminBase(BaseModel):
    admin_email:str
    fname :str
    lname : str
    gender: str
    age: int
    contact: int

# additional parameters while creating
class AdminCreate(AdminBase):
    password : str 

# additional parameters while reading   
class Admin(AdminBase):
    admin_id : int
    admin : List[Student] = []
    admin : List[Book] = []
    admin : List[Borrow] = []

    class Config:
        orm_mode = True

