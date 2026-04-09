from fastapi import FastAPI
from .database import engine
from .models import Base
from .routers import category, product

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(category.router)
app.include_router(product.router)