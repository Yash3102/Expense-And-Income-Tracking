import tkinter as tk
import matplotlib.pyplot as plt
import csv

expenses = []
budget = 0
incomes = []

def set_budget():
    global budget
    try:
        budget = float(budget_entry.get())
        budget_label.config(text=f"Budget set to ${budget:.2f}")
    except ValueError:
        budget_label.config(text="Invalid budget. Please enter a numeric value.")

def add_expense():
    global budget
    date = date_entry.get()
    description = description_entry.get()
    category = category_entry.get()

    try:
        amount = float(amount_entry.get())
    except ValueError:
        expense_label.config(text="Invalid amount. Please enter a numeric value.")
        return

    expenses.append([date, description, amount, category])
    budget -= amount

    if budget < 0:
        expense_label.config(text=f"Expense added successfully! You have exceeded your budget by ${abs(budget):.2f}.")
    else:
        expense_label.config(text=f"Expense added successfully! Remaining budget: ${budget:.2f}")

def add_income():
    global budget
    date = date_entry.get()
    description = description_entry.get()

    try:
        amount = float(amount_entry.get())
    except ValueError:
        income_label.config(text="Invalid amount. Please enter a numeric value.")
        return

    incomes.append([date, description, amount])
    budget += amount
    income_label.config(text=f"Income added successfully! Updated budget: ${budget:.2f}")

def view_expenses_and_incomes():
    if not expenses and not incomes:
        expense_label.config(text="No expenses or incomes to display.")
        return

    text = ""

    if expenses:
        text += "Expense List:\n"
        expenses.sort(key=lambda x: x[0])  # Sort by date
        for i, expense in enumerate(expenses, start=1):
            date, description, amount, category = expense
            text += f"{i}. Date: {date}, Description: {description}, Amount: ${amount:.2f}, Category: {category}\n"

    if incomes:
        text += "\nIncome List:\n"
        incomes.sort(key=lambda x: x[0])  # Sort by date
        for i, income in enumerate(incomes, start=1):
            date, description, amount = income
            text += f"{i}. Date: {date}, Description: {description}, Amount: ${amount:.2f}\n"

    expense_label.config(text=text)

    # Create a bar plot for expenses and incomes
    dates_expenses = [expense[0] for expense in expenses]
    amounts_expenses = [-expense[2] for expense in expenses]  # Use negative amounts for expenses
    dates_incomes = [income[0] for income in incomes]
    amounts_incomes = [income[2] for income in incomes]

    plt.figure(figsize=(10, 6))
    plt.bar(dates_expenses, amounts_expenses, label="Expenses", color="red")
    plt.bar(dates_incomes, amounts_incomes, label="Incomes", color="green")
    plt.title("Expense and Income Overview")
    plt.xlabel("Date")
    plt.ylabel("Amount ($)")
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

def save_expenses():
    with open("expenses.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        for expense in expenses:
            writer.writerow(expense)

# Create and configure the main tkinter window
root = tk.Tk()
root.title("Expense Tracker")

# Create and configure the budget input section
budget_label = tk.Label(root, text="Enter your budget for this month: $")
budget_label.pack()

budget_entry = tk.Entry(root)
budget_entry.pack()

budget_button = tk.Button(root, text="Set Budget", command=set_budget)
budget_button.pack()

# Create and configure the expense input section
date_label = tk.Label(root, text="Enter the date (YYYY-MM-DD):")
date_label.pack()

date_entry = tk.Entry(root)
date_entry.pack()

description_label = tk.Label(root, text="Enter a description:")
description_label.pack()

description_entry = tk.Entry(root)
description_entry.pack()

amount_label = tk.Label(root, text="Enter the amount:")
amount_label.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

category_label = tk.Label(root, text="Enter the category:")
category_label.pack()

category_entry = tk.Entry(root)
category_entry.pack()

expense_button = tk.Button(root, text="Add Expense", command=add_expense)
expense_button.pack()

# Create and configure the income input section
income_label = tk.Label(root, text="Enter an income:")
income_label.pack()

income_button = tk.Button(root, text="Add Income", command=add_income)
income_button.pack()

# Create and configure the view and save section
view_button = tk.Button(root, text="View Expenses and Incomes", command=view_expenses_and_incomes)
view_button.pack()

save_button = tk.Button(root, text="Save and Exit", command=save_expenses)
save_button.pack()

# Create a label for displaying expenses and incomes
expense_label = tk.Label(root, text="", wraplength=400)
expense_label.pack()

# Start the tkinter main loop
root.mainloop()
