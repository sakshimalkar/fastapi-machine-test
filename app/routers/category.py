from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter(prefix="/api/categories", tags=["Categories"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# GET all categories
@router.get("/")
def get_categories(page: int = 1, db: Session = Depends(get_db)):
    limit = 10
    offset = (page - 1) * limit
    return db.query(models.Category).offset(offset).limit(limit).all()


# CREATE category
@router.post("/")
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    new_category = models.Category(name=category.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


# GET category by id
@router.get("/{id}")
def get_category(id: int, db: Session = Depends(get_db)):
    return db.query(models.Category).filter(models.Category.id == id).first()


# UPDATE category
@router.put("/{id}")
def update_category(id: int, category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = db.query(models.Category).filter(models.Category.id == id).first()
    db_category.name = category.name
    db.commit()
    db.refresh(db_category)
    return db_category


# DELETE category
@router.delete("/{id}")
def delete_category(id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()
    db.delete(category)
    db.commit()
    return {"message": "Category deleted"}