import customtkinter as ctk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from menu import RestaurantOrderSystem
from tkinter import messagebox
import DB
from TUMorders import OrderSummaryPopup



# Define drink URLs
drinks = [
    "https://cdn.shopify.com/s/files/1/0558/6413/1764/files/Fanta_Logo_Design_History_Evolution_0_1024x1024.jpg?v=1693460247",  # fanta
    "https://www.coca-cola.com/content/dam/onexp/tr/tr/coca-cola-single-page/tr_coca-cola_desktopbanner_1440x810.jpg",  # cola
    "https://cdn.cimri.io/market/260x260/sutas-180-gr-bardak-ayran-_247456.jpg",  # ayran
    "https://paris-store.com/wp-content/uploads/2022/08/001920.jpg",  # mineral water
    "https://i.lezzet.com.tr/images-xxlarge-secondary/ac-karnina-cay-icmek-zararli-mi-fe626678-237e-4407-a88e-5693bf434a71.jpg",  # çay
    "https://spectrarestaurant.com/wp-content/uploads/2022/03/cafe-Latte.jpg",  # caffe latte
    "https://blogstudio.s3.theshoppad.net/coffeeheroau/ec178d83e5f597b162cda1e60cb64194.jpg" ,#esspresso coffe
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEvPfVPZxAsmoYSRPs0vdc0Fbi_zPxR16-_Q&s" ,#mocha 
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlA0gV4b6JCI6KYidVkYaygObPlSgtf7caVQ&s" ,# turk kahvesi
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwvwd_9C79ufHb33T5kilk0_dxSAhj9KuBvQ&s" # mauritanian tea
]

# Initialize CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")



# Assuming your custom module `RestaurantOrderSystem` and other functions are defined properly

class RestaurantApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # We initialize the MenuItem class
        self.menu_item = RestaurantOrderSystem()
        self.order_summary_popup = OrderSummaryPopup(self)

        self.title("Restaurant Order System")
        self.geometry("1200x800")

        self.selectedItems = []
        self.currentCostumer = None
        self.totalCost = 0 

        # Main Frames
        self.left_frame = ctk.CTkFrame(self, width=800, height=800)
        self.left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.right_frame = ctk.CTkFrame(self, width=400, height=800)
        self.right_frame.pack(side="right", fill="y", padx=10, pady=10)

        self.theme_button = ctk.CTkButton(
            self.left_frame,
            text="Change Theme",
            command=self.change_theme()
        )


        # Load UI Components
        self.create_menu_section()
        self.create_drink_section()
        self.create_basket_section()
        self.create_customer_section()
        self.create_change_theme_button()

    def create_menu_section(self):
        """Create the menu section."""
        self.menu_label = ctk.CTkLabel(self.left_frame, text="Menu", font=("Arial", 24))
        self.menu_label.pack(pady=10)

        self.menu_scroll_frame = ctk.CTkScrollableFrame(self.left_frame, width=750)
        self.menu_scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

        burgerNames = self.menu_item.burger_menu

        # Example placeholders for menu items
        for i in range(0, 10):  
            # Load default image
            self.default_image = self.load_default_image(True , None , (i + 1))

            item_frame = ctk.CTkFrame(self.menu_scroll_frame)
            item_frame.pack(fill="x", padx=5, pady=5)

            # Display image
            image_label = ctk.CTkLabel(item_frame, image=self.default_image, text="")
            image_label.pack(side="left", padx=10)

            # Display item title
            item_label = ctk.CTkLabel(item_frame, text=f"{burgerNames[i].name} {burgerNames[i].price}Tl", font=("Arial", 18))
            item_label.pack(side="left", padx=10)

            # Add-to-basket button
            add_button = ctk.CTkButton(item_frame, text="Add to Basket", command=lambda i=i: self.add_to_basket(burgerNames[i]))
            add_button.pack(side="right", padx=10)

    def create_drink_section(self):
        """Create the drink section."""
        self.drinks_label = ctk.CTkLabel(self.left_frame, text="Drinks", font=("Arial", 24))
        self.drinks_label.pack(pady=10)

        self.drinks_scroll_frame = ctk.CTkScrollableFrame(self.left_frame, width=750)
        self.drinks_scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

        drinksNames = self.menu_item.drink_menu

        # Example placeholders for drink items
        for i in range(len(drinks)):  # Use the length of drinks list for iteration
            self.default_Drink_image = self.load_default_image(False, drinks[i] , None)  # Pass the drink URL
            item_frame = ctk.CTkFrame(self.drinks_scroll_frame)
            item_frame.pack(fill="x", padx=5, pady=5)

            image_label = ctk.CTkLabel(item_frame, image=self.default_Drink_image, text="")
            image_label.pack(side="left", padx=10)

            item_label = ctk.CTkLabel(item_frame, text=f"{drinksNames[i].name } {drinksNames[i].price}Tl", font=("Arial", 18))
            item_label.pack(side="left", padx=10)

            add_button = ctk.CTkButton(item_frame, text="Add to Basket", command=lambda i=i: self.add_to_basket(drinksNames[i]))
            add_button.pack(side="right", padx=10)

    def create_basket_section(self):
        """Create the basket section."""
        self.basket_label = ctk.CTkLabel(self.right_frame, text="Basket", font=("Arial", 24))
        self.basket_label.pack(pady=10)

        self.basket_list = ctk.CTkTextbox(self.right_frame, width=350, height=400)
        self.basket_list.pack(pady=10)

        self.complete_button = ctk.CTkButton(self.right_frame, text="Complete Order", command=self.complete_order)
        self.complete_button.pack(pady=10)

    def create_customer_section(self):
        """Create the customer details section."""
        self.customer_label = ctk.CTkLabel(self.right_frame, text="Customer Details", font=("Arial", 24))
        self.customer_label.pack(pady=10)

        self.name_label = ctk.CTkLabel(self.right_frame, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = ctk.CTkEntry(self.right_frame, width=300)
        self.name_entry.pack(pady=5)

        self.budget_label = ctk.CTkLabel(self.right_frame, text="Budget:")
        self.budget_label.pack(pady=5)
        self.budget_entry = ctk.CTkEntry(self.right_frame, width=300)
        self.budget_entry.pack(pady=5)

        self.save_button = ctk.CTkButton(self.right_frame, text="Save Customer" ,command=self.save_customer)#, command=self.save_customer
        self.save_button.pack(pady=10)

    def load_default_image(self, food, url,i):
        if food:
            try:
                url = f"https://foodish-api.com/images/burger/burger{i}.jpg"
                image = Image.open(BytesIO(requests.get(url).content)).resize((70, 60))
                return ImageTk.PhotoImage(image)
            except Exception as e:
                print(f"Error loading image: {e}")

                return None
        else:
            try:
                image = Image.open(BytesIO(requests.get(url).content)).resize((70, 60))
                return ImageTk.PhotoImage(image)
            except Exception as e:
                print("Error loading the drink image line 152: ", e)
                return None
            

    def change_theme(self):
 
        current_theme = ctk.get_appearance_mode()
        if current_theme == "Dark":  
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")

    
    # Function to create the change theme button
    def create_change_theme_button(self):
        theme_button = ctk.CTkButton(self.left_frame, text="Change Theme", command=lambda: self.change_theme())
        theme_button.pack(side="top", padx=10, pady=10)  # Place button at the top of the left frame

    def add_to_basket(self, item):
        """Add an item to the basket."""

        if self.currentCostumer:
            if(DB.buy(self.currentCostumer , item.price)):
                if DB.UpdateMenu(item.name):
                    DB.UpdateMenu(item.name)
                    self.selectedItems.append(item.name)
                    self.basket_list.insert("end", f"{item.name}\n")
                    self.selectedItems.append(item.name)
                    self.totalCost += int(item.price)
                else:
                    messagebox.showinfo(f"{item.name} not available" , "please choose another item")

            else:
                messagebox.showwarning("insufficient budget")
        else:
            messagebox.showwarning("costumer not saved ", "please fill out the customer details")
        

    def complete_order(self):
        """Complete the current order."""
        if not self.currentCostumer:  # Check if customer is saved
            messagebox.showwarning("No Customer", "Please save customer details first!")
            return

        # Add the order summary to the popup
        self.order_summary_popup.add_customer_order(self.currentCostumer, self.selectedItems, self.totalCost)

        # Show the popup if it's hidden
        self.order_summary_popup.show_popup()

        # Clear the basket for the next order
        self.basket_list.delete("1.0", "end")
        self.selectedItems = []  # Clear the list of selected items
        self.totalCost = 0

    def save_customer(self):
        """Save customer details"""
        name = self.name_entry.get()
        budget = int(self.budget_entry.get())
        self.currentCostumer = name 
        
        if name and budget:
            if budget <= 500:
                messagebox.showinfo("user saved :",f" name: {name} budget:{budget}")
                if not DB.is_name_in_table(name): DB.addCustomer(name ,budget)
            else:
                messagebox.showwarning("the user budget"," canot exceed 500TL")
        else:
            messagebox.showwarning("Missing Info", "Please fill in all fields.")

# Run the application
if __name__ == "__main__":

    app = RestaurantApp()
    app.mainloop()

    while True :
        break


