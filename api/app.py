from fastapi import FastAPI

from resources import articles, products

import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(articles.router, prefix="/articles")
app.include_router(products.router, prefix="/products")
