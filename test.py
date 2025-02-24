from expense_tracker import Expense, ExpenseDatabase

# Create some expenses
groceries = Expense("Groceries", 50.0)
rent = Expense("Rent", 1500.0)

# Create a database and add expenses
db = ExpenseDatabase()
db.add_expense(groceries)
db.add_expense(rent)

# Update the groceries expense
groceries.update(new_title="Organic Groceries", new_amount=55.0)

# Print all expenses as dictionaries
print("All expenses:")
print(db.to_dict())

# Remove the rent expense
db.remove_expense(rent.id)

# Get an expense by ID
found_expense = db.get_expense_by_id(groceries.id)
print("\nFound expense by ID:")
print(found_expense.to_dict() if found_expense else "Not found")