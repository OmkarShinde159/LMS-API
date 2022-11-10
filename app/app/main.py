from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from app import models,database,schemas,crud
from app.database import SessionLocal, engine
from typing import List

# create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Hello World"}

# admin operations 

@app.post("/admin/",response_model=schemas.Admin)
def create_admin(admin:schemas.AdminCreate, db:Session=Depends(get_db)):
    db_admin = crud.get_admin_by_email(db, admin_email=admin.admin_email)
    if db_admin:
        raise HTTPException(status_code=400, detail="Email already registered")
    # return crud.create_admin(db=db, admin=admin)
    return crud.create_admin(db, admin)

@app.get("/admin/", response_model=list[schemas.Admin])
def get_admins(skip:int=0, limit:int=100, db:Session=Depends(get_db)):
    admins = crud.get_admins(db, skip=skip, limit=limit)
    return admins

@app.get("/admin/{admin_id}",response_model=schemas.Admin)
def get_admin(admin_id:int, db:Session = Depends(get_db)):
    db_admin = crud.get_admin(db, admin_id=admin_id)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_admin

# admin operations on students

@app.post("/admin/{admin_id}/student/",response_model=schemas.Student)
def create_student_by_admin(admin_id : int, student:schemas.StudentCreate, db:Session = Depends(get_db)):
    db_student = crud.get_student_by_email(db, std_email=student.std_email)
    # print(db_student)
    if db_student:
        raise HTTPException(status_code=400, detail="Email already registered")
    # print(crud.create_student_by_admin(db=db, student=student, admin_id=admin_id))
    return crud.create_student_by_admin(db, student, admin_id)

@app.get("/student/",response_model=list[schemas.Student])
def get_students(skip:int=0, limit:int=100, db:Session=Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students

@app.get("/student/{std_id}",response_model=schemas.Student)
def get_student(std_id:int, db:Session = Depends(get_db)):
    db_student = crud.get_student(db, std_id=std_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_student


# admin operation on books
@app.post("/admin/{admin_id}/book/",response_model=schemas.Book)
def create_book_by_admin(admin_id : int, book:schemas.BookCreate, db:Session = Depends(get_db)):
    return crud.create_book_by_admin(db, book, admin_id)

@app.get("/book/",response_model=list[schemas.Book])
def get_students(skip:int=0, limit:int=100, db:Session=Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books

@app.get("/book/{book_id}",response_model=schemas.Book)
def get_student(book_id:int, db:Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_book


# admin operation on borrow
@app.post("/borrow/{std_id}", response_model=schemas.Borrow)
def create_borrow(std_id:int, borrow:schemas.BorrowCreate, db:Session=Depends(get_db)):
    return crud.create_borrow(db=db, borrow=borrow, std_id=std_id)

@app.get("/borrow/",response_model=list[schemas.Borrow])
def get_borrowings(skip:int=0, limit:int=100, db:Session=Depends(get_db)):
    borrowings = crud.get_borrowings(db, skip=skip, limit=limit)
    return borrowings

@app.get("/borrow/{borrowing_id}",response_model=schemas.Borrow)
def get_borrow(borrowing_id:int, db:Session = Depends(get_db)):
    db_borrow = crud.get_borrow(db, borrowing_id=borrowing_id)
    if db_borrow is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_borrow

    