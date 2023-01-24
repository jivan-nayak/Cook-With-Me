
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
import re
import math
import Connector
import mysql.connector

urls = ["https://www.bigbasket.com/pd/40205936/puramate-whipped-cream-powder-butterscotch-100-g/", "https://www.bigbasket.com/pd/10000273/fresho-mushrooms-button-1-pack/", "https://www.bigbasket.com/pd/40003573/colavita-vinegar-white-wine-product-of-italy-500-ml-bottle/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop", "https://www.bigbasket.com/pd/10000908/fresho-chicken-curry-cut-without-skin-antibiotic-residue-free-13-15-pcs-500-g/?nc=l3category&t_pg=L3Categories&t_p=l3category&t_s=l3category&t_pos=3&t_ch=desktop", "https://www.bigbasket.com/pd/40006250/borges-extra-virgin-olive-oil-1-l-pet-bottle/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop"]

sum = 0

for url in urls:
    dish = "Lyonnaise Salad"
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
    Connector.mycursor.execute("INSERT INTO PRODUCTS(product_name, price, dish) VALUES(%s,%s,%s);",(header,x,dish))
    Connector.mydb.commit()

print(len("Fresho Chicken - Curry Cut Without Skin, Antibiotic Residue Free, 13-15 pcs, 500 g"))