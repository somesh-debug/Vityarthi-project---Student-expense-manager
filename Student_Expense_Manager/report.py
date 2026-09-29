from calculations import total_expense, average_expense, category_totals

def show_summary(expenses):
    print("\n--- EXPENSE SUMMARY ---")
    if not expenses:
        print("No expenses available for analysis.")
        return

    print(f"Number of expenses : {len(expenses)}")
    print(f"Total expense     : ₹{total_expense(expenses):.2f}")
    print(f"Average expense   : ₹{average_expense(expenses):.2f}")

def show_category_summary(expenses):
    print("\n--- CATEGORY-WISE SUMMARY ---")
    totals = category_totals(expenses)

    if not totals:
        print("No expenses available for analysis.")
        return

    for category, amount in totals.items():
        print(f"{category:<20} ₹{amount:.2f}")
