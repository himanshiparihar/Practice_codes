def bracket(a):
	open1=['[','(','{']
	close=[']',')','}']
	stack=[]
	stack3=[]
	ak=[]
	for i in range(len(a)):
		# print('i',i)
		# print('a[i]',a[i])
		if  a[i] in open1:
			stack.append(a[i])
			ak.append(i)
			stack3.append(a[i])
			# print('stack3',stack3)
			# print('stack:',stack)
		elif a[i] in close:
			pos=close.index(a[i])
			stack3.append(a[i])
			#print('index',pos)
			if ((len(stack) > 0) and open1[pos]==stack[len(stack)-1]):
				stack.pop()
				ak.pop()
				#print('stack1',stack) 
			else:
				# print('a',a)
				# print('index1',i+1)
				return (i+1)
	if len(stack)==0:
		#print('s1')
		return('Success')
	else:
		#print('ak',ak[0]+1)
		return (ak[0]+1)

n=input("")
print(bracket(n))
