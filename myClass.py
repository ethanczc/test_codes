
class Person():

	def __init__(self,name,age,say,**kwargs):
		'''
		double star for keyworded arguments
		'''
		self.name = name
		self.age = age
		self.say = say
		for key, value in kwargs.items():
			if key == 'height':
				self.height = value

	def call(self):
		print(str(self.name) + ' says ' + str(self.say))
		
	def sayHeight(self):
		try:
			print(str(self.name) +"'s height is " + str(self.height) )
		except:
			print("no height given")


class Hobo():
	def __init__(self):
		self.name = 'the hobo'

class Perform_Addition():
	def __init__(self,*args):
		'''
		single star for arguments
		'''
		total = 0
		for arg in args:
			total += arg
		self.result = total