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

    urls = ['https://www.bigbasket.com/pd/10000908/fresho-chicken-curry-cut-without-skin-antibiotic-residue-free-13-15-pcs-500-g/?nc=as&q=chicken', 'https://www.bigbasket.com/pd/10000117/fresho-ginger-100-g/?nc=as&q=ginger', 'https://www.bigbasket.com/pd/10000115/fresho-garlic-250-g/?nc=as&q=garlic', 'https://www.bigbasket.com/pd/40128824/everest-masala-garam-200-g/?nc=as&q=garam%20masala', 'https://www.bigbasket.com/pd/40075537/fresho-onion-2-kg/?nc=as&q=nion', 'https://www.bigbasket.com/pd/1208984/dabur-hommade-tomato-puree-2x200-g/?nc=as&q=tomato%20pu','https://www.bigbasket.com/pd/40102603/amul-fresh-cream-25-milk-fat-low-fat-250-ml/?nc=as&q=cream','https://www.bigbasket.com/pd/40072502/bb-royal-organic-cinnamondalchini-100-g/?nc=as&q=cinnamon','https://www.bigbasket.com/pd/269285/everest-powder-kashmirilal-ground-chilly-100-g-carton/?nc=as&q=kashmiri%20chilli']

    dish = "Chicken tikka masala"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Chicken tikka masala"
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
    mainContent = Label(f2,  text="""This rich and creamy flavoursome Chicken tikka rivals any Indian restaurant! Why go out when you can make it better at home! With aromatic golden chicken pieces swimming in an incredible curry sauce, this Chicken Tikka Masala recipe is one of the best you will try! Pair it with our buttery garlic naan breads!""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")
    ingredients = Button(f2,text="Source Ingredients",command=ingredient1).place(x = 400, y = 800)


    dish1 = Label(root, text="Go to site?",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish1.place(x = 1200, y = 750)
    dish1.bind("<Button-1>", lambda e:
    callback("https://cafedelites.com/chicken-tikka-masala/"))
    root.mainloop()



###Second recipe
def second_dish():
    master.destroy()

    urls = ['https://www.bigbasket.com/pd/10000908/fresho-chicken-curry-cut-without-skin-antibiotic-residue-free-13-15-pcs-500-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/104860/amul-butter-pasteurised-100-g-carton/?nc=as&q=butter', 'https://www.bigbasket.com/pd/40016675/disano-olive-oil-extra-virgin-250-ml-bottle/?nc=as&q=olive%20oil', 'https://www.bigbasket.com/pd/40003573/colavita-vinegar-white-wine-product-of-italy-500-ml-bottle/?nc=as&q=white%20wine', 'https://www.bigbasket.com/pd/10000127/fresho-lemon-250-g/?nc=as&q=lemon', 'https://www.bigbasket.com/pd/40109372/bb-royal-organic-black-pepperkali-mirchi-200-g/?nc=as&q=pepper', 'https://www.bigbasket.com/pd/10000154/fresho-parsley-leaves-curly-100-g/?nc=as&q=parsl', 'https://www.bigbasket.com/pd/40203901/bb-royal-organic-cloves-100-g/?nc=as&q=cloves', 'https://www.bigbasket.com/pd/10000115/fresho-garlic-250-g/?nc=as&q=garlic', 'https://www.bigbasket.com/pd/40135715/organic-nation-rosemary-30-g/?nc=as&q=rosemer']

    dish = "Garlic herb butter roast chicken"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Garlic herb butter roast chicken"
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
    callback("https://cafedelites.com/garlic-herb-butter-roast-chicken/"))
    root.mainloop()


###Third recipe
def third_dish():
    master.destroy()

    urls = ['https://www.bigbasket.com/pd/147491/saffola-gold-refined-cooking-oil-blended-rice-bran-sunflower-oil-helps-keeps-heart-healthy-1-l-pouch/?nc=as&q=cooking%20oil', 'https://www.bigbasket.com/pd/104864/amul-butter-pasteurised-500-g-carton/?nc=as&q=butter', 'https://www.bigbasket.com/pd/40203901/bb-royal-organic-cloves-100-g/?nc=as&q=cloves', 'https://www.bigbasket.com/pd/30000285/bb-royal-cardamomelaichi-green-20-g-pouch/?nc=as&q=cardamum', 'https://www.bigbasket.com/pd/40003150/milky-mist-paneer-premium-fresh-500-g-pouch/','https://www.bigbasket.com/pd/40075537/fresho-onion-2-kg/?nc=as&q=onion','https://www.bigbasket.com/pd/10000115/fresho-garlic-250-g/?nc=as&q=garli','https://www.bigbasket.com/pd/10000117/fresho-ginger-100-g/?nc=as&q=ginger','https://www.bigbasket.com/pd/10000204/fresho-tomato-local-500-g/?nc=as&q=tomato','https://www.bigbasket.com/pd/10000551/bb-popular-cashewkaju-whole-500-g/?nc=as&q=cashew','https://www.bigbasket.com/pd/20000457/bb-royal-bay-leaftej-patta-50-g/?nc=as&q=bay%20lea','https://www.bigbasket.com/pd/10000081/fresho-chilli-green-long-medium-100-g/?nc=as&q=chilli','https://www.bigbasket.com/pd/268012/everest-garam-masala-50-g-carton/?nc=as&q=garam%20masala']

    dish = "Paneer butter masala"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Paneer butter masala"
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
    mainContent = Label(f2,  text="""Paneer Butter Masala is one of India’s most popular paneer gravy recipe. This recipe with Indian cottage cheese cubes in a creamy tomato sauce is one that I have been making for a long time.""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")
    ingredients = Button(f2,text="Source Ingredients",command=ingredient1).place(x = 400, y = 800)


    dish1 = Label(root, text="Go to site?",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish1.place(x = 1200, y = 750)
    dish1.bind("<Button-1>", lambda e:
    callback("https://hebbarskitchen.com/paneer-butter-masala-recipe/"))
    root.mainloop()


###Fourth recipe
def fourth_dish():
    master.destroy()

    urls = ['https://www.bigbasket.com/pd/40203901/bb-royal-organic-cloves-100-g/?nc=as&q=cloves', 'https://www.bigbasket.com/pd/30000285/bb-royal-cardamomelaichi-green-20-g-pouch/?nc=as&q=cardamum', 'https://www.bigbasket.com/pd/40069132/happychef-whole-grain-mustard-sauce-250-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40070768/tata-sampann-chilli-powder-100-g/?nc=as&q=chilli%20powder', 'https://www.bigbasket.com/pd/1216264/mothers-recipe-paste-ginger-garlic-3x200-g/?nc=as&q=ginger%20garlic%20paste','https://www.bigbasket.com/pd/10000074/fresho-cauliflower-1-pc/?nc=as&q=cauliflower','https://www.bigbasket.com/pd/40048457/fresho-potato-new-crop-1-kg/?nc=as&q=potato','https://www.bigbasket.com/pd/147491/saffola-gold-refined-cooking-oil-blended-rice-bran-sunflower-oil-helps-keeps-heart-healthy-1-l-pouch/?nc=as&q=cooking%20oil','https://www.bigbasket.com/pd/10000081/fresho-chilli-green-long-medium-100-g/?nc=as&q=xhilli','']

    dish = "Aloo gobi"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Aloo gobi"
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
    mainContent = Label(f2,  text="""Aloo Gobi is a classic vegetarian Indian dish translating to potatoes (aloo) cauliflower (gobi). It's a one pot, super simple, comforting dish that's ready quickly. Serve it as a side or over rice. Some variations include onion or tomato, which can easily be added here.

""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")
    ingredients = Button(f2,text="Source Ingredients",command=ingredient1).place(x = 400, y = 800)


    dish1 = Label(root, text="Go to site?",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish1.place(x = 1200, y = 750)
    dish1.bind("<Button-1>", lambda e:
    callback("https://hebbarskitchen.com/aloo-gobi-dry-recipe-aloo-gobhi-ki-sabji/"))
    root.mainloop()


###Fifth recipe
def fifth_dish():
    master.destroy()

    urls = ['https://www.bigbasket.com/pd/147491/saffola-gold-refined-cooking-oil-blended-rice-bran-sunflower-oil-helps-keeps-heart-healthy-1-l-pouch/?nc=as&q=cooking%20oil', 'https://www.bigbasket.com/pd/30000285/bb-royal-cardamomelaichi-green-20-g-pouch/?nc=as&q=cardamum', 'https://www.bigbasket.com/pd/40044729/bb-royal-maida-2-kg-pouch/?nc=as&q=maida', 'https://www.bigbasket.com/pd/244096/madhur-sugar-refined-1-kg-pouch/?nc=as&q=sugar', 'https://www.bigbasket.com/pd/40053900/bb-royal-cooking-soda-100-g/?nc=as&q=baking%20soda','https://www.bigbasket.com/pd/1205131/dabur-hommade-tomato-puree-3x200-g/?nc=as&q=tomato%20puree','https://www.bigbasket.com/pd/241600/tata-salt-iodized-1-kg-pouch/?nc=as&q=salt','https://www.bigbasket.com/pd/274145/fortune-sun-lite-sunflower-refined-oil-1-l-pouch/?nc=as&q=oil','https://www.bigbasket.com/pd/40003162/milky-mist-curd-farm-fresh-500-g-pouch/?nc=as&q=curd','https://www.bigbasket.com/pd/30005421/bb-popular-kabuli-channa-1-kg-pouch/?nc=as&q=chickpea','https://www.bigbasket.com/pd/40072502/bb-royal-organic-cinnamondalchini-100-g/?nc=as&q=cinnamon','https://www.bigbasket.com/pd/30000308/bb-royal-cuminjeera-whole-50-g/?nc=as&q=jeer','https://www.bigbasket.com/pd/40075537/fresho-onion-2-kg/?nc=as&q=onion']

    dish = "Chole bhature"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Chole bhature"
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
    mainContent = Label(f2,  text="""Chole bhature is a food dish popular in the Northern areas of the Indian subcontinent. It is a combination of chana masala and bhatura/puri, a fried bread made from maida.""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")
    ingredients = Button(f2,text="Source Ingredients",command=ingredient1).place(x = 400, y = 800)


    dish1 = Label(root, text="Go to site?",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish1.place(x = 1200, y = 750)
    dish1.bind("<Button-1>", lambda e:
    callback("https://hebbarskitchen.com/chole-bhature-recipe-chana-bhatura/"))
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

    head = Label(f1, text = "Indian Cuisine", fg = "#fff2e6", bg="#040C0E", height=4, font=('Helveticabold', 35), justify="center").pack(side = "top", fill = "x")

    mainContent = Label(f2,  text="""Indian cuisine consists of a variety of regional and traditional cuisines native to the Indian subcontinent. Given the diversity in soil, climate, culture, ethnic groups, and occupations, these cuisines vary substantially and use locally available spices, herbs, vegetables, and fruits.""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")

    # btn = Button(f3, )

    # dish1 = Label(master, text="Lyonnaise Salad",font=('Helveticabold', 13), fg="black", cursor="hand2")
    # dish1.place(x = 110, y = 550)
    # dish1.bind("<Button-1>", lambda e:
    # callback("https://www.oliviascuisine.com/lyonnaise-salad/"))
    dish1 = Button(master, text="Chicken tikka masala",font=('Helveticabold', 13), fg="black", cursor="hand2",command=first_dish).place(x = 110, y = 550)

    dish2 = Button(master, text="Garlic herb butter roast chicken",font=('Helveticabold', 13), fg="black", cursor="hand2",command=second_dish).place(x = 110, y = 625)

    dish3 = Button(master, text="Paneer butter masala",font=('Helveticabold', 13), fg="black", cursor="hand2", command=third_dish).place(x = 110, y = 700)

    dish4 = Button(master, text="Aloo gobi",font=('Helveticabold', 13), fg="black", cursor="hand2", command=fourth_dish).place(x = 1000, y = 600)

    dish5 = Button(master, text="Chole bhature",font=('Helveticabold', 13), fg="black", cursor="hand2",command=fifth_dish).place(x = 1000, y = 675)

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


