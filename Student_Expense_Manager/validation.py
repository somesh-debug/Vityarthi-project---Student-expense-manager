from datetime import datetime

def get_valid_amount():
    while True:
        value = input("Amount (₹): ").strip()
        try:
            amount = float(value)
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")

def get_valid_date():
    while True:
        value = input("Date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Please use the format YYYY-MM-DD.")

def get_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")
