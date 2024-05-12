import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from PIL import Image, ImageTk

class BakeryOrderManagement:
    def __init__(self):
        self.orders = pd.DataFrame(columns=["Customer Name", "Item", "Quantity", "Order Date"])

    def add_order(self):
        customer_name = self.customer_name_entry.get()
        item = self.item_entry.get()
        quantity = int(self.quantity_entry.get())
        order_date = datetime.now().strftime("%Y-%m-%d")
        new_order = pd.DataFrame([[customer_name, item, quantity, order_date]],
                                 columns=["Customer Name", "Item", "Quantity", "Order Date"])
        self.orders = pd.concat([self.orders, new_order], ignore_index=True)
        self.result_label.config(text="Order added successfully!")

    def view_orders(self):
        if self.orders.empty:
            self.result_label.config(text="No orders available.")
        else:
            self.result_label.config(text=str(self.orders))

    def update_order(self):
        order_id = int(self.order_id_entry.get())
        if order_id >= len(self.orders):
            self.result_label.config(text="Order not found.")
        else:
            self.result_label.config(text="Updating Order ID: {}".format(order_id))
            self.orders.at[order_id, "Item"] = self.new_item_entry.get()
            self.orders.at[order_id, "Quantity"] = int(self.new_quantity_entry.get())
            self.result_label.config(text="Order updated successfully!")

    def save_to_excel(self):
        try:
            self.orders.to_excel("bakery_orders.xlsx", index=False)
            self.result_label.config(text="Orders saved to 'bakery_orders.xlsx'.")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")

    def create_ui(self):
        self.root = tk.Tk()
        self.root.title("Bakery Order Management")

        # Set background image
        # bg_image = ImageTk.PhotoImage(Image.open("bakery-background.jpg"))
        # bg_label = tk.Label(self.root, image=bg_image)
        # bg_label.place(relwidth=1, relheight=1)

        # Add styled frames
        order_frame = ttk.Frame(self.root, padding=20, relief="groove")
        order_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        

        # Labels with custom font
        heading_font = Font(family="Brush Script MT", size=18)
        ttk.Label(order_frame, text="Welcome to the Bakery!", font=heading_font).grid(row=1, column=0, pady=10)

        ttk.Separator(order_frame, orient=tk.HORIZONTAL).grid(row=2, column=0, columnspan=2, sticky="ew", pady=10)

        # Entry fields and buttons for order management
        ttk.Label(order_frame, text="Enter customer name:").grid(row=3, column=0, sticky=tk.W)
        self.customer_name_entry = ttk.Entry(order_frame)
        self.customer_name_entry.grid(row=3, column=1, pady=5)

        ttk.Label(order_frame, text="Enter item ordered:").grid(row=4, column=0, sticky=tk.W)
        self.item_entry = ttk.Entry(order_frame)
        self.item_entry.grid(row=4, column=1, pady=5)

        ttk.Label(order_frame, text="Enter quantity:").grid(row=5, column=0, sticky=tk.W)
        self.quantity_entry = ttk.Entry(order_frame)
        self.quantity_entry.grid(row=5, column=1, pady=5)

        # Buttons with images
        # add_icon = ImageTk.PhotoImage(Image.open("add.png"))
        ttk.Button(order_frame, text="Add Order", command=self.add_order).grid(row=6, column=0, pady=10)

        ttk.Button(order_frame, text="View Orders", command=self.view_orders).grid(row=6, column=1, columnspan=1, pady=10)

        ttk.Label(order_frame, text="Enter order ID to update:").grid(row=7, column=0, sticky=tk.W)
        self.order_id_entry = ttk.Entry(order_frame)
        self.order_id_entry.grid(row=7, column=1, pady=5)

        ttk.Label(order_frame, text="Enter new item:").grid(row=8, column=0, sticky=tk.W)
        self.new_item_entry = ttk.Entry(order_frame)
        self.new_item_entry.grid(row=8, column=1, pady=5)

        ttk.Label(order_frame, text="Enter new quantity:").grid(row=9, column=0, sticky=tk.W)
        self.new_quantity_entry = ttk.Entry(order_frame)
        self.new_quantity_entry.grid(row=9, column=1, pady=5)

        ttk.Button(order_frame, text="Update Order", command=self.update_order).grid(row=10, column=0, columnspan=2, pady=10)

        ttk.Separator(order_frame, orient=tk.HORIZONTAL).grid(row=11, column=0, columnspan=2, sticky="ew", pady=10)

        ttk.Button(order_frame, text="Save to Excel", command=self.save_to_excel).grid(row=12, column=0, columnspan=2, pady=10)

        ttk.Separator(order_frame, orient=tk.HORIZONTAL).grid(row=13, column=0, columnspan=2, sticky="ew", pady=10)

        ttk.Button(order_frame, text="Exit", command=self.root.destroy).grid(row=14, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(order_frame, text="")
        self.result_label.grid(row=15, column=0, columnspan=2, pady=10)

        self.root.mainloop()

if __name__ == "__main__":
    order_system = BakeryOrderManagement()
    order_system.create_ui()
