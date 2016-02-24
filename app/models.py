from . import db 
from sqlalchemy.dialects.postgresql import JSON

    
class User(db.Model):
    
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), unique=True)
    password = db.Column(db.String(45), unique=True) 
    fname = db.Column(db.String(40),)
    lname = db.Column(db.String(40),)
    age = db.Column(db.Integer, )
    sex = db.Column(db.String(20),)
    
    def __init__(self, username,password, fname, lname, age, sex):
        self.username = username
        self.password=password
        self.fname = fname
        self.lname=lname
        self.age=age
        self.sex=sex 
        

    def __repr__(self):
          return '<userid{}>'.format(self.userid)