# https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy
# https://github.com/adyouri/large-flask-app-template/tree/main
from flask import Flask
import sqlalchemy
from model import db, Group
import utils
import query

app = Flask(__name__, template_folder='../lab4/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432'
app.config['SECRET_KEY'] = '84bdd533c5499fd913e7eb26498766e21f15406ea11d7ea1'
db.init_app(app)
import routes
utils.test_for_db_connection(app, db)

# create db
with app.app_context():
    ins = sqlalchemy.inspect(db.engine)
    tables = ins.get_table_names()
    if not len(tables):
        db.create_all()

# populate db with test data
with app.app_context():
    if db.session.query(Group).first() is None:
        query.create_test_data()

