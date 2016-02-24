from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db_conn = 'postgresql+psycopg2://postgres:cartoon@localhost/WishList' 
app.config['SQLALCHEMY_DATABASE_URI'] = db_conn
db = SQLAlchemy(app)
from app import views, models
