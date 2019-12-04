from sys import argv

def add(a, b):
	return a+b

if __name__ == '__main__':
	# argv[0] == "input.py"
	a = float(argv[1])
	b = float(argv[2])

	print("The sum is: " + str(add(a, b)))

	# print formating using % and arguments should be inside a tuple
	print("Sum of %f and %f is: %f" % (a, b, add(a, b)))	
	