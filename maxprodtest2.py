def calc_fib(n):
	l1=[]
	l1[1]=1
	l1[0]=0
    if n <= 1:
    	return n
    for i in range(2,n):
    	l1[i]=l1[i-1]+l1[i-2]
    return l1[i]
n = int(input("enter the no. of terms: "))
print(calc_fib(n))