import sqlite3 
from menu import RestaurantOrderSystem 
# we connect to the DB
con = sqlite3.connect("restaurant.db")

# create the cursor
cursor = con.cursor()

def UpdateMenu(item_name):
    try:
        # Check if the item exists in the menu and get its current quantity
        query = "SELECT availableQuantity FROM menu WHERE MenuItem = ?"
        cursor.execute(query, (item_name,))
        result = cursor.fetchone()

        if result is None:
            print(f"Item '{item_name}' does not exist in the menu.")
            return False

        current_quantity = result[0]

        # Check if the item is available (quantity > 0)
        if current_quantity <= 0:
            print(f"Item '{item_name}' is out of stock.")
            return False

        # Subtract one from the current quantity
        new_quantity = current_quantity - 1
        update_query = "UPDATE menu SET availableQuantity = ? WHERE MenuItem = ?"
        cursor.execute(update_query, (new_quantity, item_name))
        con.commit()

        print(f"One unit of '{item_name}' has been substracted. New quantity: {new_quantity}")
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    

def buy( name , amount ):
    try:
        # Check if the customer exists and get their current budget
        query = "SELECT budget FROM customers WHERE firstName = ?"
        cursor.execute(query, (name,))
        result = cursor.fetchone()

        if result is None:
            print(f"Customer {name} does not exist.")
            return False

        current_budget = result[0]

        # Check if the customer has enough budget
        if current_budget < amount:
            print(f"Customer {name} does not have enough budget.")
            return False

        # Subtract the amount from the budget
        new_budget = current_budget - amount
        update_query = "UPDATE customers SET budget = ? WHERE firstName = ?"
        cursor.execute(update_query, (new_budget, name))
        con.commit()

        print(f"{amount} has been subtracted from {name}'s budget.")
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False 

def createCustomerDB():
    cursor.execute("""CREATE TABLE IF NOT EXISTS customers(
       firstName TEXT,
       budget INTEGER              
       )              
    """)
    con.commit()

createCustomerDB()

def addCustomer(name , budget):
    cursor.execute("""
        INSERT INTO customers (firstName , budget)
        VALUES(?, ?)           
    """,(name, budget))
    con.commit

def is_name_in_table(name):
    query = "SELECT 1 FROM customers WHERE firstName = ? LIMIT 1"
    cursor.execute(query, (name,))
    result = cursor.fetchone()
    return result is not None


def createMenuDB():
    cursor.execute("""CREATE TABLE IF NOT EXISTS menu(
       MenuItem TEXT,
       price INTEGER,
       availableQuantity INTEGER     
       )              
    """)
    con.commit()

createMenuDB()

def addMenuItem(name , budget, availableQuantity):
    cursor.execute("""
        INSERT INTO menu (MenuItem , price ,availableQuantity)
        VALUES(?, ?, ?)           
    """,(name, budget , availableQuantity))
    con.commit()


def getUserBalance(name):
    query = "SELECT budget FROM customers WHERE firstName = ?"
    cursor.execute(query, (name,))
    result = cursor.fetchone()
    return result[0]


resto = RestaurantOrderSystem()


    

for burger in resto.burger_menu:
    addMenuItem(burger.name, burger.price , 5)

for drink in resto.drink_menu:
    addMenuItem(drink.name , drink.price , 5)

def displayTable():
    cursor.execute(""" SELECT * FROM menu """)
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("the table is empty")


# cursor.execute("""DELETE FROM menu""")
# cursor.execute("""DELETE FROM customers""")

con.commit()

displayTable()