def clean(string): #input : string output : string
	return string
def calculate(string): #input : str output : python number
	return 0
class Number:
	def __init__(self, numberstring):
		self.numberstring = clean(numberstring)
		
	def getExactValue(self):
		return calculate(self.numberstring)