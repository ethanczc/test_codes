# file saved as PeopleClass.py

class Person():
	def __init__(self,name):
		self.name = name
	def SayName(self):
		print ('Hi, My name is ' + str(self.name))

import PeopleClass
# imports PeopleClass

ethan = PeopleClass.Person('ethan')
ethan.SayName()

from PeopleClass import Person
# imports Person class from PeopleClass

ethan = Person('ethan')
ethan.SayName()

from PeopleClass import *
# imports all classes in PeopleClass