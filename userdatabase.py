from google.appengine.ext import db

class UserDatabase(db.Model):
	username	= db.StringProperty()
	password	= db.StringProperty()
	email		= db.StringProperty()
	college		= db.StringProperty()
	location	= db.StringProperty()
	stats		= db.StringProperty()#change to have wins, losses, points as Integers