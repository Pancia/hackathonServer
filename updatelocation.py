import json

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

class UpdateLocation(webapp.RequestHandler):

	def get(self):
		self.updateLocation()

	def post(self):
		self.updateLocation()

	def updateLocation(self):
		self.response.headers["Content-Type"] = "application/json"
			

		self.response.write(
			json.dumps(
				{"success":0, "response":"#TEST - Hello World!"}
			)
		)

def main():
	application = webapp.WSGIApplication([("/updatelocation.py", UpdateLocation)], debug=True)
	util.run_wsgi_app(application)

if __name__ == "__main__":
	main()





