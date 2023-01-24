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

    urls = ['https://www.bigbasket.com/pd/10000203/fresho-tomato-local-1-kg/?nc=as&q=tomato', 'https://www.bigbasket.com/pd/241600/tata-salt-iodized-1-kg-pouch/', 'https://www.bigbasket.com/pd/10000148/fresho-onion-1-kg/', 'https://www.bigbasket.com/pd/104864/amul-butter-pasteurised-500-g-carton/']

    dish = "Home made Tomato Sauce"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Home made Tomato Sauce"
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
    mainContent = Label(f2,  text="""This homemade tomato sauce recipe is proof that sometimes the best things in life are the simplest ones! Ripe tomatoes, salt, an onion and butter. That’s all you need for the greatest tomato sauce of all time.""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")
    ingredients = Button(f2,text="Source Ingredients",command=ingredient1).place(x = 400, y = 800)


    dish1 = Label(root, text="Go to site?",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish1.place(x = 1200, y = 750)
    dish1.bind("<Button-1>", lambda e:
    callback("https://www.oliviascuisine.com/homemade-tomato-sauce/"))
    root.mainloop()



###Second recipe
def second_dish():
    master.destroy()

    urls = ['https://www.bigbasket.com/pd/40207350/wingreens-farms-impatient-baker-easy-pizza-dough-mix-easy-to-make-500-g-pouch/?nc=as&q=pizza%20dough', 'https://www.bigbasket.com/pd/10000203/fresho-tomato-local-1-kg/?nc=as&q=tomato', 'https://www.bigbasket.com/pd/229136/amul-cheese-slices-750-g-pouch/?nc=as&q=cheese', 'https://www.bigbasket.com/pd/40094892/fresho-signature-chicken-breakfast-ham-sliced-300-g/?nc=as&q=ham', 'https://www.bigbasket.com/pd/40081759/keya-oregano-pizza-italian-80-g-canister/?nc=as&q=oregeno', 'https://www.bigbasket.com/pd/40129799/knorr-pizza-pasta-sauce-200-g/?nc=as&q=pizza%20sauce']

    dish = "Ham and Cheese Calzone"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Ham and Cheese Calzone"
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
    mainContent = Label(f2,  text="""Calzone for lunch, calzone for dinner, calzone for breakfast, calzone as a just because snack – I can eat a calzone anytime, anywhere!
    What’s not to love? Delicious pizza dough, check. Tons of juicy, flavorful ham, double check. Lots and lots of cheese, triple check!
    They are also incredibly versatile and a great way to use up leftovers. So if you have leftover ham or turkey after Thanksgiving/Christmas, make calzone! I guarantee you won’t be sorry!""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")
    ingredients = Button(f2,text="Source Ingredients",command=ingredient1).place(x = 400, y = 800)


    dish1 = Label(root, text="Go to site?",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish1.place(x = 1200, y = 750)
    dish1.bind("<Button-1>", lambda e:
    callback("https://www.oliviascuisine.com/ham-and-cheese-calzone/#Ingredients"))
    root.mainloop()


###Third recipe
def third_dish():
    master.destroy()

    urls = ['https://www.bigbasket.com/pd/10000908/fresho-chicken-curry-cut-without-skin-antibiotic-residue-free-13-15-pcs-500-g/?nc=as&q=chicken', 'https://www.bigbasket.com/pd/10000127/fresho-lemon-250-g/?nc=as&q=lemon', 'https://www.bigbasket.com/pd/161826/aashirvaad-atta-whole-wheat-2-kg-pouch/?nc=as&q=flour', 'https://www.bigbasket.com/pd/50000050/kodai-cheese-parmesan-200-g/?nc=as&q=parmesan', 'https://www.bigbasket.com/pd/104864/amul-butter-pasteurised-500-g-carton/?nc=as&q=butter','https://www.bigbasket.com/pd/274120/sunpure-refined-sunflower-oil-1-l-pouch/?nc=as&q=oil', 'https://www.bigbasket.com/pd/40005819/fresho-sambar-onion-peeled-small-onion-200-g/?nc=as&q=shallot', 'https://www.bigbasket.com/pd/40087450/de-nigris-vinegar-white-wine-500-ml/?nc=as&q=white%20wine']

    dish = "Chicken Piccata"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Chicken Piccata"
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
    mainContent = Label(f2,  text="""Easy chicken dinners should be up everyone’s sleeves, especially if you are constantly busy and struggling to put food on the table! From this Chicken Piccata to a delicious Chicken Marsala, Blackened Chicken Breasts and Sheet Pan Chicken with Spicy Potatoes""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")
    ingredients = Button(f2,text="Source Ingredients",command=ingredient1).place(x = 400, y = 800)


    dish1 = Label(root, text="Go to site?",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish1.place(x = 1200, y = 750)
    dish1.bind("<Button-1>", lambda e:
    callback("https://www.oliviascuisine.com/chicken-piccata/"))
    root.mainloop()


###Fourth recipe
def fourth_dish():
    master.destroy()

    urls = ['https://www.bigbasket.com/pd/40025355/fresho-whole-wheat-bread-safe-preservative-free-400-g/?nc=as&q=bread', 'https://www.bigbasket.com/pd/10000203/fresho-tomato-local-1-kg/?nc=as&q=tomato', 'https://www.bigbasket.com/pd/10000115/fresho-garlic-250-g/?nc=as&q=garlic', 'https://www.bigbasket.com/pd/274120/sunpure-refined-sunflower-oil-1-l-pouch/?nc=as&q=oil', 'https://www.bigbasket.com/pd/241600/tata-salt-iodized-1-kg-pouch/?nc=as&q=sa', 'https://www.bigbasket.com/pd/40202140/happychef-basil-25-g/?nc=as&q=basil']

    dish = "Tomato Bruschetta"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Tomato Bruschetta"
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
    dish1.place(x = 1200, y = 750)
    dish1.bind("<Button-1>", lambda e:
    callback("https://www.oliviascuisine.com/tomato-bruschetta/#Ingredients"))
    root.mainloop()


###Fifth recipe
def fifth_dish():
    master.destroy()

    urls = ['https://www.bigbasket.com/pd/10000908/fresho-chicken-curry-cut-without-skin-antibiotic-residue-free-13-15-pcs-500-g/?nc=as&q=chicken', 'https://www.bigbasket.com/pd/10000273/fresho-mushrooms-button-1-pack/?nc=as&q=mushroo', 'https://www.bigbasket.com/pd/10000148/fresho-onion-1-kg/?nc=as&q=shallot', 'https://www.bigbasket.com/pd/10000115/fresho-garlic-250-g/?nc=as&q=garlic', 'https://www.bigbasket.com/pd/40017684/castillo-de-salobrena-non-alcoholic-fruit-red-wine-1-l/?nc=as&q=red%20wine', 'https://www.bigbasket.com/pd/40005030/amul-fresh-cream-25-milk-fat-low-fat-1-l-carton/?nc=as&q=cream', 'https://www.bigbasket.com/pd/126906/aashirvaad-atta-whole-wheat-10-kg-pouch/?nc=as&q=flour', 'https://www.bigbasket.com/pd/104860/amul-butter-pasteurised-100-g-carton/?nc=as&q=butter', 'https://www.bigbasket.com/pd/40016673/disano-olive-oil-extra-virgin-500-ml-bottle/?nc=as&q=olive%20oil']

    dish = "Chicken Marsala"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Chicken Marsala"
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
    mainContent = Label(f2,  text="""Who doesn’t love a good chicken dinner? This chicken Marsala is better than the one you would get at a restaurant! And if you’re looking for more chicken breast recipes to add to your repertoire!""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")
    ingredients = Button(f2,text="Source Ingredients",command=ingredient1).place(x = 400, y = 800)


    dish1 = Label(root, text="Go to site?",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish1.place(x = 1200, y = 750)
    dish1.bind("<Button-1>", lambda e:
    callback("https://www.oliviascuisine.com/chicken-marsala/"))
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

    head = Label(f1, text = "Italian Cuisine", fg = "#fff2e6", bg="#D2042D", height=4, font=('Helveticabold', 35), justify="center").pack(side = "top", fill = "x")

    mainContent = Label(f2,  text="""Italian cuisine (Italian: Cucina italiana, pronounced [ku'tʃina ita'ljana]) is a Mediterranean cuisine consisting of the ingredients, recipes and cooking techniques developed across the Italian Peninsula since antiquity, and later spread around the world together with waves of Italian diaspora. Italian food is more than just pizza and spaghetti. There's a wide range of ingredients, flavors, and dishes to experiment with in your own home.""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#097969", wraplength=1500, justify="center")
    mainContent.pack(side="top")

    # btn = Button(f3, )

    # dish1 = Label(master, text="Lyonnaise Salad",font=('Helveticabold', 13), fg="black", cursor="hand2")
    # dish1.place(x = 110, y = 550)
    # dish1.bind("<Button-1>", lambda e:
    # callback("https://www.oliviascuisine.com/lyonnaise-salad/"))
    dish1 = Button(master, text="Home made Tomato Sauce",font=('Helveticabold', 13), fg="black", cursor="hand2",command=first_dish).place(x = 110, y = 550)

    dish2 = Button(master, text="Ham and Cheese Calzone",font=('Helveticabold', 13), fg="black", cursor="hand2",command=second_dish).place(x = 110, y = 625)

    dish3 = Button(master, text="Chicken Piccata",font=('Helveticabold', 13), fg="black", cursor="hand2", command=third_dish).place(x = 110, y = 700)

    dish4 = Button(master, text="Tomato Bruschetta",font=('Helveticabold', 13), fg="black", cursor="hand2", command=fourth_dish).place(x = 1000, y = 600)

    dish5 = Button(master, text="Chicken Marsala",font=('Helveticabold', 13), fg="black", cursor="hand2",command=fifth_dish).place(x = 1000, y = 675)

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


