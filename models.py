from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email
        
# User profile
class Profile(db.Model):
	profileid = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(50))
	password = db.Column(db.String(50))
	def __init__(self, username):
		self.username = username
		self.password = password
		self.profileid = profileid
	def __repr__(self):
		return '<Profile %r>' % (self.username) 
	
#Challenges
class Challenges(db.Model):
	challengeID = db.Column(db.Integer, primary_key = True)
	challengeName = db.Column(db.String(150))
	challengePoints = db.Column(db.Integer)
	#def __init__(self, challengeID, challengeName, challengePoints):
		#self.challengeID = challengeID
		#self.challengeName = challengeName
		#self.challengePoints = challengePoints
	def __repr__(self):
		return '<challengeID %r>' % (self.challengeID)

#Products
class Products(db.Model):
	productiD = db.Column(db.Integer, primary_key = True)
	productName = db.Column(db.String(150))
	def __init__(self, productiD):
		self.productiD=productiD
		self.productName = productName
	def __repr__(self):
		return '<Products %r>' % (self.productiD)



