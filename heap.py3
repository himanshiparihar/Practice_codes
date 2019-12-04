def heap(a,n,c):
	k=0
	k=n
	print('k',k)
	while n>1:
		ac=int(n/2)
		#print('ac',ac)
		if a[ac-1]>a[n-1]:
			a[ac],a[n-1]=a[n-1],a[ac]
			c+=1
			print(ac-1,n-1)
			n=int(n/2)
			print('while n',n)
	n=k-1
	print('n',n)
	while n>1:
		print(n,'n')
		heap(a,n,c)
	print('c',c)
if __name__ == '__main__':
	n=int(input())
	a = list(map(int,input(" ").strip().split()))[:n]
	print('a',a)
	n=len(a)
	print('n',n)
	heap(a,n,c=0)