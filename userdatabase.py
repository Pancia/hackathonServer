from google.appengine.ext import db

class UserDatabase(db.Model):
	username	= db.StringProperty()
	password	= db.StringProperty()
	email		= db.StringProperty()
	college		= db.StringProperty()
	location	= db.StringProperty()
	wins		= db.IntegerProperty()
	losses		= db.IntegerProperty()
	points		= db.IntegerProperty()
	#change to have wins, losses, points as Integers