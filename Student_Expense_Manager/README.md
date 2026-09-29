# Student Expense Manager

## 1. Project Overview
Student Expense Manager is a simple Python-based application designed to help college students record, manage and analyze their daily expenses.

The application provides an easy menu-driven interface. Users can add, view, update and delete expenses. It also calculates total and average spending and provides a category-wise summary.

## 2. Features
- Add a new expense
- View all expenses
- Update an existing expense
- Delete an expense
- Calculate total and average expense
- View category-wise expense summary
- Validate user input
- Store data permanently in a CSV file
- Handle invalid input without crashing

## 3. Technologies Used
- Python 3
- CSV file storage
- Python unittest
- Git and GitHub

No external Python packages are required.

## 4. Project Structure
```text
Student_Expense_Manager/
├── main.py
├── expense_manager.py
├── storage.py
├── validation.py
├── calculations.py
├── report.py
├── README.md
├── statement.md
├── requirements.txt
├── data/
│   └── expenses.csv
├── tests/
│   └── test_project.py
└── docs/
    └── diagrams/
```

## 5. How to Run
1. Install Python 3.
2. Open the project folder in VS Code or a terminal.
3. Run:
```bash
python main.py
```
4. Follow the menu shown on the screen.

## 6. How to Test
Run:
```bash
python -m unittest discover -s tests -v
```

## 7. Data Storage
Expense records are stored in `data/expenses.csv`.

## 8. Error Handling
The application checks:
- invalid amount
- negative or zero amount
- incorrect date format
- empty text fields
- invalid menu choices
- invalid expense IDs

## 9. Future Enhancements
- Monthly budget tracking
- Graphical charts
- Login system
- Export reports to PDF
- SQLite database
- Web-based interface
