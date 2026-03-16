import pandas as pd

date = input("Date (YYYY-MM-DD): ")
hours = float(input("Hours worked: "))
rate = float(input("Hourly rate: "))

df = pd.DataFrame([[date,hours,rate]],
columns=["date","hours_worked","hourly_rate"])

df.to_csv("data/income.csv",mode="a",header=False,index=False)

print("Income added.")
