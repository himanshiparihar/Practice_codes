import mysql.connector as m
cu=m.connect(host="localhost",user="root",passwd="",database="cabbooking")
myc=cu.cursor()
# myc.execute("create table cabbook(id int PRIMARY KEY AUTO_INCREMENT,destination varchar(200),fare1 int)")
# myc.execute("create table nodays(days int primary key auto_increment,fare2 int)")
# myc.execute("create table nopeople(people int primary key auto_increment,fare3 int)")
# myc.execute("create table ac(location varchar(50),fare4 int)")
# myc.execute("create table nonac like ac")
sum3=0
sum1=0
sum2=0
def carbook():
	dest = [('indore',2000),('gwalior',2500),('jabalpur',1500),('vidisha',1700),('ujjain',2200)]
	sql = "insert into cabbook (destination,fare1) values (%s,%d)"
	myc.executemany(sql,dest)
	cu.commit()
	a=int(input("choose your destination:1 indore 2 gwalior 3 jabalpur 4 vidisha 5 ujjain"))
	myc.execute("select * from cabbook where destination='%s'"%(a))
	des=myc.fetchone()
	b=des[2]
	b1=des[1]
	global sum3
	sum3+=b
	print("fare for going to %s is : %d "%(b1,b))
def dys():
	dest=[(200),(400),(600),(900),(1500)]
	sql="insert into nodays(fare2) values (%s)"
	myc.executemany(sql,dest)
	cu.commit()
	c=int(input("enter no. of days:1. 1-2 days 2. 3-6 days 3. 7-10 days 4. 11-20 days 5. more than 20 days"))
	myc.execute("select * from nodays where days='%s' "%(c))
	dy=myc.fetchone()
	d=dy[1]
	global sum3
	sum3+=d
	print("fare for your booking days is: %d"%(d))
def ppl():
	myc.execute("insert into nopeople(fare3) values ((200),(500),(800)) ")
	e=int(input("enter no. of people: 1. 1-2 people 2. 3-5 people 3. 6-8 people "))
	myc.execute("select * from nopeople where days='%d'"%(e))
	pe=myc.fetchone()
	f=pe[1]
	global sum3
	sum3=sum3+f
	print("fare for people going on a journey is:%d"%(f))
def aac():
	myc.execute("insert into ac(location,fare4) values (('near station',1000),('near market',1500),('anywhere',800))")
	g=int(input("enter your staying location : near station , near market , anywhere"))
	myc.execute("select * from ac where location='%s' "%(g))
	ac1=myc.fetchone()
	h=ac1[1]
	global sum2
	sum2=h+sum3
	print("fare for ac room is:%d"%(h))
	print("total is %d"%(sum2))
def nona():
	myc.execute("insert into nonac(location,fare4)values (('near station',800),('near market',1000),('anywhere',600))")
	g=int(input("enter your staying location : near station , near market , anywhere"))
	myc.execute("select * from ac where location='%s' "%(g))
	nonac1=myc.fetchone()
	h=nonac1[1]
	global sum1
	sum1=sum3+h
	print("fare for non ac room is:%d"%(h))
	print("total is %d"%(sum1))
print("welcome to cabbooking system")
carbook()
dys()
ppl()
inp=int(input("press 1 for hotel booking and 2 for no hotel booking"))
if inp==1:
	inp1=int(input("press 1 for ac hotel and 2 for non ac hotel"))
	if inp1==1:
		aac()
	else:
		nona()
else:
	print("good day")


