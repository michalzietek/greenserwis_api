from datetime import datetime
from typing import List


from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from models import Article
from database import get_db

from schema import ArticleViewModel, PostArticleViewModel

router = APIRouter()





@router.get("/", response_model=List[ArticleViewModel])
def list_articles(article_id: int = None, db: Session = Depends(get_db)):
    article_query = db.query(Article)
    if article_id is not None:
        article_query = article_query.filter(Article.id == article_id)
    return article_query.all()



@router.post("/", response_model=PostArticleViewModel)
def add_article(article: PostArticleViewModel, db: Session = Depends(get_db)):
    article_query = Article(title = article.title, photo = article.photo, text = article.text, addition_date = datetime.now())
    db.add(article_query)
    db.commit()

    return article


@router.put("/{article_id}", response_model=PostArticleViewModel)
def update_article(article: PostArticleViewModel, article_id: int, db: Session = Depends(get_db)):
    article_query = db.query(Article).filter(Article.id == article_id).first()
    if not article_query:
        raise HTTPException(400)
    article_query.title = article.title
    article_query.photo = article.photo
    article_query.text = article.text
    db.commit()

    return article


@router.delete("/{arcticle_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    article_query = db.query(Article).filter(Article.id == article_id).first()
    if not article_query:
        raise HTTPException(400)
    db.delete(article_query)
    db.commit()

    return {
        '200': 'article deleted'
    }
