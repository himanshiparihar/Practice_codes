# def gcd(a,b): 
# 	if a == 0 : 
# 		return b  
      
# 	return gcd(b%a, a)
# def lcm (a,b):
# 	return int((a*b)/gcd(a,b))
# x, y = [int(x) for x in input().split()] 
# print(lcm(x,y))
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
		elif(int(stops[lm+1])-int(stops[lm]))>m:
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