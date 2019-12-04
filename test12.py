
l1=[]
l2=[]
l3=[]
l4=[]
for i in range (1,251):
	l4.append(4*i)
	l3.append(4*i-1)
	l2.append(4*i-2)
	l1.append(4*i-3)
print(l1)
print(l2)
print(l3)
print(l4)
a=int(input("enter a no."))
j=1
# if a%4==0:
# 	print ("the no. belong to list 4")
# elif a%2==0 and a%4 != 0:
# 	print("the no. belong to list 2")
# else:
# 	while j<=250:
# 		if a==4*j-1:
# 			print("the no. belong to list 3")
# 		elif a==4*j-3:
# 			print ("the no. belong to list 1")
# 		else:
# 			j+=1
if a in l1:
	print ("no is in list1")
elif a in l2:
	print("no. is in list2")
elif a in l3:
	print("no. is in list3")
elif a in l4:
	print("no. is in list4")
else:
	print("")
