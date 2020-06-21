from datetime import datetime

import peewee as pw

from app import db


class Article(pw.Model):

    class Meta:
        database = db

    heading = pw.TextField()
    addition_date = pw.DateTimeField(default=datetime.now)
    photos = pw.TextField()
    text = pw.TextField()
