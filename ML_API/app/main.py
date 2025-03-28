from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd 
import io
from typing import List
from pydantic import BaseModel, ValidationError
from xgboost import XGBClassifier

app = FastAPI()


final_features = [
    "Quick Ratio", 
    "Allocation rate per person",
    "Continuous Net Profit Growth Rate",
    "Total debt/Total net worth",
    "Accounts Receivable Turnover",
    "Fixed Assets to Assets",
    "Interest Expense Ratio",
    "Interest-bearing debt interest rate",
    "Working capitcal Turnover Rate",
    "Research and development expense rate",
    "Persistent EPS in the Last Four Seasons",
    "ROA(B) before interest and depreciation after tax",
    "Borrowing dependency", 
    "Revenue per person",
    "Total Asset Growth Rate", 
    "Net Value Growth Rate",
    "ROA(C) before interest and depreciation before interest",
    "Operating profit per person", 
    "Cash/Current Liability",
    "Current Liabilities/Equity", 
    "Cash Turnover Rate",
    "Total assets to GNP price", 
    "After-tax Net Profit Growth Rate",
    "Inventory Turnover Rate (times)", 
    "Quick Assets/Total Assets",
    "Non-industry income and expenditure/revenue",
    "Retained Earnings to Total Assets", 
    "Total expense/Assets",
    "Current Liability to Assets",
    "Cash Flow to Equity"
]


model = XGBClassifier()
model.load_model("model.json")

# we define input schema
class InputData(BaseModel):
    predictions: List[int]


@app.get("/")
async def root():
    return {"Message": "Welcome to ML_API"}


@app.post("/predict/", response_model=InputData)
async def predict(file: UploadFile = File(...)):
    try:
        """Make a prediction based on the input data"""
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

        missing = set(final_features) - set(df.columns)
        if missing:
            raise HTTPException(status_code=400, detail=f"Missing columns in CSV: {missing}")

        df_final = df[final_features]

        if df_final.empty:
            raise HTTPException(status_code=400, detail="Uploaded CSV is empty or missing required data.")

        predictions = model.predict(df_final)

        return {"predictions": predictions.tolist()}
    
    except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    
    