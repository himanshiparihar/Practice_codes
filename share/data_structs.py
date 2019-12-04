class Info(object):
	def __init__(self, name="", age=0):
		self.name = name
		self.age = age

	def addAddress(self, house=""):
		self.address = house

	def showDetails(self):
		print(self.name, self.age, self.address)


if __name__ == '__main__':
	# # list
	# lst = [13, -2, 3]
	# lst.append(10)
	# print(lst, lst[2])

	# # tuple -> Immutable
	# tup = (2, 13, -4)
	# print(tup, tup[1])

	# # dicts [key -> value]
	# dic = {1 : "cat", 2 : "Dog", 3 : "Human"}
	# print(dic)
	# print(dic[3])

	# class
	person1 = Info("udit", 22)
	person1.addAddress("IIIT")
	person1.showDetails() 

	# # sorting
	# print("List:", lst)
	# print("Sorted list:", sorted(lst))