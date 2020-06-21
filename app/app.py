from fastapi import FastAPI
import peewee as pw

from local_settings import DATABASE

db = pw.PostgresqlDatabase(
    database=DATABASE['name'],
    user=DATABASE['user'],
    password=DATABASE['password'],
    host=DATABASE['host'],
)

app = FastAPI()
