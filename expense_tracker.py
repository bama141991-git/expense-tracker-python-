import json
from datetime import datetime
import os

DATA_FILE = "expenses.json"

def load_expenses():
    """Load expenses from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_expenses(expenses):
    """Save expenses to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    """Add a new expense entry."""
    category = input("Enter category (food, travel, shopping, bills, etc): ")
    amount = float(input("Enter amount: "))
    note = input("Enter a short note (optional): ")

    expense = {
        "category": category,
        "amount": amount,
        "note": note,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    print("\nExpense added successfully!\n")

def view_expenses():
    """View all expenses."""
    expenses = load_expenses()

    if not expenses:
        print("\nNo expenses recorded yet.\n")
        return

    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['category']} - £{exp['amount']} - {exp['note']} ({exp['date']})")
    print()

def total_expenses():
    """Calculate the total of all expenses."""
    expenses = load_expenses()
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal expenses: £{total:.2f}\n")

def main():
    print("\n=== Personal Expense Tracker ===")

    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Amount Spent")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice! Try again.\n")

if __name__ == "__main__":
    main()
