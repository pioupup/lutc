
class Person:
	def __init__(self, name, age, pay=0, job=None):
		self.name = name
		self.age = age
		self.pay = pay
		self.job = job
	def __str__(self):
		dict_str = self.__class__.__name__ + ":"
		for key in self.__dict__:
			dict_str += " " + str(key) + "=>" + str(self.__dict__[key]) + ";"
		return dict_str
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self, percent):
		self.pay *= (1.0 + percent)

if __name__ == '__main__':
	bob = Person('Bob Smith', 42, 30000, 'software')
	sue = Person('Sue Jones', 45, 40000, 'hardware')
	print(bob.name, sue.pay)

	print(bob.lastName())
	sue.giveRaise(.10)
	print(sue.pay)

	print(sue)