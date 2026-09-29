from collections import defaultdict

def total_expense(expenses):
    return sum(float(e["amount"]) for e in expenses)

def average_expense(expenses):
    if not expenses:
        return 0
    return total_expense(expenses) / len(expenses)

def category_totals(expenses):
    totals = defaultdict(float)
    for expense in expenses:
        totals[expense["category"]] += float(expense["amount"])
    return dict(sorted(totals.items()))
