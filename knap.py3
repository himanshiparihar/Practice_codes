import numpy as np
def knap(x,a,y):
	az=[]
	ap=np.zeros((y+1,x+1))
	for km in range(0,y+1):
		for kn in range(0,x+1):
			if km==0 or kn==0:
				ap[km][kn]=0
			elif a[km]<=kn:
				ap[km][kn]=max(ap[km-1,kn],ap[km-1,kn-a[km]],a[km])
			else:
				ap[km][kn]=ap[km-1][kn]
	for km in range(0,y+1):
		for kn in range(0,x+1):
			if kn==x:
				az.append(ap[km][kn])
	return(max(az))
if __name__ == '__main__':
	a=[]
	x, y = [int(x) for x in input().split()]
	ni=input()
	a=ni.split(" ")
	a = [ int(xx) for xx in a ]
	a.insert(0,0)
	a.sort(reverse=True)
	print(knap(x,a,y))
