import mysql.connector as mys
cu=mys.connect(host="localhost",user="root",passwd="",database="registration")
myc=cu.cursor()
#myc.execute("create table registration1(username varchar(50),emailid varchar(50),password varchar(50))")
def regi():	
	a=raw_input("enter your username")
	b=raw_input("enter your emailid")
	c=raw_input("enter your password")
	usr="""insert into registration1(username,emailid,password) valuses(%s,%s,%s)"""%(a,b,c)
	myc.execute(usr)
	cu.commit()
	ab=int(input("press 1 for more registration and 2 for login"))
	if ab==1:
		regi()
	else:
		login()
def login():
	a=raw_input("enter your emailid")
	myc.execute("select * from registration1 where emailid = '%s' "%(a))
	cu.commit()
	cre=myc.fetchone()
	c=cre[1]
	if a==cre[1]:
		pa=input("enter your password")
		if pa==cre[2]:
			print ("welcome")
		else :
			print("wrong password")
	else:
		print("wrong emailid")
y=int(input("press 1 for registration and 2 for login"))
if y==1:
	regi()
elif y==2:
	login()
else:
	print("wrong choice")
	