# This is the Main file of  Student Expense Manager
#  mainly takes input from the user and calls the required functn.

from expense_manager import ExpenseManager
from report import show_summary, show_category_summary
from validation import get_valid_amount, get_valid_date, get_non_empty_text


# This function shows all the options to the user and its user choice to chose
def print_menu():
    print("\n" + "=" * 45)
    print("        STUDENT EXPENSE MANAGER")
    print("=" * 45)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. View Expense Summary")
    print("6. View Category-wise Summary")
    print("7. Exit")
    print("=" * 45)


# This function is used when the user wants to add a new expense
def add_expense(manager):
    print("\n--- ADD EXPENSE ---")

    # Taking date from the user
    date = get_valid_date()

    # Category can be something like Food, Travel, etc.
    category = get_non_empty_text("Category: ")

    # Small description of what the money was spent on
    description = get_non_empty_text("Description: ")

    # Taking the amount after checking that it is valid
    amount = get_valid_amount()

    # Sending all the details to ExpenseManager
    expense = manager.add_expense(date, category, description, amount)

    # Showing the ID given to the new expense
    print(f"\nExpense added successfully! ID: {expense['id']}")


# This function displays all the expenses saved in the file
def view_expenses(manager):
    expenses = manager.get_all_expenses()

    print("\n--- ALL EXPENSES ---")

    # If there are no expenses, there is nothing to display
    if not expenses:
        print("No expenses found.")
        return

    # Printing the headings in a simple table format
    print(f"{'ID':<5}{'Date':<13}{'Category':<15}{'Amount':>10}  Description")
    print("-" * 70)

    # Going through every expense one by one
    for e in expenses:
        print(f"{e['id']:<5}{e['date']:<13}{e['category']:<15}"
              f"₹{float(e['amount']):>8.2f}  {e['description']}")


# This function allows the user to change an old expense
def update_expense(manager):
    print("\n--- UPDATE EXPENSE ---")

    # First show the expenses so that the user can see their IDs
    view_expenses(manager)

    # If there are no expenses, we do not need to continue
    if not manager.get_all_expenses():
        return

    try:
        # Taking the ID of the expense that needs to be changed
        expense_id = int(input("\nEnter expense ID to update: "))
    except ValueError:
        # This happens if the user enters something other than a number
        print("Invalid ID.")
        return

    print("Enter new details:")

    # Taking the new values
    date = get_valid_date()
    category = get_non_empty_text("Category: ")
    description = get_non_empty_text("Description: ")
    amount = get_valid_amount()

    # Trying to update the expense using its ID
    if manager.update_expense(expense_id, date, category, description, amount):
        print("Expense updated successfully!")
    else:
        # This means the entered ID was not found
        print("Expense ID not found.")


# This function is used to remove an expense
def delete_expense(manager):
    print("\n--- DELETE EXPENSE ---")

    # Show the expenses first so the user can select an ID
    view_expenses(manager)

    # No need to delete anything if there are no expenses
    if not manager.get_all_expenses():
        return

    try:
        # Taking the ID of the expense to delete
        expense_id = int(input("\nEnter expense ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    # Calling the delete function
    if manager.delete_expense(expense_id):
        print("Expense deleted successfully!")
    else:
        print("Expense ID not found.")


# Main function of the program
def main():
    # Creating an object of ExpenseManager
    # This object will handle the expense-related work
    manager = ExpenseManager()

    # The menu keeps showing until the user chooses Exit
    while True:
        print_menu()

        # Taking the user's choice
        choice = input("Enter your choice (1-7): ").strip()

        # Calling the function according to the selected option
        if choice == "1":
            add_expense(manager)

        elif choice == "2":
            view_expenses(manager)

        elif choice == "3":
            update_expense(manager)

        elif choice == "4":
            delete_expense(manager)

        elif choice == "5":
            # Shows total and average expense
            show_summary(manager.get_all_expenses())

        elif choice == "6":
            # Shows how much money was spent in each category
            show_category_summary(manager.get_all_expenses())

        elif choice == "7":
            # Exit the program
            print("\nThank you for using Student Expense Manager!")
            break

        else:
            # Runs when the user enters a number outside 1-7
            print("Please choose a valid option.")


# This makes sure main() runs only when this file is directly executed
if __name__ == "__main__":
    main()
