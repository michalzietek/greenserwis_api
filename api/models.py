from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from database import Base


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100), default=False, nullable=False)
    addition_date = Column(DateTime ,default=datetime.now)
    photo = Column(Integer, default=False, nullable=False)
    text = Column(String(length=300), default=False, nullable=True)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100), default=False, nullable=False)
    photo = Column(Integer, default=False, nullable=False)
    description = Column(String, default=False, nullable=True)
    price = Column(Float, default=False, nullable=True)
