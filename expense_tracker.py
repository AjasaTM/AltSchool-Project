import uuid
from datetime import datetime

# ----------------------------------------------
# 1. Define the Expense class
# ----------------------------------------------
class Expense:
    def __init__(self, title: str, amount: float):
        # Generate a unique ID for the expense
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        # Set timestamps to current UTC time
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at  # Initially same as created_at

    def update(self, new_title: str = None, new_amount: float = None):
        # Update title/amount if provided
        if new_title is None and new_amount is None:
            raise ValueError("You must provide at least one field to update (title or amount).")
        
        if new_title:
            self.title = new_title
        if new_amount:
            self.amount = new_amount
        
        # Update the timestamp
        self.updated_at = datetime.utcnow()

    def to_dict(self) -> dict:
        # Convert the expense to a dictionary (useful for JSON/saving)
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

# ----------------------------------------------
# 2. Define the ExpenseDatabase class
# ----------------------------------------------
class ExpenseDatabase:
    def __init__(self):
        self.expenses = []  # List to store expenses

    def add_expense(self, expense: Expense):
        # Add an expense to the database
        self.expenses.append(expense)

    def remove_expense(self, expense_id: str):
        # Remove an expense by its ID
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]

    def get_expense_by_id(self, expense_id: str) -> Expense | None:
        # Find an expense by ID (returns None if not found)
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expenses_by_title(self, title: str) -> list[Expense]:
        # Return all expenses with a matching title
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self) -> list[dict]:
        # Convert all expenses to dictionaries
        return [expense.to_dict() for expense in self.expenses]