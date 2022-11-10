# create database models

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, VARCHAR,DateTime,Date
from sqlalchemy.orm import relationship

from app.database import Base

class Admin(Base):
    __tablename__ = "admin"

    admin_id = Column(Integer, primary_key=True, index=True)
    fname = Column(String)
    lname = Column(String)
    gender = Column(String)
    age = Column(Integer)
    contact = Column(Integer)
    admin_email = Column(String, unique=True, index=True)
    hashed_pwd = Column(String)
    # admin = relationship("Student","Book","Borrow")
    

class Student(Base):
    __tablename__ = "student"

    std_id = Column(Integer, primary_key=True, index=True)
    fname = Column(String)
    lname = Column(String)
    gender = Column(String)
    age = Column(Integer)
    contact = Column(Integer)
    std_email = Column(String, unique=True, index=True)
    admin_id = Column(Integer, ForeignKey("admin.admin_id"))
    admin = relationship("Admin")


class Book(Base):
    __tablename__ = "book"

    book_id = Column(Integer, primary_key=True, index=True)
    bk_title = Column(VARCHAR)
    bk_name = Column(VARCHAR)
    publisher = Column(VARCHAR)
    author = Column(VARCHAR)
    bk_num = Column(Integer)
    pub_date = Column(Date)
    admin_id = Column(Integer, ForeignKey("admin.admin_id"))
    admin = relationship("Admin")
    # book = relationship("Admin","Student","Borrow")


class Borrow(Base):
    __tablename__ = "borrowing"

    borrowing_id = Column(Integer,primary_key=True,index=True)
    book_id = Column(Integer,ForeignKey("book.book_id"))
    stud_id = Column(Integer,ForeignKey("student.std_id"))
    date_borrowed = Column(Date)
    date_return = Column(Date)
    book = relationship("Book")
    stud = relationship("Student")



