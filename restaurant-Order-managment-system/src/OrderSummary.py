from tkinter import Toplevel, Text
import customtkinter as ctk

class OrderSummaryPopup:
    def __init__(self, parent=None):
        """
        Initialize the OrderSummaryPopup class.
        """
        self.popup = None
        self.text_widget = None
        self.parent = parent

    def show(self):
        """Create and display the popup window if it doesn't already exist."""
        if self.popup is None or not self.popup.winfo_exists():
            self.popup = Toplevel(self.parent)
            self.popup.title("Order Summary")
            self.popup.geometry("600x400")
            
            # Create the text widget to display the order summary
            self.text_widget = Text(self.popup, wrap="word", font=("Arial", 12), height=20, width=50)
            self.text_widget.pack(fill="both", expand=True, padx=10, pady=10)
            
            # Close button for the popup
            close_button = ctk.CTkButton(self.popup, text="Close", command=self.hide_popup)
            close_button.pack(pady=10)

    def hide_popup(self):
        """Hide the popup without destroying it."""
        if self.popup:
            self.popup.withdraw()  # Hide the popup

    def show_popup(self):
        """Bring the popup back if it was hidden."""
        if self.popup:
            self.popup.deiconify()  # Show the popup again

    def add_customer_order(self, customer_name, items, total_paid):
        """Add a customer's order to the summary."""
        if self.text_widget is None:
            self.show()  # Ensure the popup and text widget are created
        
        # Format the order summary and add it to the text widget
        order_summary = (
            f"Customer {customer_name} : {', '.join(items)}\n"
            f"Customer Total: Paid {total_paid} TL\n\n"
        )
        
        # Insert the order summary at the end of the text widget
        self.text_widget.insert("end", order_summary)
        self.text_widget.yview("end")  # Scroll to the bottom