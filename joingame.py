import json
import random

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext import db

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
		if self.request.get("username") != "" and self.request.get("gamemode") != "":
			username = self.request.get("username")
			gamemode = self.request.get("gamemode")

			q_loc = db.GqlQuery("SELECT * FROM UserDatabase " + "WHERE username=:1", username)
			if (q_loc.get() == None):
				self.response.write({"response": "UserDatabase was null!"})
				return
			location = q_loc.get().location

			q_coll = db.GqlQuery("SELECT * FROM CollegeDatabase " + "WHERE name=:1", location)
			college = q_coll.get()

			if gamemode == "attacker":
				if len(college.defenders) > 0:
					defender_index = random.randint(0, len(college.defenders)-1)
					opponent = college.defenders[defender_index]
					#make a game ONLY if game doesnt already exist with that username
					q_ingame = db.GqlQuery("SELECT * FROM GameDatabase " + "WHERE attacker=:1", username)
					game = q_ingame.get()
					if (game == None):
						game = GameDatabase(defender=opponent, attacker=username)
						game.put()
						self.response.write({"p2_username":str(opponent)})
					else:
						self.response.write({"response": "game already exists"})
						return
				else:
					self.response.write({"p2_username": "pve"})

			elif gamemode == "defender":
				if username in college.defenders:
					q_ingame = db.GqlQuery("SELECT * FROM GameDatabase " + "WHERE defender=:1", username)
					game = q_ingame.get()
					if (game == None):
						self.response.write({"response": "try again"})
						return

					if username == game.defender:
						college.defenders.remove(username)
						college.put()
						self.response.write({"p2_username":str(game.attacker)})
					else:
						self.response.write({"response": "try again"})
				else:
					college.defenders.append(username)
					college.put()
					self.response.write({"response":"added to game"})

def main():
	application = webapp.WSGIApplication([("/joingame.py", JoinGame)], debug=True)
	util.run_wsgi_app(application)

if __name__ == "__main__":
	main()
