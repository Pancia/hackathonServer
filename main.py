import webapp2
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello World!")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
