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
				self.response.write({"response": "user already exists!"})
				return
			else:
				ud = UserDatabase(username=username, password=password, email=email, college=college)#set stats to 0
				ud.put()
				self.response.write({"response":"success"})
		else:
			self.response.write({"response":"invalid parameters", 
				"debug":str("username:"+username+"password:"+password+"email:"+email+"college:"+college)})

def main():
	application = webapp.WSGIApplication([("/adduser.py", AddUser)], debug=True)
	util.run_wsgi_app(application)

if __name__ == "__main__":
	main()





