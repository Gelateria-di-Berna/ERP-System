from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship("Note")

# #GdB
# class Article(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     products = db.relationship("Product")
#     unit = db.Column(db.String(100))
    
# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     article_id = db.Column(db.Integer, db.ForeignKey("article.id"))
#     charge_id = db.Column(db.Integer, db.ForeignKey("charge.id"))
#     location_id = db.Column(db.Integer, db.ForeignKey("location.id"))
    
# class Charge(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     article_id = db.Column(db.Integer, db.ForeignKey("article.id"))
#     products = db.relationship("Product")
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
    
# class Location(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     address = db.Column(db.String(100))
#     products = db.relationship("Product")
#     users = db.relationship("User2")
    
# class User2(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(150), unique=True)
#     password = db.Column(db.String(150))
#     name = db.Column(db.String(150))
#     surname = db.Column(db.String(150))
#     locations = db.relationship("Location")
#     role = db.Column(db.String(150))
#     active = db.Column(db.Boolean(True))