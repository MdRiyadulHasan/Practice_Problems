from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
app.app_context().push()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    date_joined = db.Column(db.Date, default=datetime.utcnow)

    def __repr__(self):
        return f'<User: {self.email}>'

from app import app
from app import db, User
db.create_all()
User.query.all()
user = User(name = "Hasan", email  = "hasn@gmail.com")
user = User(name = "Tanvir", email = "ziha@gmail.com")
db.session.add(user)
db.session.commit()
User.query.all()
user = User.query.filter_by(name = "Riyad").first()
db.session.delete(user)


