import sys
def compute_min_refills(d, m, stops):
	c=0
	ctr=0
	ctr1=0
	for lm in range(len(stops)-1):
		if (int(stops[lm])-c)>m:
			c=int(stops[lm-1])
			ctr1 += 1
		elif(m-(int(stops[lm])-c))<(int(stops[lm+1])-int(stops[lm])):
			c=int(stops[lm])
			ctr +=1
		elif int(stops[lm+1])-int(stops[lm]):
			return -1
	return (ctr+ctr1)
if __name__ == '__main__':
	stops=[]
	d=int(input())
	m=int(input())
	n=int(input())
	i1=input()
	stops=i1.split(" ")
	stops.append(d)
	print(compute_min_refills(d, m, stops))