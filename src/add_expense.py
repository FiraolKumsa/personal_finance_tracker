import pandas as pd

date = input("Date (YYYY-MM-DD): ")
category = input("Category: ")
amount = float(input("Amount: "))

df = pd.DataFrame([[date,category,amount]],
columns=["date","category","amount"])

df.to_csv("data/expenses.csv",mode="a",header=False,index=False)

print("Expense added.")
