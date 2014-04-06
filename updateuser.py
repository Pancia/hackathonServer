import json

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext import db

from userdatabase import UserDatabase

class UpdateUser(webapp.RequestHandler):

	def get(self):
		self.updateUser()

	def post(self):
		self.updateUser()

	def updateUser(self):
		self.response.headers["Content-Type"] = "application/json"
		username 	= self.request.get('username')
		#password 	= self.request.get('password')
		#email 		= self.request.get('email')
		#college 	= self.request.get('college')
		location 	= self.request.get('location')
		#wins		= self.request.get('wins')
		#losses		= self.request.get('losses')
		#points		= self.request.get('points')

		if username == '':
			self.response.write({'response': 'user name was null!'})
			return
		else:
			q = db.GqlQuery("SELECT * FROM UserDatabase " + "WHERE username=:1", username)
			if (q.get() == None):
				self.response.write({'response': 'user not found!'})
				return
			else:
				user = q.get()
				#if password != '':
				#	#blah
				#if email != '':
				#	#blah
				#if college != '':
				#	#blah
				if location != '':
					user.location = location
					user.put()
					self.response.write({'response':'success'})
				#if wins != '':
				#	#blah
				#if losses != '':
				#	#blah
				#if points != '':
				#	#blah


def main():
	application = webapp.WSGIApplication([("/updateuser.py", UpdateUser)], debug=True)
	util.run_wsgi_app(application)

if __name__ == "__main__":
	main()





