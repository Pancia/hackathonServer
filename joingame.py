import json
import random

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext import db
import logging

from userdatabase import UserDatabase
from gamedatabase import GameDatabase
from collegedatabase import CollegeDatabase

class JoinGame(webapp.RequestHandler):

	def get(self):
		self.joinGame()

	def post(self):
		self.joinGame()

	def joinGame(self):
		self.response.headers["Content-Type"] = "application/json"
		jayson = json.loads(self.request.body)
		username = jayson.get("username")
		gamemode = jayson.get("gamemode")
		if username != "" and gamemode != "":
			q_loc = db.GqlQuery("SELECT * FROM UserDatabase " + "WHERE username=:1", username)
			if (q_loc.get() == None):
				self.response.write({"response": {"message":"UserDatabase was null!", "status":-1}})
				return
			location = q_loc.get().location

			q_coll = db.GqlQuery("SELECT * FROM CollegeDatabase " + "WHERE name=:1", location)
			college = q_coll.get()

			if gamemode == "attacker":
				if len(college.defenders) > 0:
					defender_index = random.randint(0, len(college.defenders)-1)
					opponent = college.defenders[defender_index]
					q_ingame = db.GqlQuery("SELECT * FROM GameDatabase " + "WHERE attacker=:1", username)
					game = q_ingame.get()
					if (game == None):
						game = GameDatabase(defender=opponent, attacker=username)
						game.put()
						self.response.write({"response":{"p2_username":str(opponent), "status":0}})
					else:
						self.response.write({"response": {"message":"game already exists", "status":2}})
						return
				else:
					self.response.write({"response":{"p2_username": "pve", "status":0}})

			elif gamemode == "defender":
				if username in college.defenders:
					q_ingame = db.GqlQuery("SELECT * FROM GameDatabase " + "WHERE defender=:1", username)
					game = q_ingame.get()
					if (game == None):
						logging.warning("game with user("+str(username)+")not found")
						self.response.write({"response": {"message":"try again", "status":1}})
						return

					if username == game.defender:
						college.defenders.remove(username)
						college.put()
						self.response.write({"response":{"p2_username":str(game.attacker), "status":0}})
					else:
						self.response.write({"response": {"message":"try again", "status":1}})
				else:
					college.defenders.append(username)
					college.put()
					self.response.write({"response": {"message":"added to game", "status":1}})
		else:
			self.response.write({"response":{"message":"invalid parameters", "status":-2, 
				"debug":{"username":username, "gamemode":gamemode}}})

def main():
	application = webapp.WSGIApplication([("/joingame.py", JoinGame)], debug=True)
	util.run_wsgi_app(application)

if __name__ == "__main__":
	main()
