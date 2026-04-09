from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter(prefix="/api/products", tags=["Products"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# GET all products with pagination
@router.get("/")
def get_products(page: int = 1, db: Session = Depends(get_db)):
    limit = 10
    offset = (page - 1) * limit
    return db.query(models.Product).offset(offset).limit(limit).all()


# CREATE product
@router.post("/")
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    new_product = models.Product(
        name=product.name,
        price=product.price,
        category_id=product.category_id
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


# GET product by id
@router.get("/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
    return db.query(models.Product).filter(models.Product.id == id).first()


# UPDATE product
@router.put("/{id}")
def update_product(id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == id).first()
    db_product.name = product.name
    db_product.price = product.price
    db_product.category_id = product.category_id
    db.commit()
    db.refresh(db_product)
    return db_product


# DELETE product
@router.delete("/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    db.delete(product)
    db.commit()
    return {"message": "Product deleted"}