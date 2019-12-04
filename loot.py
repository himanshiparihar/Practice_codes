# Uses python3
import sys
def get_optimal_value():
	l1={}
	sum1=0
	f=0
	global y
	global d1
	global k
	for km in d1.keys():
		l1[km]=float(k)/float(d1[km]) # to set a link betw ratio of value-column and values
	#print("l1",l1)
	kf=max(l1.values())	
	lok = [key  for (key, value) in l1.items() if value == kf]
	cd1=lok[0]	# key of maximum ratio quantity
	#print("cd1",cd1)
	for su in d1.values():
		sum1=sum1+su
	#print("sum1",sum1)
	if sum1>y: # to check if total wt of different items is greater than than the sack weight
		while y != 0: # we will fill sack till it wont get full
			if d1[cd1]>=y : # checking if the maxim ratio qt can fill the sack completely
				cd1=float(cd1/d1[cd1])*y # finding the value the sack will have after filling the item
				#print(cd1)
				k=float(k)+float(cd1)
				print(k)
				y=0
			else:
				y=y-d1[cd1] #subtracting the weight which have been fill into the sack
				k=k+cd1
				del d1[cd1]
				#print("k",k)
				#print("y",y)
				#print("d1",d1)
					#deleting those item which have been filled into the stack
				get_optimal_value()
	else: # if the wt of sack is bigger then the values of all the item will be added
		for hm in d1.keys():
			f=f+hm
		k=k+f
		print (k)
k=0
d1={}
x, y = [int(x) for x in input().split()] # entr no of items and the wt of sack
while x != 0:
	a,b = [int(xa) for xa in input().split()] 
	d1[a]=b #creating dictionary of values and wt of item
	x -=1	
get_optimal_value()
