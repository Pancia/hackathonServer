from google.appengine.ext import db

class CollegeDatabase(db.Model):
	name 				= db.StringProperty()
	num_of_resources 	= db.StringProperty()
	defenders 			= db.StringListProperty()