# for j in range(0,4):
# 	if j==0 or j==3:
# 		print('*****')
# 	if j==1 or j==2:
# 		print('*   *')
for i in range(4):
	for col in range(6):
		if i==0 or i==3 or col==0 or col==5:
			print("*",end="")
		else:
			print(" ",end="")
	print() 
