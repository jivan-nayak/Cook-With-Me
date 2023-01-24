from distutils import command
from tkinter import *
import GUI
import webbrowser
import Connector
import sys
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
import re
import math
import Connector


###This fucntion scrapes the bigbasket for the ingredients and stores them in the data base
def scrape(urls, dish_name):

    sum = 0
    for url in urls:
        req = Request(url, headers = {"User-Agent": "Mozilla/5.0"})

        webpage = urlopen(req).read()
        soup = bs(webpage, "html.parser")
        # print(soup.prettify())

        div_title = soup.find("div", attrs = {"id": "title"})
        # print(div_title.prettify())
        print()
        header = div_title.find("h1")
        header = header.get_text()
        print(header)

        div_price = soup.find("div", attrs = {"id": "price"})
        # print(div_price.prettify())
        # price = div_price.find_all("td")
        price = div_price.get_text()
        td_list = div_price.find_all("td")
        price = td_list[1].get_text()
        print(price[3:])
        x = int(math.ceil(float(price[3:])))
        sum += x
        print("The current sum is: " + str(sum))
        print()

        Connector.establish_connection()
        Connector.mycursor.execute("INSERT INTO PRODUCTS(product_name, price, dish) VALUES(%s,%s,%s);",(header,x,dish_name))
        Connector.mydb.commit()


def on_click():
    master.destroy()

def quit():
    master.destroy()
    sys.exit()

def callback(url):
    webbrowser.open_new_tab(url)


###The first recipe
def first_dish():
    master.destroy()

    urls = ['https://www.bigbasket.com/pd/40094879/fresho-signature-pork-streaky-bacon-sliced-200-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40135854/bb-royal-organic-mustardrai-big-200-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40005819/fresho-sambar-onion-peeled-small-onion-200-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/270524/chings-secret-chilli-vinegar-170-ml-bottle/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40006250/borges-extra-virgin-olive-oil-1-l-pet-bottle/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40161158/upf-healthy-brown-eggs-6-pcs/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop']

    dish = "Lyonnaise Salad"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Lyonnaise Salad"
        string, total = Connector.ingredient(dish)
        label = Label(f2, text=string, wraplength=1500, font=('Helveticabold', 12), justify='left').place(x = 150, y = 475)
        print("Terminal output\n")
        print(string)

    ###Main driver of the program
    root = Tk()
    root.attributes("-fullscreen",True)
    f1 = Frame(root).pack(side = "top", fill = "x")
    head = Label(f1, text = dish, fg = "#fff2e6", bg="#040C0E", height=4, font=('Helveticabold', 35), justify="center").pack(side = "top", fill = "x")
    f2 = Frame(root).pack()
    mainContent = Label(f2,  text="""Whether Lyon ever was the gastronomic capital of France is debatable, but it sure has spawned some great dishes, including salade Lyonnaise, not the most simple salad ever made but one that approaches perfection in a way others do not. The combination of bitter greens (traditionally frisée, though escarole, dandelion, and arugula all work beautifully), crisp bacon, barely cooked eggs and warm vinaigrette is really unbeatable.""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")
    ingredients = Button(f2,text="Source Ingredients",command=ingredient1).place(x = 400, y = 800)


    dish1 = Label(root, text="Go to site?",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish1.place(x = 1200, y = 750)
    dish1.bind("<Button-1>", lambda e:
    callback("https://www.oliviascuisine.com/lyonnaise-salad/"))
    root.mainloop()



###Second recipe
def second_dish():
    master.destroy()

    urls = ['https://www.bigbasket.com/pd/10000908/fresho-chicken-curry-cut-without-skin-antibiotic-residue-free-13-15-pcs-500-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40135854/bb-royal-organic-mustardrai-big-200-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40094879/fresho-signature-pork-streaky-bacon-sliced-200-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40005819/fresho-sambar-onion-peeled-small-onion-200-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/10000115/fresho-garlic-250-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40026327/fresho-thyme-10-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/100210776/keya-parsley-15-g-bottle/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40087450/de-nigris-vinegar-white-wine-500-ml/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40102603/amul-fresh-cream-25-milk-fat-low-fat-250-ml/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/126906/aashirvaad-atta-whole-wheat-10-kg-pouch/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop']

    dish = "French Mustard Chicken"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "French Mustard Chicken"
        string, total = Connector.ingredient(dish)
        label = Label(f2, text=string, wraplength=1500, font=('Helveticabold', 12), justify='left').place(x = 150, y = 475)
        print("Terminal output\n")
        print(string)

    ###Main driver of the program
    root = Tk()
    root.attributes("-fullscreen",True)
    f1 = Frame(root).pack(side = "top", fill = "x")
    head = Label(f1, text = dish, fg = "#fff2e6", bg="#040C0E", height=4, font=('Helveticabold', 35), justify="center").pack(side = "top", fill = "x")
    f2 = Frame(root).pack()
    mainContent = Label(f2,  text="""French Mustard Chicken, or Poulet à la Moutarde, is a classic French dish that is simple but impressive! Chicken thighs are braised in a rich, creamy mustard sauce that will have you licking your plate clean. The whole dish comes together in just about an hour!""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")
    ingredients = Button(f2,text="Source Ingredients",command=ingredient1).place(x = 400, y = 800)


    dish1 = Label(root, text="Go to site?",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish1.place(x = 1200, y = 750)
    dish1.bind("<Button-1>", lambda e:
    callback("https://www.oliviascuisine.com/french-mustard-chicken/"))
    root.mainloop()


###Third recipe
def third_dish():
    master.destroy()

    urls = ['https://www.bigbasket.com/pd/40080803/dr-oetker-funfoods-veg-mayonnaise-original-875-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/10000115/fresho-garlic-250-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40069132/happychef-whole-grain-mustard-sauce-250-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40231284/al-ameera-tahina-spread-pure-rich-in-nutrition-protein-600-g-bottle/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40181626/valley-spice-red-chilli-powder-fiery-spicy-100-g-pet-bottle/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop']

    dish = "Sausage Chicken Cassoulet"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Sausage Chicken Cassoulet"
        string, total = Connector.ingredient(dish)
        label = Label(f2, text=string, wraplength=1500, font=('Helveticabold', 12), justify='left').place(x = 150, y = 475)
        print("Terminal output\n")
        print(string)

    ###Main driver of the program
    root = Tk()
    root.attributes("-fullscreen",True)
    f1 = Frame(root).pack(side = "top", fill = "x")
    head = Label(f1, text = dish, fg = "#fff2e6", bg="#040C0E", height=4, font=('Helveticabold', 35), justify="center").pack(side = "top", fill = "x")
    f2 = Frame(root).pack()
    mainContent = Label(f2,  text="""Inspired by the traditional French dish, this Sausage and Chicken Cassoulet is rich, hearty and perfect for cold winter days. It can be a labor of love, but believe me it is so worth it!""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")
    ingredients = Button(f2,text="Source Ingredients",command=ingredient1).place(x = 400, y = 800)


    dish1 = Label(root, text="Go to site?",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish1.place(x = 1200, y = 750)
    dish1.bind("<Button-1>", lambda e:
    callback("https://www.oliviascuisine.com/sausage-chicken-cassoulet/"))
    root.mainloop()


###Fourth recipe
def fourth_dish():
    master.destroy()

    urls = ['https://www.bigbasket.com/pd/40080803/dr-oetker-funfoods-veg-mayonnaise-original-875-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/10000115/fresho-garlic-250-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40069132/happychef-whole-grain-mustard-sauce-250-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40231284/al-ameera-tahina-spread-pure-rich-in-nutrition-protein-600-g-bottle/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40181626/valley-spice-red-chilli-powder-fiery-spicy-100-g-pet-bottle/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop']

    dish = "Roasted Garlic Aioli"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Roasted Garlic Aioli"
        string, total = Connector.ingredient(dish)
        label = Label(f2, text=string, wraplength=1500, font=('Helveticabold', 12), justify='left').place(x = 150, y = 475)
        print("Terminal output\n")
        print(string)

    ###Main driver of the program
    root = Tk()
    root.attributes("-fullscreen",True)
    f1 = Frame(root).pack(side = "top", fill = "x")
    head = Label(f1, text = dish, fg = "#fff2e6", bg="#040C0E", height=4, font=('Helveticabold', 35), justify="center").pack(side = "top", fill = "x")
    f2 = Frame(root).pack()
    mainContent = Label(f2,  text="""Hello, garlic lovers, this Roasted Garlic Aioli is for you! Creamy, garlicky and packed with umami flavor. Serve it on burgers, veggies or as a dip for McCain® fries!

""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")
    ingredients = Button(f2,text="Source Ingredients",command=ingredient1).place(x = 400, y = 800)


    dish1 = Label(root, text="Go to site?",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish1.place(x = 1000, y = 650)
    dish1.bind("<Button-1>", lambda e:
    callback("https://www.oliviascuisine.com/roasted-garlic-aioli/"))
    root.mainloop()


###Fifth recipe
def fifth_dish():
    master.destroy()

    urls = ['https://www.bigbasket.com/pd/40080803/dr-oetker-funfoods-veg-mayonnaise-original-875-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/10000115/fresho-garlic-250-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40069132/happychef-whole-grain-mustard-sauce-250-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40231284/al-ameera-tahina-spread-pure-rich-in-nutrition-protein-600-g-bottle/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40181626/valley-spice-red-chilli-powder-fiery-spicy-100-g-pet-bottle/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop']

    dish = "Blue Cheese Fig Tart"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Blue Cheese Fig Tart"
        string, total = Connector.ingredient(dish)
        label = Label(f2, text=string, wraplength=1500, font=('Helveticabold', 12), justify='left').place(x = 150, y = 475)
        print("Terminal output\n")
        print(string)

    ###Main driver of the program
    root = Tk()
    root.attributes("-fullscreen",True)
    f1 = Frame(root).pack(side = "top", fill = "x")
    head = Label(f1, text = dish, fg = "#fff2e6", bg="#040C0E", height=4, font=('Helveticabold', 35), justify="center").pack(side = "top", fill = "x")
    f2 = Frame(root).pack()
    mainContent = Label(f2,  text="""To celebrate Bastille Day, we can go full on French with a delicious savory and sweet Blue Cheese Fig Tart. Serve it for brunch, as an appetizer and/or as a snack and be ready for your tastebuds to start dancing the can-can!""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")
    ingredients = Button(f2,text="Source Ingredients",command=ingredient1).place(x = 400, y = 800)


    dish1 = Label(root, text="Go to site?",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish1.place(x = 1200, y = 750)
    dish1.bind("<Button-1>", lambda e:
    callback("https://www.oliviascuisine.com/blue-cheese-fig-tart/"))
    root.mainloop()


###Main driver program of the french cuisine
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

    # dish1 = Label(master, text="Lyonnaise Salad",font=('Helveticabold', 13), fg="black", cursor="hand2")
    # dish1.place(x = 110, y = 550)
    # dish1.bind("<Button-1>", lambda e:
    # callback("https://www.oliviascuisine.com/lyonnaise-salad/"))
    dish1 = Button(master, text="Lyonnaise Salad",font=('Helveticabold', 13), fg="black", cursor="hand2",command=first_dish).place(x = 110, y = 550)

    dish2 = Button(master, text="French Mustard Chicken (Poulet à la Moutarde)",font=('Helveticabold', 13), fg="black", cursor="hand2",command=second_dish).place(x = 110, y = 625)

    dish3 = Button(master, text="Sausage and Chicken Cassoulet",font=('Helveticabold', 13), fg="black", cursor="hand2", command=third_dish).place(x = 110, y = 700)

    dish4 = Button(master, text="Roasted Garlic Aioli",font=('Helveticabold', 13), fg="black", cursor="hand2", command=fourth_dish).place(x = 1000, y = 600)

    dish5 = Button(master, text="Blue Cheese Fig Tart",font=('Helveticabold', 13), fg="black", cursor="hand2",command=fifth_dish).place(x = 1000, y = 675)

    # dish2 = Label(master, text="French Mustard Chicken (Poulet à la Moutarde)",font=('Helveticabold', 13), fg="black", cursor="hand2")
    # dish2.place(x = 110, y = 625)
    # dish2.bind("<Button-1>", lambda e:callback("https://www.oliviascuisine.com/french-mustard-chicken/"))

    # dish3 = Label(master, text="French Mustard Chicken (Poulet à la Moutarde)",font=('Helveticabold', 13), fg="black", cursor="hand2")
    # dish3.place(x = 110, y = 700)
    # dish3.bind("<Button-1>", lambda e:callback("https://www.oliviascuisine.com/sausage-chicken-cassoulet/"))

    # dish4 = Label(master, text="French Mustard Chicken (Poulet à la Moutarde)",font=('Helveticabold', 13), fg="black", cursor="hand2")
    # dish4.place(x = 1000, y = 600)
    # dish4.bind("<Button-1>", lambda e:callback("https://www.oliviascuisine.com/roasted-garlic-aioli/"))

    # dish5 = Label(master, text="French Mustard Chicken (Poulet à la Moutarde)",font=('Helveticabold', 13), fg="black", cursor="hand2")
    # dish5.place(x = 1000, y = 675)
    # dish5.bind("<Button-1>", lambda e:callback("https://www.oliviascuisine.com/blue-cheese-fig-tart/"))

    master.mainloop()


