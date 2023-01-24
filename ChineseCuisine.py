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

    urls = ['https://www.bigbasket.com/pd/10000166/fresho-radish-white-500-g/?nc=as&q=raddish', 'https://www.bigbasket.com/pd/10000082/fresho-chilli-green-long-medium-250-g/?nc=as&q=chilli', 'https://www.bigbasket.com/pd/50000478/fresho-capsicum-green-organically-grown-250-g/?nc=as&q=green%20pepper', 'https://www.bigbasket.com/pd/270509/chings-secret-dark-soy-sauce-210-g-bottle/?nc=as&q=soy%20sauce', 'https://www.bigbasket.com/pd/40141933/double-horse-synthetic-vinegar-1-l-plastic-bottle/?nc=as&q=vinegar', 'https://www.bigbasket.com/pd/10000117/fresho-ginger-100-g/?nc=as&q=ginger', 'https://www.bigbasket.com/pd/10000115/fresho-garlic-250-g/?nc=as&q=garlic', 'https://www.bigbasket.com/pd/40070768/tata-sampann-chilli-powder-100-g/', 'https://www.bigbasket.com/pd/100554/saffola-tasty-refined-cooking-oil-blended-rice-bran-corn-oil-pro-fitness-conscious-1-l-pouch/?nc=as&q=vegetable%20oil']

    dish = "Hot and Sour Pickled Radish"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Hot and Sour Pickled Radish"
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
    mainContent = Label(f2,  text="""Winter is the great season for radish. For me, I get my favorite 4 ways of cooking white radish — Sichuan style pickling in big jars, used in braised dishes like beef and radish, in soups and this quite pickling.
    It is widely served in breakfast restaurant, hot pot restaurant and noodle restaurants all year around. But I love to serve this in winter along with fatty dishes like red braised pork belly or hot pot dinner. Each time I make a large batch but it is finished even faster than delicious main course. It presents an appealing looking and a profound hot yet sour flavor.

""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")
    ingredients = Button(f2,text="Source Ingredients",command=ingredient1).place(x = 400, y = 800)


    dish1 = Label(root, text="Go to site?",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish1.place(x = 1200, y = 750)
    dish1.bind("<Button-1>", lambda e:
    callback("https://www.chinasichuanfood.com/hot-and-sour-pickled-radish/"))
    root.mainloop()



###Second recipe
def second_dish():
    master.destroy()

    urls = ['https://www.bigbasket.com/pd/10000117/fresho-ginger-100-g/?nc=as&q=ginger', 'https://www.bigbasket.com/pd/10000115/fresho-garlic-250-g/?nc=as&q=garlic', 'https://www.bigbasket.com/pd/40070768/tata-sampann-chilli-powder-100-g/', 'https://www.bigbasket.com/pd/10000054/fresho-brinjal-bottle-shape-500-g/?nc=as&q=eggplant', 'https://www.bigbasket.com/pd/40094813/fresho-signature-pork-smoked-breakfast-ham-sliced-200-g/?nc=as&q=pork', 'https://www.bigbasket.com/pd/40005769/fresho-beans-julienne-200-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40070789/saffola-gold-refined-cooking-oil-blended-rice-bran-sunflower-oil-helps-keeps-heart-healthy-15-l-jar/?nc=as&q=cooking%20oil', 'https://www.bigbasket.com/pd/40070768/tata-sampann-chilli-powder-100-g/?nc=as&q=chilli%20powder', 'https://www.bigbasket.com/pd/244096/madhur-sugar-refined-1-kg-pouch/?nc=as&q=sugar']

    dish = "Mapo Eggplants"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Mapo Eggplants"
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
    mainContent = Label(f2,  text="""Sichuan braised eggplants is another great rice killer eggplant recipe.
The sauces used is very similar with Mapo tofu, only Sichuan peppercorn powder is slightly limited. Days ago, I get a lovely feedback about my favorite mapo tofu saying the flavors and sauce of Mapo tofu is so great and is there any other ingredients that can match well with Mapo sauce? Then I thought about the idea in my mind and found several possible ingredients– eggplants, winter melon and radish.""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")
    ingredients = Button(f2,text="Source Ingredients",command=ingredient1).place(x = 400, y = 800)


    dish1 = Label(root, text="Go to site?",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish1.place(x = 1200, y = 750)
    dish1.bind("<Button-1>", lambda e:
    callback("https://www.chinasichuanfood.com/sichuan-eggplants/"))
    root.mainloop()


###Third recipe
def third_dish():
    master.destroy()

    urls = ['https://www.bigbasket.com/pd/10000273/fresho-mushrooms-button-1-pack/?nc=as&q=mushroom', 'https://www.bigbasket.com/pd/40086160/sanjay-namkeen-roasted-groundnut-200-g/?nc=as&q=roasted%20peanuts', 'https://www.bigbasket.com/pd/40075537/fresho-onion-2-kg/?nc=as&q=onion', 'https://www.bigbasket.com/pd/40070768/tata-sampann-chilli-powder-100-g/?nc=as&q=chilli%20powder', 'https://www.bigbasket.com/pd/147491/saffola-gold-refined-cooking-oil-blended-rice-bran-sunflower-oil-helps-keeps-heart-healthy-1-l-pouch/?nc=as&q=cooking%20oil', 'https://www.bigbasket.com/pd/10000117/fresho-ginger-100-g/?nc=as&q=ginger', 'https://www.bigbasket.com/pd/10000115/fresho-garlic-250-g/?nc=as&q=garlic']

    dish = "Kung Pao Mushroom"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Kung Pao Mushroom"
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
    mainContent = Label(f2,  text="""Kung Pao sauce is one of the popular home style stir fry sauces in Szechuan cuisine. Kung pao sauce has two layers of flavor, one is from spices and the other one is from a balanced flavor bought by soy sauce, vinegar and sugar.""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")
    ingredients = Button(f2,text="Source Ingredients",command=ingredient1).place(x = 400, y = 800)


    dish1 = Label(root, text="Go to site?",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish1.place(x = 1200, y = 750)
    dish1.bind("<Button-1>", lambda e:
    callback("https://www.chinasichuanfood.com/kung-pao-mushroom/"))
    root.mainloop()


###Fourth recipe
def fourth_dish():
    master.destroy()

    urls = ['https://www.bigbasket.com/pd/40026596/bb-royal-soya-bean-1-kg-pouch/?nc=as&q=soya%20bean', 'https://www.bigbasket.com/pd/40211241/bisleri-mineral-water-10-l-can/?nc=as&q=mineral%20water']

    dish = "Tofu Skin"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Tofu Skin"
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
    callback("https://www.chinasichuanfood.com/how-to-make-tofu-skin/"))
    root.mainloop()


###Fifth recipe
def fifth_dish():
    master.destroy()

    urls = ['https://www.bigbasket.com/pd/10000117/fresho-ginger-100-g/?nc=as&q=ginger', 'https://www.bigbasket.com/pd/10000115/fresho-garlic-250-g/?nc=as&q=garlic', 'https://www.bigbasket.com/pd/10000908/fresho-chicken-curry-cut-without-skin-antibiotic-residue-free-13-15-pcs-500-g/', 'https://www.bigbasket.com/pd/171320/lee-kum-kee-sauce-oyster-510-g-bottle/?nc=as&q=oyster', 'https://www.bigbasket.com/pd/40067874/weikfield-soya-sauce-220-g/?nc=as&q=soy%20sauce', 'https://www.bigbasket.com/pd/241600/tata-salt-iodized-1-kg-pouch/?nc=as&q=salt', 'https://www.bigbasket.com/pd/40044725/bb-royal-corn-flour-starch-1-kg/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop', 'https://www.bigbasket.com/pd/40200484/happychef-baking-soda-100-g/?nc=as&q=baking%20soda', '']

    dish = "Pan-Fried Black Pepper Chicken"
    scrape(urls,dish)

    ###This function establishes an connection with mysql and queries the ingredients and stores the in string that can be displayed
    def ingredient1():
        dish = "Pan-Fried Black Pepper Chicken"
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
    mainContent = Label(f2,  text="""Chicken with bones like chicken legs, wings and whole are much more popular than chicken breast in Chinese cuisine as the former ones are believed to be much easier to cook.""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")
    ingredients = Button(f2,text="Source Ingredients",command=ingredient1).place(x = 400, y = 800)


    dish1 = Label(root, text="Go to site?",font=('Helveticabold', 13), fg="black", cursor="hand2")
    dish1.place(x = 1200, y = 750)
    dish1.bind("<Button-1>", lambda e:
    callback("https://www.chinasichuanfood.com/pan-fried-black-pepper-chicken/"))
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

    head = Label(f1, text = "Chinese Cuisine", fg = "#fff2e6", bg="#040C0E", height=4, font=('Helveticabold', 35), justify="center").pack(side = "top", fill = "x")

    mainContent = Label(f2,  text="""Chinese cuisine is an important part of Chinese culture and includes cuisines originating from China. Because of the Chinese diaspora and historical power of the country, Chinese cuisine has influenced many other cuisines in Asia and beyond, with modifications made to cater to local palates. Chinese food staples such as rice, soy sauce, noodles, tea, chili oil, and tofu, and utensils such as chopsticks and the wok, can now be found worldwide.""",padx=50, pady=75, font=('Helveticabold', 15), fg = "#ffe6e6", bg="#132226", wraplength=1500, justify="center")
    mainContent.pack(side="top")

    # btn = Button(f3, )

    # dish1 = Label(master, text="Lyonnaise Salad",font=('Helveticabold', 13), fg="black", cursor="hand2")
    # dish1.place(x = 110, y = 550)
    # dish1.bind("<Button-1>", lambda e:
    # callback("https://www.oliviascuisine.com/lyonnaise-salad/"))
    dish1 = Button(master, text="Hot and Sour Pickled Radish",font=('Helveticabold', 13), fg="black", cursor="hand2",command=first_dish).place(x = 110, y = 550)

    dish2 = Button(master, text="Mapo Eggplants",font=('Helveticabold', 13), fg="black", cursor="hand2",command=second_dish).place(x = 110, y = 625)

    dish3 = Button(master, text="Kung Pao Mushroom",font=('Helveticabold', 13), fg="black", cursor="hand2", command=third_dish).place(x = 110, y = 700)

    dish4 = Button(master, text="Tofu Skin",font=('Helveticabold', 13), fg="black", cursor="hand2", command=fourth_dish).place(x = 1000, y = 600)

    dish5 = Button(master, text="Pan-Fried Black Pepper Chicken",font=('Helveticabold', 13), fg="black", cursor="hand2",command=fifth_dish).place(x = 1000, y = 675)

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


