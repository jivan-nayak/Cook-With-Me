from tkinter import *
import GUI
import webbrowser


def on_click():
    master.destroy()

def quit():
    master.destroy()

def callback(url):
    webbrowser.open_new_tab(url)


def begin():
    global master
    master = Tk()
    master.attributes("-fullscreen",True)

    #Define a callback function
    def callback(url):
        webbrowser.open_new_tab(url)

    def back():
        master.destroy()
        GUI.begin()

    #Create a Label to display the link
    f1 = Frame(master).pack(side = "top", fill = "x")
    f2 = Frame(master).pack()
    f3 = Frame(master).pack()

    btn1 = Button(master, text = "Go Back", command = back).place(x = 425, y = 800)
    btn2 = Button(master, text="Quit",command=quit).place(x=1100,y=800)

    head = Label(f1, text = "French Cuisine", fg = "#fff2e6", bg="#040C0E", height=4, font=('Helveticabold', 35), justify="center").pack(side = "top", fill = "x")

    mainContent = Label(f2,  text="""French Oh la la! French food is so good, but can be quite intimidating. Don’t worry! My recipes are easy to make and will hopefully demystify French cuisine for you.\nAnyone can make a delicious boeuf bourguignon, cheesy gougères and/or a sexy gratin dauphinoise! Plus French pastries, desserts, entrées and sides to get you feeling like you are in Paris.\nCan’t find the French recipe you are looking for? Stay tuned, as I am constantly adding new recipes to this collection! Bon appétit!""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")

    # btn = Button(f3, )

    dish1 = Label(master, text="Lyonnaise Salad",font=('Helveticabold', 13), fg="blue", cursor="hand2")
    dish1.place(x = 110, y = 550)
    dish1.bind("<Button-1>", lambda e:
    callback("https://www.oliviascuisine.com/lyonnaise-salad/"))

    dish2 = Label(master, text="French Mustard Chicken (Poulet à la Moutarde)",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish2.place(x = 110, y = 625)
    dish2.bind("<Button-1>", lambda e:callback("https://www.oliviascuisine.com/french-mustard-chicken/"))

    dish3 = Label(master, text="French Mustard Chicken (Poulet à la Moutarde)",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish3.place(x = 110, y = 700)
    dish3.bind("<Button-1>", lambda e:callback("https://www.oliviascuisine.com/french-mustard-chicken/"))

    dish4 = Label(master, text="French Mustard Chicken (Poulet à la Moutarde)",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish4.place(x = 1000, y = 600)
    dish4.bind("<Button-1>", lambda e:callback("https://www.oliviascuisine.com/french-mustard-chicken/"))

    dish5 = Label(master, text="French Mustard Chicken (Poulet à la Moutarde)",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish5.place(x = 1000, y = 675)
    dish5.bind("<Button-1>", lambda e:callback("https://www.oliviascuisine.com/french-mustard-chicken/"))

    master.mainloop()


