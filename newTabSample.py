#Import the required libraries
from tkinter import *
from tkinter.font import Font
import webbrowser

#Create an instance of tkinter frame
master = Tk()
master.attributes("-fullscreen",True)

#Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

#Create a Label to display the link
f1 = Frame(master).pack(side = "top", fill = "x")
f2 = Frame(master).pack()
f3 = Frame(master).pack()

head = Label(f1, text = "French Cuisine", fg = "#fff2e6", bg="#040C0E", height=4, font=('Helveticabold', 35), justify="center").pack(side = "top", fill = "x")

mainContent = Label(f2,  text="""French Oh la la! French food is so good, but can be quite intimidating. Don’t worry! My recipes are easy to make and will hopefully demystify French cuisine for you.\nAnyone can make a delicious boeuf bourguignon, cheesy gougères and/or a sexy gratin dauphinoise! Plus French pastries, desserts, entrées and sides to get you feeling like you are in Paris.\nCan’t find the French recipe you are looking for? Stay tuned, as I am constantly adding new recipes to this collection! Bon appétit!""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
mainContent.pack(side="top")

# btn = Button(f3, )

dish1 = Label(master, text="Lyonnaise Salad",font=('Helveticabold', 10), fg="blue", cursor="hand2")
dish1.place(x = 110, y = 550)
dish1.bind("<Button-1>", lambda e:
callback("https://www.oliviascuisine.com/lyonnaise-salad/"))

dish2 = Label(master, text="French Mustard Chicken (Poulet à la Moutarde)",font=('Helveticabold', 15), fg="black", cursor="hand2")
dish2.place(x = 110, y = 650)
dish2.bind("<Button-1>", lambda e:callback("https://www.oliviascuisine.com/french-mustard-chicken/"))

master.mainloop()