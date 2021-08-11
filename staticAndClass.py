class person(object):
	population = 50
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# Classmethod takes the actual class and can access anything within that class
	# Needs at least one parameter (as class name gets passed in automatically)
	@classmethod
	def getPopulation(cls):
		return cls.population

	# Only use parameters you pass
	# You don't need parameters
	@staticmethod
	def isAdult(age):
		return age >= 18

	def display(self):
		print(self.name, "is", self.age, "years old")


newPerson = person("tim", 18)
print(person.isAdult())
