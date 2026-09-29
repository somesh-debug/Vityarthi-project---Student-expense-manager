import csv
from pathlib import Path

class Storage:
    """Reads and writes expense data using a CSV file."""

    FILE_PATH = Path(__file__).parent / "data" / "expenses.csv"
    FIELDS = ["id", "date", "category", "description", "amount"]

    def __init__(self):
        self.FILE_PATH.parent.mkdir(exist_ok=True)
        if not self.FILE_PATH.exists():
            self.save_expenses([])

    def load_expenses(self):
        try:
            with open(self.FILE_PATH, "r", newline="", encoding="utf-8") as file:
                return list(csv.DictReader(file))
        except (OSError, csv.Error):
            return []

    def save_expenses(self, expenses):
        with open(self.FILE_PATH, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.FIELDS)
            writer.writeheader()
            writer.writerows(expenses)
