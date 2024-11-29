"""
Task:- 
Develop a personal finance tracker 
Objective:- 
Create an application that helps users manage their
income, expenses, and savings.
Features:- 
Input fields for tracking income, expenses, and categories (e.g., groceries, rent, entertainment).
Generate reports and charts to visualize spending patterns.
Set budget goals and track progress towards them.
Export data to a CSV file or visualize it using matplotlib
Technologies:-
Python, pandas for data management, matplotlib or seaborn for visualization,
and optionally sqlite3 for database storage.

"""

#_______________My_code_________________________________

import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt

# Initialize matplotlib for embedding in tkinter
plt.style.use('ggplot')

# DataFrame to store financial data
data = pd.DataFrame(columns=["Date", "Category", "Type", "Amount"])

# List of predefined categories for the dropdown
categories = ["Groceries", "Rent", "Entertainment", "Utilities", "Transportation", "Health", "Other"]

# Function to add a new record
def add_record():
    date = date_entry.get()
    category = category_combobox.get()  # Get the selected category from Combobox
    trans_type = trans_type_var.get()
    amount = amount_entry.get()
    
    if date and category and trans_type and amount:
        try:
            amount = float(amount)
            new_record = pd.DataFrame([[date, category, trans_type, amount]], columns=["Date", "Category", "Type", "Amount"])
            global data
            data = pd.concat([data, new_record], ignore_index=True)
            messagebox.showinfo("Success", "Record added successfully!")
            clear_entries()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for amount.")
    else:
        messagebox.showerror("Error", "All fields are required.")

# Function to clear entry fields
def clear_entries():
    date_entry.delete(0, tk.END)
    category_combobox.set('')  # Reset category dropdown
    amount_entry.delete(0, tk.END)
    trans_type_var.set("")  # Reset transaction type

# Function to visualize data
def show_report():
    if data.empty:
        messagebox.showinfo("No Data", "No records to display.")
        return

    data["Amount"] = pd.to_numeric(data["Amount"])
    plt.figure(figsize=(10, 6))
    data.groupby("Category")["Amount"].sum().plot(kind="bar", color='#6A0DAD')
    plt.title("Spending by Category", fontsize=16)
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.show()

# Function to export data to CSV
def export_data():
    if data.empty:
        messagebox.showinfo("No Data", "No records to export.")
        return

    file_path = "finance_data.csv"
    data.to_csv(file_path, index=False)
    messagebox.showinfo("Export Successful", f"Data exported to {file_path}.")

# Create the main application window
root = tk.Tk()
root.title("Personal Finance Tracker")
root.geometry("800x600")  # Adjust the window size
root.config(bg="#F0E68C")  # Background color

# Styling for labels and buttons
label_style = {'bg': "#F0E68C", 'font': ("Helvetica", 12, "bold")}
entry_style = {'font': ("Helvetica", 12), 'width': 30}  # Set width for uniformity

# Create a frame to hold all the widgets
frame = tk.Frame(root, bg="#F0E68C")
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Create labels and entry widgets
tk.Label(frame, text="Date (YYYY-MM-DD):", **label_style).grid(row=0, column=0, padx=10, pady=5, sticky="w")
date_entry = tk.Entry(frame, **entry_style)
date_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Category:", **label_style).grid(row=1, column=0, padx=10, pady=5, sticky="w")
category_combobox = ttk.Combobox(frame, values=categories, **entry_style)  # Dropdown for category
category_combobox.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Transaction Type:", **label_style).grid(row=2, column=0, padx=10, pady=5, sticky="w")
trans_type_var = tk.StringVar()
income_radio = ttk.Radiobutton(frame, text="Income", variable=trans_type_var, value="Income")
expense_radio = ttk.Radiobutton(frame, text="Expense", variable=trans_type_var, value="Expense")
income_radio.grid(row=2, column=1, padx=10, pady=5, sticky="w")
expense_radio.grid(row=2, column=1, padx=100, pady=5, sticky="w")

tk.Label(frame, text="Amount:", **label_style).grid(row=3, column=0, padx=10, pady=5, sticky="w")
amount_entry = tk.Entry(frame, **entry_style)
amount_entry.grid(row=3, column=1, padx=10, pady=5)

# Button styling
button_style = {'font': ("Helvetica", 12), 'bg': "#6A0DAD", 'fg': "white", 'width': 30}

# Create buttons and align them properly in a single column
add_button = tk.Button(frame, text="Add Record", command=add_record, **button_style)
add_button.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

# Change cursor to hand on hover
add_button.config(cursor="hand2")

report_button = tk.Button(frame, text="Show Report", command=show_report, **button_style)
report_button.grid(row=5, column=0, padx=10, pady=10, columnspan=2)
report_button.config(cursor="hand2")

export_button = tk.Button(frame, text="Export to CSV", command=export_data, **button_style)
export_button.grid(row=6, column=0, padx=10, pady=10, columnspan=2)
export_button.config(cursor="hand2")

clear_button = tk.Button(frame, text="Clear Entries", command=clear_entries, **button_style)
clear_button.grid(row=7, column=0, padx=10, pady=10, columnspan=2)
clear_button.config(cursor="hand2")

# Run the main event loop
root.mainloop()



