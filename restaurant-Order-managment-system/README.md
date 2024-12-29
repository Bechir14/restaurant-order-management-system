# Restaurant Management System

## Overview

The **Restaurant Management System** is a robust application designed to streamline restaurant operations. It provides a seamless user experience through an intuitive GUI, efficient database management, and modular business logic. This system is ideal for managing menus, customer details, and order processing while ensuring scalability and ease of maintenance.

---

## Features

### GUI Components

1. **Menu Display**
   - Category-based item grouping.
   - Displays item details (image, name, price).
   - Real-time stock availability indicators.

2. **Basket Interface**
   - Dynamic item list with quantity adjustment.
   - Running total calculation.

3. **Customer Section**
   - Input fields for customer name and budget.
   - Save button to store customer details.

---

## Database Design

### 1. `menu` Table

Handles menu item data:
- **MenuItem**: Name/description of the item.
- **price**: Cost of the item.
- **availableQuantity**: Quantity in stock.

**Schema Definition:**
```python
def createMenuDB():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu(
            MenuItem TEXT,
            price INTEGER,
            availableQuantity INTEGER
        )
    """)
    con.commit()

```
2. customers Table
Stores customer information:

firstName: Customer's name.
budget: Customer's budget.
Schema Definition:

```python

def createCustomerDB():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers(
            firstName TEXT,
            budget INTEGER
        )
    """)
    con.commit()
```
System Flow
1. Order Lifecycle
The application handles the complete order lifecycle:

Customer Interaction: Input name and budget.
Menu Interaction: Add items to basket.
Validation: Checks for budget sufficiency and stock availability.
Completion: Finalize the order, update database records.
2. Validation Rules
Name must not be empty.
Budget must be a positive number.
Items must be in stock to add them to an order.
API Integration
The system uses the Foodish API to fetch food images dynamically. The images enhance the user experience by providing visual representations of menu items.

Image Loading Example:
```python

def load_default_image(self, food, url, i):
    try:
        url = f"https://foodish-api.com/images/burger/burger{i}.jpg"
        image = Image.open(BytesIO(requests.get(url).content)).resize((70, 60))
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image: {e}")
        return None
```
Class Interactions
Menu Class

Fetches and manages menu items.
Updates item quantities after order completion.
Customer Class

Manages customer information.
Updates budget after order completion.
Order Class

Tracks order items and calculates total cost.
Finalizes order and links it to the customer.
Example Workflow:


# Add items to menu
menu.add_item("Burger", 300, 10)

# Create customer
```python
customer = Customer()
customer.save_customer("Alice", 1000)
```

# Create order
```python
order = Order(order_id="ORD001")
order.add_item("Burger", 2, menu.get_item_details("Burger")["price"])
```

# Complete order
```python
if customer.budget >= order.calculate_total():
    order.complete_order()
    menu.update_quantity("Burger", -2)
    customer.update_budget(order.calculate_total())
    customer.add_order(order)
else:
    print("Insufficient budget!")
```
Error Handling
Error Type	System Response
Insufficient Budget	Warning popup with remaining budget.
Out of Stock	Disable "Add" button, show stock status.
Invalid Customer Data	Display form validation message.
Failed Transaction	Rollback changes, show error message.
Order Summary
The order summary interface displays:

Ordered items, quantities, and prices.
Total cost and remaining budget.
It features a dual-theme toggle for light/dark modes, providing a comfortable viewing experience.

Contribution Guide
Clone the repository:
```bash
git clone https://github.com/your-username/restaurant-management-system.git
```
Install dependencies:
```bash

pip install -r requirements.txt
```
Run the application:
```bash
python main.py
```
Feel free to fork the repository and submit pull requests for new features or bug fixes.

Future Enhancements
Add support for order history.
Implement online payment integration.
Expand API usage for additional menu images.

