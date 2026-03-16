import pandas as pd

income = pd.read_csv("../data/income.csv")
expenses = pd.read_csv("../data/expenses.csv")

income["salary"] = income["hours_worked"] * income["hourly_rate"]

total_salary = income["salary"].sum()
total_expense = expenses["amount"].sum()

balance = total_salary - total_expense

category_summary = expenses.groupby("category")["amount"].sum()

print("Total Salary:", total_salary)
print("Total Expenses:", total_expense)
print("Balance:", balance)

print("\nExpenses by Category")
print(category_summary)

report = pd.DataFrame({
"salary":[total_salary],
"expenses":[total_expense],
"balance":[balance]
})

report.to_csv("reports/monthly_report.csv",index=False)

# --- Visualization ---
import matplotlib.pyplot as plt

category_summary.plot(kind="bar")

plt.title("Expenses by Category")
plt.ylabel("Amount ($)")
plt.xlabel("Category")

plt.show()
