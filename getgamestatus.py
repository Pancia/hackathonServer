import json

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext import db
import logging

from gamedatabase import GameDatabase

class GetGameStatus(webapp.RequestHandler):

	def get(self):
		self.getGameStatus()

	def post(self):
		self.getGameStatus()

	def getGameStatus(self):
		self.response.headers["Content-Type"] = "application/json"
		jayson = json.loads(self.request.body)
		username = jayson.get("username")
		gamemode = jayson.get("gamemode")

		if username != "" and gamemode != "":
			q_ingame = db.GqlQuery("SELECT * FROM GameDatabase " + "WHERE "+gamemode+"=:1", username)
			game = q_ingame.get()
			if (game == None):
				self.response.write({"response": "failed to find game"})
				return
			if game.defender_move == None and game.attacker_move != None:
				logging.info("Both game moves not submitted")
				self.response.write({"response": "try again"})#game moves not both submitted
				return
			if game.defender_move != None and game.attacker_move == None:
				logging.info("Both game moves not submitted")
				self.response.write({"response": "try again"})#game moves not both submitted
				return

			if game.should_reset == False or game.should_reset == None:
				game.should_reset = True
				game.put()
				if gamemode == "attacker":
					self.response.write({"gamemove":str(game.defender_move)})
				elif gamemode == "defender":
					self.response.write({"gamemove":str(game.attacker_move)})
			else:
				if gamemode == "attacker":
					self.response.write({"gamemove":str(game.defender_move)})
				elif gamemode == "defender":
					self.response.write({"gamemove":str(game.attacker_move)})
				db.delete(game)


	def isGameOver(self, game):
		if game.defender_move != game.attacker_move:
			return True
		else: 
			return False

def main():
	application = webapp.WSGIApplication([("/getgamestatus.py", GetGameStatus)], debug=True)
	util.run_wsgi_app(application)

if __name__ == "__main__":
	main()
