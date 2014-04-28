import json

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext import db

from userdatabase import UserDatabase

class AddUser(webapp.RequestHandler):

	def get(self):
		self.addUser()

	def post(self):
		self.addUser()

	def addUser(self):
		self.response.headers["Content-Type"] = "application/json"
		jayson = json.loads(self.request.body)
		username = jayson.get("username")
		password = jayson.get("password")
		email = jayson.get("email")
		college = jayson.get("college")
		if username != "" and password != "" and email != "" and college != "":
			q = db.GqlQuery("SELECT * FROM UserDatabase " + "WHERE username=:1", username)
			if (q.get() != None):
				self.response.write({"response": {"message":"user already exists!", "status":2} })
				return
			else:
				ud = UserDatabase(username=username, password=password, email=email, college=college)#set stats to 0
				ud.put()
				self.response.write({"response":{"message":"success", "status":0}})
		else:
			self.response.write({"response":{"message":"invalid parameters", "status":-2,
				"debug":{"username":username,"password":password,"email":email,"college":college}}})

def main():
	application = webapp.WSGIApplication([("/adduser.py", AddUser)], debug=True)
	util.run_wsgi_app(application)

if __name__ == "__main__":
	main()





