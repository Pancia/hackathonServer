import json

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

class GetGameStatus(webapp.RequestHandler):

	def get(self):
		self.getGameStatus()

	def post(self):
		self.getGameStatus()

	def getGameStatus(self):
		self.response.headers["Content-Type"] = "application/json"
		username = self.request.get('username')
		gamemode = self.request.get('gamemode')

		if username != '' and gamemode != '':
			q_ingame = db.GqlQuery("SELECT * FROM GameDatabase " + "WHERE "+gamemode+"=:1", username)
			game = q_ingame.get()
			if (game == None):
				self.response.write({'response': 'failed to find game'})
				return
			

def main():
	application = webapp.WSGIApplication([("/getgamestatus.py", GetGameStatus)], debug=True)
	util.run_wsgi_app(application)

if __name__ == "__main__":
	main()
