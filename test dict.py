import re
Dictionary1 = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}   
# Printing keys of dictionary 
l1=[]
l=Dictionary1.values()
l1.append(l)
print(l1)
a='353 46 jim'
print(a[0:5])
l2=[]
inp='vv 23 233 87'
for i in range(len(inp)):
	if inp[i].isdigit():
		cd=inp[i]
		l2.append(cd)
print(l2)
str = 'add 12456 and 232 !'
match = re.search(r'\d+\s*\w+\s*\d+', str)
# If-statement after sarch() tests if it succeeded
if match:
  print 'found', match.group() ## 'found word:cat'
else:
  print 'did not found'
k1=[]
k1=str.split(" ")
print (k1)
inp=input("enter instruction: ")
print (inp)