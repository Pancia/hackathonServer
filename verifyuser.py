import json

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext import db

import json

from userdatabase import UserDatabase

class VerifyUser(webapp.RequestHandler):

	def get(self):
		self.verifyUser()

	def post(self):
		self.verifyUser()

	def verifyUser(self):
		self.response.headers["Content-Type"] = "application/json"
		jayson = json.loads(self.request.body)
		username = jayson.get("username")
		password = jayson.get("password")
		if username != "" and password != "":
			q = db.GqlQuery("SELECT * FROM UserDatabase " + "WHERE username=:1", username)
			user = q.get()
			if user == None:
				self.response.write({"response": {"message":"no such user", "status":-1}})
				return
			elif user.password == password:
				self.response.write({"response":{"message":"success", "college":str(user.college), "status":0}})
			else:
				self.response.write({"response":{"message":"failed", "status":2}})
		else:
			self.response.write({"response":{"message":"invalid parameters", "status":-2,
				"debug":{"username":username, "password":password}}})

def main():
	application = webapp.WSGIApplication([("/verifyuser.py", VerifyUser)], debug=True)
	util.run_wsgi_app(application)

if __name__ == "__main__":
	main()

