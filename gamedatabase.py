from google.appengine.ext import db

class GameDatabase(db.Model):
	defender		= db.StringProperty()
	attacker		= db.StringProperty()
	defender_move	= db.StringProperty()
	attacker_move	= db.StringProperty()