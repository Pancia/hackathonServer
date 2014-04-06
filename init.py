import json

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext import db

from userdatabase import UserDatabase
from gamedatabase import GameDatabase
from collegedatabase import CollegeDatabase

# class UserDatabase(db.Model):
# 	username	= db.StringProperty()
# 	password	= db.StringProperty()
# 	email		= db.StringProperty()
# 	college		= db.StringProperty()
# 	location	= db.StringProperty()
# 	stats		= db.StringProperty()

# class CollegeDatabase(db.Model):
# 	name 				= db.StringProperty()
# 	num_of_resources 	= db.StringProperty()
# 	defenders 			= db.StringListProperty()

class Init(webapp.RequestHandler):

	def get(self):
		self.init()

	def post(self):
		self.init()

	def init(self):
		self.response.headers["Content-Type"] = "text/plain"
		self.response.write("INITIALIZING")

		ud1 = UserDatabase(username="anthony", location="oakes")
		ud1.put()
		ud2 = UserDatabase(username="rachelle", location="oakes")
		ud2.put()
		ud3 = UserDatabase(username="jordan", location="oakes")
		ud3.put()
		ud4 = UserDatabase(username="cameron", location="oakes")
		ud4.put()

		self.initColleges()

	def initColleges(self):
		oakes = CollegeDatabase(name="oakes", num_of_resources="500", defenders=[])
		oakes.put()
		eight = CollegeDatabase(name="eight", num_of_resources="500", defenders=[])
		eight.put()

def main():
	application = webapp.WSGIApplication([("/init.py", Init)], debug=True)
	util.run_wsgi_app(application)

if __name__ == "__main__":
	main()





