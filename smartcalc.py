import pyttsx3 
import re
# initialisation 
engine = pyttsx3.init() 
l1=[['add','addition','summation','sum'], ['subtract','subtration','difference','minus'] ,['multiply','multiplication','into'] ,['division','by','divide'] ,['mod','modulus','remainder']]
l2=[]
l3=[]
def calc():	
	global l3
	l2=[]
	l3=[]
	counter=0
	inp=raw_input("enter instruction: ")
	l2=inp.split(" ")
	for digi in l2:
		if digi.isdigit():
			l3.append(digi)
			counter+=1
			if counter>=3:
				print("i cant take more thn 2 values")
				engine.say("i cant take more thn 2 values")
				engine.runAndWait()
	for i in range(len(l1)):
		for j in range(len(l1[i])):
			c=l1[i][j]
			match=re.search(c,inp)
			if match:
				return i
def calc1(cal):
	try:#global cal
		if cal==0:
			sum1=int(l3[0],10)+int(l3[1],10)
			print(sum1)
			engine.say(sum1)  
			engine.runAndWait()
		elif cal==1:
			sum1=int(l3[1],10)-int(l3[0],10)
			print(sum1)
			engine.say(sum1)  
			engine.runAndWait()
		elif cal==2:
			sum1=int(l3[0],10)*int(l3[1],10)
			print(sum1)
			engine.say(sum1)  
			engine.runAndWait()
		elif cal==3:
			sum1=int(l3[0],10)/int(l3[1],10)
			print(sum1)
			engine.say(sum1)  
			engine.runAndWait()
		elif cal==4:
			sum1=int(l3[0],10)%int(l3[1],10)
			print(sum1)
			engine.say(sum1)  
			engine.runAndWait()
	except IndexError:
		print("index out of range")
		
kr="Y"
while kr=='Y':
	try:
		cal=calc()
	except UnboundLocalError as u:
		print(u,"an error is occured")
	calc1(cal)
	cr=raw_input("do you want to calculate again:y/n")
	kr=cr.upper()

else:
	print("good day")
#vicky05soni@gmail.com
# min(range) for min value
# max (range) for max value
#histogram tell frequency
#bins is gap
#left and right skewed
#mean median(statistic) for temp
#what should i do next(reinforcement)