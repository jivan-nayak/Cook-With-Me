from tkinter import *

def onclick():
    listobj = ["pizza", 'burger', 'cake', 'noodles']
    for item in listobj:
        my_list.insert(END, item)

def show():
    label2.config(text="You've selected " + my_list.get(ANCHOR))

master = Tk()
master.geometry("400x400")
label1 = Label(master, text = "This is for practice! \n Click the below button to view my favourite food")
label1.pack(pady=10)

btn = Button(master, text = "Click me to view my favourite food!", command=onclick)
btn.pack(pady=10)

my_list = Listbox(master)
my_list.pack(pady=5)

btn2 = Button(master, text="Submit", command=show)
btn2.pack(pady=2)

label2 = Label(master, text="")
label2.pack(pady=5)

master.mainloop()