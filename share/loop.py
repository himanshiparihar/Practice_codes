from input import add

if __name__ == '__main__':
	lst = range(1, 50)

	# lst = [1,2,3,...,49]
	for num in lst:
		print("Square of ", num, " is: ", num**2)

	size = len(lst)
	i = 0

	while(i<size):
		if (lst[i] % 3 == 0):
			print("%d is divisible by 3." % lst[i])
		i = i+1

	