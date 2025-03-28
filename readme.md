# Bankruptcy Predictor
This project provides a machine learning-powered credit risk prediction API that determines the likelihood of a customer declaring bankruptcy. The API is built using FastAPI, XGBoost, and Docker, with deployment on Google Cloud Run.

Features
1. Accepts CSV file input with financial data
2. Validates the file for required data
3. Makes a prediction using the XGBoost
4. Returns predictions in a Json format

Requirements.
1. Python==3.10+
2. FastApi
3. Pandas
4. XGBoost

Setup Instructions
1. Clone the repository
git clone https://github.com/Oluwasegun001100/Bankruptcy-prediction.git
cd Bankruptcy-prediction
2. Create a Virtual Environment & Install Dependencies
python -m venv venv
pip install -r requirements.txt

Usuage
1. Start the FastApi Server
2. Open your browser and navigate to http://127.0.0.1:8000.
3. Use the /predict endpoint to upload a CSV file and get predictions

CSV File Format
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

API Users 
1. Loan Officers and Banks - 
2. Data Scientists & Engineers - Extend and improve the model by fine-tuning hyperparameters or retraining on new datasets.
3. Developers & Fintech Companies - Integrate this API into financial applications to automate credit risk analysis.

Text Diagram
1. User uploads a CSV file containing the required financial data to the FastApi server using the predict endpoint
2. Server receives and validate the data againt the required features
3. If the CSV is valid, the server inputs the date to the model for prediction, if the file isn't valid the server raises the appropirate error.
4. The XGBoost mdoel returns the prediction to the FastApi server
5. The server sends the prediction in a Json format to the user

















