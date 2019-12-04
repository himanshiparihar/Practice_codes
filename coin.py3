# import sys

# def get_change(m):
# 	c=int(m/10)
# 	m=m%10
# 	b=int(m/5)
# 	m=m%5
# 	m=int(m/1)
# 	m=m+c+b
# 	return int(m)

# if __name__ == '__main__':
# 	m = int(input())
# 	print(get_change(m))
d1={}
l1={}
k=0
x, y = [int(x) for x in input().split()] 
while x != 0:
	a,b = [int(xa) for xa in input().split()] 
	d1[a]=b
	x -=1	
for km in d1.keys():
	l1[km]=k/d1[km]
kf=max(l1.values())
lok = [key  for (key, value) in l1.items() if value == kf]
cd1=lok[0]
if d1[cd1]>=y: 
	cd1=(cd1/d1[cd1])*y
	k=k+cd1
	print (k)
else:
	y=y-d1[cd1]
	k=k+cd1
	del d1[cd1]
	print (k)
