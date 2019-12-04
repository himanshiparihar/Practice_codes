from tkinter import *
root = Tk()
root.title("Calculator")
root.geometry('480x600')
root.resizable(width=False,height=False)
root.configure(bg="purple")

inputdata = StringVar()
expression = ""

def getValue(va):
  global expression
  expression = expression+str(va)
  inputdata.set(expression)


def clear():
  global expression
  expression = ""
  inputdata.set(expression)

def calculation():
  global expression
  total = str(eval(expression))
  inputdata.set(total)
  expression = ""

def ch():
  l1.config(text="CALCULATOR",fg="black")


b1 = Button(text="C",command=clear,bg="red",fg="black",font=("Wide Latin",23,"bold"),activebackground="orange",activeforeground="blue",bd="3")
b1.grid(row="2",column="0",ipadx="14",ipady="14",sticky=N+E+W+S)
Button(text="/",command=lambda:getValue("/"),bg="blue",fg="black",font=("Wide Latin",23,"bold"),activebackground="orange",activeforeground="blue",bd="3").grid(row="2",column="1",ipadx="14",ipady="14",sticky=N+E+W+S)
Button(text="*",bg="blue",command=lambda:getValue("*"),fg="black",font=("Wide Latin",23,"bold"),activebackground="orange",activeforeground="blue",bd="3").grid(row="2",column="2",ipadx="14",ipady="14",sticky=N+E+W+S)
Button(text="-",bg="blue",command=lambda:getValue("-"),fg="black",font=("Wide Latin",23,"bold"),activebackground="orange",activeforeground="blue",bd="3").grid(row="2",column="3",ipadx="14",ipady="14",sticky=N+E+W+S)

Button(text="7",bg="#33E5FF",command=lambda:getValue(7),fg="black",font=("Wide Latin",23,"bold"),activebackground="orange",activeforeground="blue",bd="3").grid(row="3",column="0",ipadx="10",ipady="14",sticky=N+E+W+S)
Button(text="8",bg="#33E5FF",fg="black",command=lambda:getValue(8),font=("Wide Latin",23,"bold"),activebackground="orange",activeforeground="blue",bd="3").grid(row="3",column="1",ipadx="10",ipady="14",sticky=N+E+W+S)
Button(text="9",bg="#33E5FF",fg="black",command=lambda:getValue(9),font=("Wide Latin",23,"bold"),activebackground="orange",activeforeground="blue",bd="3").grid(row="3",column="2",ipadx="10",ipady="14",sticky=N+E+W+S)
Button(text="+",bg="blue",fg="black",font=("Wide Latin",23,"bold"),command=lambda:getValue("+"),activebackground="orange",activeforeground="blue",bd="3").grid(row="3",column="3",rowspan="2",ipadx="10",ipady="14",sticky=N+E+W+S)

Button(text="4",bg="#33E5FF",fg="black",font=("Wide Latin",23,"bold"),activebackground="orange",command=lambda:getValue(4),activeforeground="blue",bd="3").grid(row="4",column="0",ipadx="14",ipady="14",sticky=N+E+W+S)
Button(text="5",command=lambda:getValue(5),bg="#33E5FF",fg="black",font=("Wide Latin",23,"bold"),activebackground="orange",activeforeground="blue",bd="3").grid(row="4",column="1",ipadx="14",ipady="14",sticky=N+E+W+S)
Button(text="6",bg="#33E5FF",fg="black",command=lambda:getValue(6),font=("Wide Latin",23,"bold"),activebackground="orange",activeforeground="blue",bd="3").grid(row="4",column="2",ipadx="14",ipady="14",sticky=N+E+W+S)

Button(text="1",command=lambda:getValue(1),bg="#33E5FF",fg="black",font=("Wide Latin",23,"bold"),activebackground="orange",activeforeground="blue",bd="3").grid(row="5",column="0",ipadx="14",ipady="14",sticky=N+E+W+S)
Button(text="2",bg="#33E5FF",fg="black",command=lambda:getValue(2),font=("Wide Latin",23,"bold"),activebackground="orange",activeforeground="blue",bd="3").grid(row="5",column="1",ipadx="14",ipady="14",sticky=N+E+W+S)
Button(text="3",bg="#33E5FF",fg="black",command=lambda:getValue(3),font=("Wide Latin",23,"bold"),activebackground="orange",activeforeground="blue",bd="3").grid(row="5",column="2",ipadx="14",ipady="14",sticky=N+E+W+S)
Button(text="=",bg="blue",command=calculation,fg="black",font=("Wide Latin",23,"bold"),activebackground="orange",activeforeground="blue",bd="3").grid(row="5",column="3",rowspan="2",ipady="14",sticky=N+E+W+S)

Button(text="0",bg="#33E5FF",command=lambda:getValue(0),fg="black",font=("Wide Latin",23,"bold"),activebackground="orange",activeforeground="blue",bd="3").grid(row="6",column="0",ipadx="14",ipady="14",sticky=N+E+W+S)
Button(text="00",bg="#33E5FF",command=lambda:getValue("00"),fg="black",font=("Wide Latin",16,"bold"),activebackground="orange",activeforeground="blue",bd="3").grid(row="6",column="1",ipadx="14",ipady="14",sticky=N+E+W+S)

Button(text=".",bg="#33E5FF",command=lambda:getValue("."),fg="black",font=("Wide Latin",23,"bold"),activebackground="orange",activeforeground="blue",bd="3").grid(row="6",column="2",ipadx="14",ipady="14",sticky=N+E+W+S)

#Button(text="Clear",command=ch).grid(row="4",column="0",columnspan="4",ipadx="14",ipady="14",sticky=N+E+W+S)


Entry(font=("Pocket Calculator",35,"bold"),textvariable=inputdata,bg="gray",fg="white").grid(row="1",column="0",columnspan="4",ipadx=14,ipady=14)

l1 = Label(text="Welcome Makhan",bg="purple",fg="orange",font=("",30,"bold"))
l1.grid(row="0",column="0",columnspan="4")
root.mainloop()