from tkinter import *
from PIL import Image, ImageTk

def onclickchinese():
    pass

def onclickindian():
    pass

def onclickfrench():
    pass

def onclickitalian():
    pass

master = Tk()
master.title("Cook with me !")
master.attributes('-fullscreen', True)
master.iconbitmap(
    "C:/Users/Jivan/Desktop/Mini Project/sem 5/Code/imgaes/bg2.ico")
background_image = PhotoImage(
    file='C:/Users/Jivan/Desktop/Mini Project/sem 5/Code/imgaes/bg1.png')
background_label = Label(master, image=background_image)
background_label.place(relwidth=1, relheight=1)


# Adding buttons with appropriate text labels
heading = Label(master, text="What are you craving today :P",
                font=("Felix Titling", 24), bg="#FFF1AF")
heading.place(relx=0.5, rely=0.5, anchor=CENTER)

img1 = Image.open('C:/Users/Jivan/Desktop/Mini Project/sem 5/Code/imgaes/ind.png').resize((200,300))
img1 = PhotoImage(img1)
label1 = Label(master, text="Indian Cuisine",
            font=("Felix Titling", 16), bg="#C3B091")
label1.place(relx=0.2, rely=0.37, anchor=CENTER)
indian = Button(master, text="Indian Cuisines", justify='center',
                command=onclickindian, image=img1, height=200, width=300)
indian.place(relx=0.2, rely=0.23, anchor=CENTER)

img2 = PhotoImage(
    file="C:/Users/Jivan/Desktop/Mini Project/sem 5/Code/imgaes/chinese-min.png")
label2 = Label(master, text="Chinese Cuisine",
            font=("Felix Titling", 16), bg="#C3B091")
label2.place(relx=0.8, rely=0.37, anchor=CENTER)
chinese = Button(master, text="Chinese Cuisines", command = onclickchinese,
                justify='center', image=img2, height=200, width=300)
chinese.place(relx=0.8, rely=0.23, anchor=CENTER)

img3 = PhotoImage(
    file="C:/Users/Jivan/Desktop/Mini Project/sem 5/Code/imgaes/french.png")
label3 = Label(master, text="French Cuisine",
            font=("Felix Titling", 16), bg="#C3B091")
label3.place(relx=0.2, rely=0.86, anchor=CENTER)
french = Button(master, text="French Cuisines", command = onclickfrench,
                justify='center', image=img3, height=200, width=300)
french.place(relx=0.2, rely=0.72, anchor=CENTER)

img4 = PhotoImage(
    file="C:/Users/Jivan/Desktop/Mini Project/sem 5/Code/imgaes/italian.png")
label4 = Label(master, text="Italian Cuisine",
            font=("Felix Titling", 16), bg="#C3B091")
label4.place(relx=0.8, rely=0.86, anchor=CENTER)
italian = Button(master, text="Italian Cuisines", command = onclickitalian,
                justify='center', image=img4, height=200, width=300)
italian.place(relx=0.8, rely=0.72, anchor=CENTER)

# img5 = PhotoImage(file="C:/Users/Jivan/Desktop/Mini Project/sem 5/Code/imgaes/korean.png")
# label5 = Label(master, text = "Korean Cuisine")
# label5.place(relx=0.1, rely=0.05, anchor=CENTER)
# korean = Button(master, text="Korean Cuisines", justify='center', image=img5)
# korean.place(relx=0.1, rely=0.05, anchor=CENTER)


master.mainloop()