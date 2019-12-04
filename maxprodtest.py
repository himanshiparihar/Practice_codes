import random
def maxprod(l1):
    maxi=l1[0]*l1[1]
    return maxi
l1=[]
input1=random.randrange(1000,100000)
for x in range(input1):
	a=random.randrange(1000,10000)
	l1.append(a)
l1.sort()
print(l1)
print(maxprod(l1))