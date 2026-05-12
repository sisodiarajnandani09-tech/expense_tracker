from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

transactions=[] #fakedatabase

class Transaction(BaseModel):
    type: str #income or expense
    amount: float
    category: str
    month: str #May
    
    
#add transaction
@app.post("/transactions")
def add_transaction(transaction: Transaction):
    transactions.append(transaction)
    return {
        "message": "Transaction added successfully"
    }
    
#get  all transactions
@app.get("/transactions")
def get_transactions():
    return transactions

#Balance Calculation
@app.get("/balance")
def get_balance():
    income = sum(
    t.amount for t in transactions if t.type == "income"
)

    expense = sum(
        t.amount for t in transactions if t.type == "expense"
    )

    balance = income - expense

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": balance
    }
    
# Monthly Summary
@app.get("/monthly/{month}")
def monthly_summary(month: str):
    monthly_data = [
        t for t in transactions if t.month.lower() == month.lower()
    ]

    total = sum(t.amount for t in monthly_data)

    return {
        "month": month,
        "transactions": monthly_data,
        "total": total
    }
    
# Category Filter
@app.get("/category/{category}")
def category_filter(category: str):
    filtered = [
        t.dict()
        for t in transactions
        if t.category.lower() == category.lower()
    ]

    return {
        "category": category,
        "transactions": filtered
    }
