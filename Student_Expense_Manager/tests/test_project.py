import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch

import storage
from expense_manager import ExpenseManager
from calculations import total_expense, average_expense, category_totals

class TestStudentExpenseManager(unittest.TestCase):

    def setUp(self):
        self.temp_file = Path(tempfile.mktemp(suffix=".csv"))
        self.original_path = storage.Storage.FILE_PATH
        storage.Storage.FILE_PATH = self.temp_file
        self.manager = ExpenseManager()

    def tearDown(self):
        storage.Storage.FILE_PATH = self.original_path
        if self.temp_file.exists():
            self.temp_file.unlink()

    def test_add_expense(self):
        expense = self.manager.add_expense(
            "2026-09-28", "Food", "Dinner", 250
        )
        self.assertEqual(expense["id"], "1")
        self.assertEqual(len(self.manager.get_all_expenses()), 1)

    def test_update_expense(self):
        self.manager.add_expense("2026-09-28", "Food", "Dinner", 250)
        result = self.manager.update_expense(
            1, "2026-09-29", "Travel", "Bus", 80
        )
        self.assertTrue(result)
        self.assertEqual(self.manager.get_all_expenses()[0]["category"], "Travel")

    def test_delete_expense(self):
        self.manager.add_expense("2026-09-28", "Food", "Dinner", 250)
        self.assertTrue(self.manager.delete_expense(1))
        self.assertEqual(len(self.manager.get_all_expenses()), 0)

    def test_calculations(self):
        expenses = [
            {"amount": "100", "category": "Food"},
            {"amount": "200", "category": "Travel"},
            {"amount": "300", "category": "Food"}
        ]
        self.assertEqual(total_expense(expenses), 600)
        self.assertEqual(average_expense(expenses), 200)
        self.assertEqual(category_totals(expenses)["Food"], 400)

if __name__ == "__main__":
    unittest.main()
