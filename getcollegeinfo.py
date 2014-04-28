import json

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext import db

from collegedatabase import CollegeDatabase

class GetCollegeInfo(webapp.RequestHandler):

	def get(self):
		self.getCollegeInfo()

	def post(self):
		self.getCollegeInfo()

	def getCollegeInfo(self):
		self.response.headers["Content-Type"] = "application/json"
		jayson = json.loads(self.request.body)
		college = jayson.get("college")

		if college != "":
			q = db.GqlQuery("SELECT * FROM CollegeDatabase " + "WHERE name=:1", college)
			college = q.get()
			if college == None:
				self.response.write({"response": {"message":"failed to find college", "status":-1}})
			else:
				self.response.write({"response": {"status":0,"defender_count":len(college.defenders), 
												"resources":str(college.num_of_resources)}})
		else:
			self.response.write({"response":{"message":"invalid parameters", "status":-2, 
				"debug":{"college"+college}}})

def main():
	application = webapp.WSGIApplication([("/getcollegeinfo.py", GetCollegeInfo)], debug=True)
	util.run_wsgi_app(application)

if __name__ == "__main__":
	main()





