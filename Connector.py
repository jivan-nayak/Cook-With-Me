import mysql.connector

def establish_connection():
    global mydb
    global mycursor
    mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='prices')
    mycursor = mydb.cursor()


establish_connection()
def ingredient(dish):
    mycursor.execute('SELECT product_name, price FROM products where dish in ("%s");' % (dish))
    myresult = mycursor
    total = 0
    string = ""
    for product_name, price in myresult:
        print("Product: " + str(product_name) + " Price: " + str(price))
        total += int(price)
        print()
        string = string + "Product: " + str(product_name) + " Price: " + str(price) + "\n"

    print(total)

    return string, total
