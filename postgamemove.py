import json

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext import db

from gamedatabase import GameDatabase

class PostGameMove(webapp.RequestHandler):

	def get(self):
		self.postGameMove()

	def post(self):
		self.postGameMove()

	def postGameMove(self):
		self.response.headers["Content-Type"] = "application/json"
		jayson = json.loads(self.request.body)
		username = jayson.get("username")
		move = jayson.get("move")
		gamemode = jayson.get("gamemode")
		if username != "" and move != "" and gamemode != "":
			#find game with username
			q_ingame = db.GqlQuery("SELECT * FROM GameDatabase " + "WHERE "+gamemode+"=:1", username)
			game = q_ingame.get()
			if (game == None):
				self.response.write({"response": "failed to find game"})
				return
			
			#if move already exists "ignore" it
			if gamemode == "attacker" and game.attacker_move == None:
				game.attacker_move = move
			elif gamemode == "defender" and game.defender_move == None:
				game.defender_move = move
			game.put()
			self.response.write({"response":"success"})

def main():
	application = webapp.WSGIApplication([("/postgamemove.py", PostGameMove)], debug=True)
	util.run_wsgi_app(application)

if __name__ == "__main__":
	main()
