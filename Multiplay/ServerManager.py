import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class ServerManager:
	def __init__(self, certificatepath, databaseURL):
		self.certificatepath = certificatepath
		self.databaseURL = databaseURL

		self.cred = credentials.Certificate(certificatepath)
		firebase_admin.initialize_app(self.cred, {
			'databaseURL' : databaseURL
			})





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
		return False
if __name__  == "__main__":
	manager = ServerManager('key2.json',  'https://gerrymandering-296813.firebaseio.com/')
	print(manager.isWaitingGame('saaaa'))