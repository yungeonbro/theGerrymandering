import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from gamelogic import *
import time


def lisenter(event):
	print(event.data)

class ServerManager:
	def __init__(self, certificatepath, databaseURL):
		self.certificatepath = certificatepath
		self.databaseURL = databaseURL

		self.cred = credentials.Certificate(certificatepath)
		firebase_admin.initialize_app(self.cred, {
			'databaseURL' : databaseURL
			})

		firebase_admin.db.reference('gerrymandering-296813/games').listen(lisenter)



	def cls(self): # doesent work
		self.directory = db.reference()
		self.directory.update({'games':[]})

	def addGame(self, pwd):
		self.directory = db.reference()
		data = self.directory.get()
		data['games'].append({'password':pwd, 'started':False, 'ended':False})
		self.directory.update(data)

	def isWaitingGame(self, pwd):
		self.directory = db.reference()
		data = self.directory.get()
		for game in data['games']:
			if game['password'] == pwd:
				print("asdf")
				game['started'] = True
				self.directory.update(data)
				return True
		return False

	def hasGameStarted(self, pwd):
		self.directory = db.reference()
		data = self.directory.get()
		for game in data['games']:
			if game['password'] == pwd:
				return game['started']

	def getSizeOfGame(self):
		return 6

	def addGameInfo(self, pwd):
		self.directory = db.reference()
		data = self.directory.get()
		for game in data['games']:
			if game['password'] == pwd:
				game['gameinfo']={'turn':0, 'demPoint':0, 'repPoint':0}
		self.directory.update(data)

	def upLoadGame(self, pwd, rgame):
		self.directory = db.reference()
		data = self.directory.get()
		for game in data['games']:
			if game['password'] == pwd:
				print(game)
				game['gameinfo']['turn'] = rgame.turn
				game['gameinfo']['demPoint'] = rgame.demPoint
				game['gameinfo']['repPoint'] = rgame.repPoint
				game['gameinfo']['board'] = rgame.board
		self.directory.update(data)

	def downLoadGame(self, pwd):
		time.sleep(4)
		self.directory = db.reference()
		data = self.directory.get()
		for game in data['games']:
			if game['password'] == pwd:
				retgame = Game(6)
				retgame.turn = game['gameinfo']['turn']
				retgame.demPoint = game['gameinfo']['demPoint']
				retgame.repPoint = game['gameinfo']['repPoint']
				retgame.board = game['gameinfo']['board']
				return retgame

if __name__  == "__main__":
	manager = ServerManager('key2.json',  'https://gerrymandering-296813.firebaseio.com/')
	print(manager.isWaitingGame('saaaa'))