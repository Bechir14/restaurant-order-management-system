# 🍔 Burger Shop Classes Documentation  

This README provides details about the `User` and `Menu` classes implemented in Python. These classes are designed for managing user budgets and a burger menu system.  

---

## 👤 User Class  

### Attributes  
- **`name`**: The name of the user will be provided during object creation.  
- **`budget`**: The user's budget, also set during object creation.  

### Methods  
- **`buy(total_amount)`**  
  - **Purpose**: Checks if the user's budget is sufficient for the given order amount. If successful, deducts the total amount from the budget.  
  - **Parameters**: `total_amount` (int or float): The total cost of the order.  
  - **Returns**: `True` if the purchase is successful, `False` otherwise.  
  - **Return Type**: `bool`  

- **`get_user_name()`**  
  - **Purpose**: Returns the name of the user.  
  - **Return Type**: `str`  

- **`get_user_budget()`**  
  - **Purpose**: Retrieves the user's current budget.  
  - **Return Type**: `int` or `float`  

---

## 📋 Menu Class  

### Attributes  
- **`items`**: A list of strings, each representing a burger name along with its price (e.g., `"Cheeseburger - $5.99"`).  
- **`prices`**: A separate list of numbers (int or float), representing the prices of the items in the same order as in the `items` list.  

---


