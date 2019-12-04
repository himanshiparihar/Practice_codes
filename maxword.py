f = open('sample.txt', 'U')
myNames = [line.strip() for line in f]
counter=0
c=[]
for i in myNames:
	k=i.split(" ")
	c+=k
     print(max(set(c), key = c.count) )

	#max(stats.iteritems(), key=operator.itemgetter(1))[0]


	