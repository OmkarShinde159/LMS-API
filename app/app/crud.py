from sqlalchemy.orm import Session
from app import models,schemas
from typing import List
from fastapi import FastAPI,Depends,HTTPException

def get_admin(db:Session, admin_id:int):
    return db.query(models.Admin).filter(models.Admin.admin_id == admin_id).first()

def get_student(db:Session, std_id:int):
    return db.query(models.Student).filter(models.Student.std_id == std_id).first()

def get_book(db:Session, book_id:int):
    return db.query(models.Book).filter(models.Book.book_id == book_id).first()

def get_borrow(db:Session, borrowing_id:int):
    return db.query(models.Borrow).filter(models.Borrow.borrowing_id == borrowing_id).first()



def get_admin_by_email(db:Session,admin_email:str):
    return db.query(models.Admin).filter(models.Admin.admin_email == admin_email).first()

def get_student_by_email(db:Session,std_email:str):
    return db.query(models.Student).filter(models.Student.std_email == std_email).first()



def get_admins(db:Session, skip:int=0, limit:int=100):
    return db.query(models.Admin).offset(skip).limit(limit).all()

def get_students(db:Session, skip:int=0, limit:int=100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def get_books(db:Session, skip:int=0, limit:int=100):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_borrowings(db:Session, skip:int=0, limit:int=100):
    return db.query(models.Borrow).offset(skip).limit(limit).all()



def create_admin(db:Session, admin: schemas.AdminCreate):
    fake_hashed_pw = admin.password + " notreallyhashed"
    # db_admin = models.Admin(**admin.dict(),hashed_pwd = fake_hashed_pw)
    db_admin = models.Admin(
        admin_email = admin.admin_email,
        fname = admin.fname,
        lname = admin.lname,
        gender = admin.gender,
        age = admin.age,
        contact = admin.contact,
        hashed_pwd = fake_hashed_pw)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin

def create_student_by_admin(db:Session, student:schemas.StudentCreate, admin_id:int):
    db_student = models.Student(**student.dict(),admin_id=admin_id)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def create_book_by_admin(db:Session, book:schemas.BookCreate, admin_id:int):
    db_book = models.Book(**book.dict(), admin_id=admin_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def create_borrow(db:Session, borrow:schemas.BorrowCreate, std_id:int):
    db_borrow = models.Borrow(**borrow.dict(), stud_id=std_id)
    db.add(db_borrow)
    db.commit()
    db.refresh(db_borrow)
    return db_borrow



        



