from storage import Storage
from datetime import datetime

class ExpenseManager:
    """Handles add, view, update and delete operations for expenses."""

    def __init__(self):
        self.storage = Storage()

    def get_all_expenses(self):
        return self.storage.load_expenses()

    def add_expense(self, date, category, description, amount):
        expenses = self.get_all_expenses()
        next_id = max([int(e["id"]) for e in expenses], default=0) + 1

        expense = {
            "id": str(next_id),
            "date": date,
            "category": category.title(),
            "description": description,
            "amount": f"{amount:.2f}"
        }

        expenses.append(expense)
        self.storage.save_expenses(expenses)
        return expense

    def update_expense(self, expense_id, date, category, description, amount):
        expenses = self.get_all_expenses()

        for expense in expenses:
            if int(expense["id"]) == expense_id:
                expense.update({
                    "date": date,
                    "category": category.title(),
                    "description": description,
                    "amount": f"{amount:.2f}"
                })
                self.storage.save_expenses(expenses)
                return True

        return False

    def delete_expense(self, expense_id):
        expenses = self.get_all_expenses()
        updated = [e for e in expenses if int(e["id"]) != expense_id]

        if len(updated) == len(expenses):
            return False

        self.storage.save_expenses(updated)
        return True
