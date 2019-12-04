import sys
def calc_fib(n):
	l1=[]
	l1.append(0)
	l1.append(1)
	if n <= 1:
		return n
	for i in range(2,n+1):
		b=(l1[i-1]+l1[i-2])%10
		l1.append(b)
	return l1[i]
n = int(input())
print(calc_fib(n))
