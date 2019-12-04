k1=[]
l1=[]
c=0
a=int(input())
for i in range(a):
	l=input()
	k=l.split(" ")
	if 'push' in l:
		k1.append(int(k[1]))
		#print(k1)
	elif 'pop' in l:
		k1.pop()
	elif 'max' in l:
		c=c+1
		l1.append(max(k1))
for i in range(c):
	print(l1[i])
