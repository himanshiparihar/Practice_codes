import random
def maxprod(l1):
    n=len(l1)
    maxi=0
    for p1 in range(n):
        for p2 in range(p1+1,n):
            maxi=max(maxi,l1[p1]*l1[p2])
    return maxi
l1=[]
input1=random.randrange(1000,10000)
for x in range(input1):
	a=random.randrange(1000,100000)
	l1.append(a)
print(l1)
print(maxprod(l1))