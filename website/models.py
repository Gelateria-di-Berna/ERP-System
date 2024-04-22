from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.orm import backref

# Tabelle für die Zuordnung von Nutzern zu Standorten
users_locations = db.Table('users_locations',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('location_id', db.Integer, db.ForeignKey('location.id'), primary_key=True)
)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    name = db.Column(db.String(150))
    surname = db.Column(db.String(150))
    password = db.Column(db.String(150))
    #notes = db.relationship("Note")
    locations = db.relationship(
        "Location", 
        secondary=users_locations, 
        backref= "users"
        )

    def add_location(self, name, address):
        new_location = Location(name=name, address=address)
        self.locations.append(new_location)
        db.session.add(new_location)
        db.session.commit()
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
    
class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    address = db.Column(db.String(100), unique=True)
    #products = db.relationship("Product")

# class User2(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(150), unique=True)
#     password = db.Column(db.String(150))
#     name = db.Column(db.String(150))
#     surname = db.Column(db.String(150))
#     locations = db.relationship("Location")
#     role = db.Column(db.String(150))
#     active = db.Column(db.Boolean(True))