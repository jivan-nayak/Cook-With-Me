from tkinter import *
from tkinter import font

global name
global email
global age
name = ["Shivam","Sandy","Yashas","Panda as pd","Me"]
email = ["abc","def","ghi","jkl","mno"]
age = [1,2,3,4,5]

def submit():
    name.append(var1.get())
    email.append(var2.get())
    age.append(var3.get())
    display()
    
def delete():
    name.pop()
    age.pop()
    email.pop()
    display()

def display():
    label1 = Label(master, text="Name", width=20, font=("bold")).place(x=68,y=240)
    label1 = Label(master, text="Email", width=20, font=("bold")).place(x=68,y=260)
    label1 = Label(master, text="Age", width=20, font=("bold")).place(x=68,y=280)
    label1 = Label(master, text=name, width=100, font=("bold")).place(x=800,y=240)
    label1 = Label(master, text=email, width=100, font=("bold")).place(x=800,y=260)
    label1 = Label(master, text=age, width=100, font=("bold")).place(x=800,y=280)

master = Tk()
master.geometry("1000x1000")
label = Label(master, text = "Registration From", font=("bold",14)).place(x = 90, y = 60)

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()

label1 = Label(master, text="Name", width=20, font=("bold",12)).place(x=68,y=90)
txt1 = Entry(master, text=var1, width=20).place(x=200,y=90)

label2 = Label(master, text="Email", width=20, font=("bold",12)).place(x=68,y=110)
txt2 = Entry(master, text=var2, width=20).place(x=200,y=110)

label3 = Label(master, text="Age", width=20, font=("bold",12)).place(x=68,y=130)
txt3 = Entry(master, text=var3, width=20).place(x=200,y=130)

btn = Button(master, text="Submit", command=submit).place(x=90,y=200)
btn1 = Button(master, text="Delete", command=delete).place(x=150,y=200)

master.mainloop()