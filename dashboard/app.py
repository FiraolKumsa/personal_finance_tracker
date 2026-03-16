import streamlit as st
import pandas as pd

income = pd.read_csv("data/income.csv")
expenses = pd.read_csv("data/expenses.csv")

income["salary"] = income["hours_worked"] * income["hourly_rate"]

total_salary = income["salary"].sum()
total_expense = expenses["amount"].sum()

balance = total_salary - total_expense

st.title("Personal Finance Dashboard")

st.metric("Total Salary", total_salary)
st.metric("Total Expenses", total_expense)
st.metric("Balance", balance)

st.subheader("Expenses by Category")

category_summary = expenses.groupby("category")["amount"].sum()

st.bar_chart(category_summary)
