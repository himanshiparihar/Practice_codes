def euc(a,b):
	while (a != b):
		if(a>b):
			a=a-b
		else:
			b=b-a
	return a
x, y = [int(x) for x in input().split()] 
print(euc(x,y))