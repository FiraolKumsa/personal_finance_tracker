import streamlit as st
import pandas as pd
from pathlib import Path

# --- Paths ---
BASE_DIR = Path(__file__).resolve().parent.parent  # project root
DATA_DIR = BASE_DIR / "data"

INCOME_FILE = DATA_DIR / "income.csv"
EXPENSE_FILE = DATA_DIR / "expenses.csv"

# --- Load data ---
income = pd.read_csv(INCOME_FILE)
expenses = pd.read_csv(EXPENSE_FILE)

income["salary"] = income["hours_worked"] * income["hourly_rate"]

total_salary = income["salary"].sum()
total_expenses = expenses["amount"].sum()
balance = total_salary - total_expenses

# --- Streamlit UI ---
st.title("💰 Personal Finance Dashboard")

st.metric("Total Salary", total_salary)
st.metric("Total Expenses", total_expenses)
st.metric("Balance", balance)

category_summary = expenses.groupby("category")["amount"].sum()
st.bar_chart(category_summary)
