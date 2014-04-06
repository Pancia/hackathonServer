import json

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext import db

from collegedatabase import CollegeDatabase

class UpdateCollegeInfo(webapp.RequestHandler):

	def get(self):
		self.updateCollegeInfo()

	def post(self):
		self.updateCollegeInfo()

	def updateCollegeInfo(self):
		self.response.headers["Content-Type"] = "application/json"
		college = self.request.get("college")
		resources = self.request.get("resources")
		username = self.request.get("username")
		if college != "":
			q = db.GqlQuery("SELECT * FROM CollegeDatabase " + "WHERE name=:1", college)
			college = q.get()
			if college == None:
				self.response.write({"response":"college not found"})
				return
			else:
				if resources != "":
					college.num_of_resources = resources
					college.put()
				if username != "":
					college.defenders.remove(username)
					college.put()
				self.response.write({"response":"success"})

def main():
	application = webapp.WSGIApplication([("/updatecollegeinfo.py", UpdateCollegeInfo)], debug=True)
	util.run_wsgi_app(application)

if __name__ == "__main__":
	main()





