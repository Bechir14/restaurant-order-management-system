

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def _str_(self):
        return f"{self.name}: {self.price} TL"
    
class RestaurantOrderSystem:
    def __init__(self):
        self.customer_name = ""
        self.soup = None
        self.starters = []
        self.small_dish = None
        self.main_dish = None
        self.salad = None
        self.dessert = None
        self.drink = None




        self.small_dish_menu = [
            MenuItem("Pacha Borek", 105.0),
            MenuItem("Cheese Borek", 100.0),
            MenuItem("Potato Borek", 100.0),
            MenuItem("Spinach Borek", 100.0),
            MenuItem("Appetizers", 150.0),
            MenuItem("Courgette roll", 95.0),
            MenuItem("I don't want", 0.0),
        ]

        self.salad_menu = [
            MenuItem("Potato Salad", 70.0),
            MenuItem("Avocado Salad", 90.0),
            MenuItem("Caesar Salad", 120.0),
            MenuItem("Caprese Salad", 85.0),
            MenuItem("Seasonal Salad", 70.0),
            MenuItem("Green Salad", 70.0),
            MenuItem("I don't want", 0.0),
        ]

        self.burger_menu = [
            MenuItem("Classic Burger", 300),
            MenuItem("Cheeseburger", 200),
            MenuItem("Double Cheeseburger", 190),
            MenuItem("Bacon Burger", 180),
            MenuItem("BBQ Burger", 180),
            MenuItem("Spicy Chicken Burger", 190),
            MenuItem("Veggie Burger", 195),
            MenuItem("Mushroom Swiss Burger", 200),
            MenuItem("Tex-Mex Burger", 200),
            MenuItem("Black Angus Burger", 230),
        ]



        self.drink_menu = [
            MenuItem("Fanta", 80),
            MenuItem("Cola", 80),
            MenuItem("Ayran", 45),
            MenuItem("Mineral Water", 40),
            MenuItem("Tea", 40),
            MenuItem("Latte", 150),
            MenuItem("Espresso", 130),
            MenuItem("Mocha", 150),
            MenuItem("Turkish Coffee", 110),
            MenuItem("Mauritanian Tea", 100),
        ]

    def introduce_customer(self):
        print("Please enter your first and last name.")
        self.customer_name = input("First Last Name: ")
        print(f"Welcome, {self.customer_name}!")

    def make_selection(self, menu, category_name):
        print(f"Please choose a {category_name}:")
        for i, item in enumerate(menu, 1):
            print(f"{i} - {item.name}: {item.price} TL")
        selection = int(input()) - 1
        return menu[selection]

    def take_order(self):
        print("Welcome to the Restaurant Order System!")
        self.introduce_customer()
        print("Please select an option:")
        print("1 - Place an order")
        print("2 - I don't want anything")
        selection = int(input())

        if selection == 2:
            print("Have a nice day! See you again.")
            return False

        self.soup = self.make_selection(self.soup_menu, "Soup")
        self.starters.append(self.make_selection(self.starter_menu, "Starter"))
        self.small_dish = self.make_selection(self.small_dish_menu, "Small Dish")
        self.salad = self.make_selection(self.salad_menu, "Salad")
        self.main_dish = self.make_selection(self.main_dish_menu, "Main Dish")
        self.dessert = self.make_selection(self.dessert_menu, "Dessert")
        self.drink = self.make_selection(self.drink_menu, "Drink")
        return True

    def calculate_total(self):
        total_price = sum([item.price for item in [self.soup] + self.starters + [self.small_dish, self.salad, self.main_dish, self.dessert, self.drink]])
        return total_price

    def payment_method(self):
        print("\nSelect your payment method:")
        print("1 - Pay by card")
        print("2 - Pay by cash")
        selection = int(input())

        if selection == 1:
            print("You selected card payment.")
        elif selection == 2:
            print("You selected cash payment.")
        else:
            print("Invalid option. Cash payment selected.")
            return "Cash payment"
        return "Card payment"

    def order_summary(self):
        print(f"\nOrder summary for {self.customer_name}:")
        print(self.soup)
        for starter in self.starters:
           print(starter)
        print(self.small_dish)
        print(self.salad)
        print(self.main_dish)
        print(self.dessert)
        print(self.drink)
        print(f"Total Price: {self.calculate_total()} TL")

    def create_order(self):
        if self.take_order():
            self.order_summary()
            payment_method = self.payment_method()
            print(f"Thank you {self.customer_name}, your order has been created. Payment method: {payment_method}")
            print("Have a nice day!")
        else:
            print("No order placed. Exiting the system.")

    def getBurgerMenu(self):
        burgerArr = []
        for buger in self.burger_menu :
            temp = f"{buger.name} {buger.price}."
            burgerArr.append(temp)

        return burgerArr 
    

    def getDrinkMenu(self):
        drinkArr = []
        for drink in self.drink_menu :
            temp = f"{drink.name} {drink.price}."
            drinkArr.append(temp)

        return drinkArr 
