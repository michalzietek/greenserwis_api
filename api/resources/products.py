from datetime import datetime
from typing import List


from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from models import Product
from database import get_db

from schema import ProductViewModel, PostProductViewModel

router = APIRouter()





@router.get("/", response_model=List[ProductViewModel])
def list_products(product_id: int = None, db: Session = Depends(get_db)):
    product_query = db.query(Product)
    if product_id is not None:
        product_query = product_query.filter(Product.id == product_id)
    return product_query.all()



@router.post("/", response_model=PostProductViewModel)
def add_product(product: PostProductViewModel, db: Session = Depends(get_db)):
    article_query = Product(title = product.title, photo = product.photo, description = product.description, price = product.price)
    db.add(article_query)
    db.commit()

    return product


@router.put("/{product_id}", response_model=PostProductViewModel)
def update_product(product: PostProductViewModel, article_id: int, db: Session = Depends(get_db)):
    article_query = db.query(Product).filter(Product.id == article_id).first()
    if not article_query:
        raise HTTPException(400)
    article_query.title = product.title
    article_query.photo = product.photo
    article_query.description = product.description
    article_query.price = product.price
    db.commit()

    return product


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product_query = db.query(Product).filter(Product.id == product_id).first()
    if not product_query:
        raise HTTPException(400)
    db.delete(product_query)
    db.commit()

    return {
        '200': 'product deleted'
    }
