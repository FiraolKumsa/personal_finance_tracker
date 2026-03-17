
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --- Set paths relative to this script ---
BASE_DIR = Path(__file__).resolve().parent.parent  # project root
DATA_DIR = BASE_DIR / "data"

INCOME_FILE = DATA_DIR / "income.csv"
EXPENSE_FILE = DATA_DIR / "expenses.csv"

# --- Read data ---
income = pd.read_csv(INCOME_FILE)
expenses = pd.read_csv(EXPENSE_FILE)

# --- Calculate salary ---
income["salary"] = income["hours_worked"] * income["hourly_rate"]

# --- Financial summary ---
total_salary = income["salary"].sum()
total_expenses = expenses["amount"].sum()
balance = total_salary - total_expenses

print("------ FINANCIAL SUMMARY ------")
print(f"Total Salary: {total_salary}")
print(f"Total Expenses: {total_expenses}")
print(f"Balance: {balance}\n")

# --- Expense by category ---
category_summary = expenses.groupby("category")["amount"].sum()
print("Expenses by Category:")
print(category_summary)

# --- Visualization ---
category_summary.plot(kind="bar")
plt.title("Expenses by Category")
plt.ylabel("Amount ($)")
plt.show()
