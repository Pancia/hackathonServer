import json

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

class Test(webapp.RequestHandler):

	def get(self):
		self.test()

	def post(self):
		self.test()

	def test(self):
		self.response.headers["Content-Type"] = "application/json"
			

		self.response.write(
			json.dumps(
				{"success":0, "response":"#TEST - Hello World!"}
			)
		)

def main():
	application = webapp.WSGIApplication([("/test.py", Test)], debug=True)
	util.run_wsgi_app(application)

if __name__ == "__main__":
	main()





