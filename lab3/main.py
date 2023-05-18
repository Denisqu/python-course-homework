from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import sqlalchemy

from model import db, Student
import utils
import query

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432'
db.init_app(app)
utils.test_for_db_connection(app, db)

# create db
with app.app_context():
    ins = sqlalchemy.inspect(db.engine)
    tables = ins.get_table_names()
    if not len(tables):
        db.create_all()


# populate db with test data
# TODO: проверять пустая ли бд, если да, то заполнять её тестовыми данными
with app.app_context():
    query.create_test_data()


