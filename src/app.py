from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import uvicorn

# 1. Initialize the API
app = FastAPI(title="LeadPulse Scoring API")

# 2. Load the "Brain" (Model) and the "Columns" (Language) we saved
# This tells the API how to interpret the data
try:
    model = joblib.load('models/lead_model.pkl')
    model_columns = joblib.load('models/model_columns.pkl')
except:
    print("Error: Model files not found. Did you run train.py first?")

# 3. Define what a "Lead" looks like (Data Validation)
# If a user sends a string where a number should be, the API will catch the error.
class LeadInput(BaseModel):
    TotalVisits: float
    TotalTimeSpentOnWebsite: float 
    PageViewsPerVisit: float
    LeadOrigin: str
    LeadSource: str

@app.get("/")
def home():
    return {"status": "LeadPulse API is Online", "message": "Welcome to the Sales Scoring Engine"}

@app.post("/predict")
def predict(data: LeadInput):
    # Convert incoming data to a dictionary
    data_dict = data.dict()
    
    # Map the input names to the EXACT names the model learned in train.py
    input_data = {
        'TotalVisits': data_dict['TotalVisits'],
        'Total Time Spent on Website': data_dict['TotalTimeSpentOnWebsite'],
        'Page Views Per Visit': data_dict['PageViewsPerVisit'],
        'Lead Origin': data_dict['LeadOrigin'],
        'Lead Source': data_dict['LeadSource']
    }
    
    # Create a DataFrame for the model
    input_df = pd.DataFrame([input_data])
    
    # Preprocess: Turn text (Google, etc.) into numbers (1s and 0s)
    input_df = pd.get_dummies(input_df)
    
    # IMPORTANT: Align columns. 
    # If the input doesn't have a specific LeadSource, add it as a 0 so the model doesn't crash.
    for col in model_columns:
        if col not in input_df.columns:
            input_df[col] = 0
            
    # Make sure the columns are in the exact same order as they were during training
    input_df = input_df[model_columns]
    
    # 4. Get the Score (Probability of Conversion)
    probability = model.predict_proba(input_df)[0][1]
    score = round(probability * 100, 2)
    
    # Assign a Priority Label
    if score > 70:
        priority = "🔥 High (Hot Lead)"
    elif score > 35:
        priority = "⚡ Medium (Warm Lead)"
    else:
        priority = "❄️ Low (Cold Lead)"
    
    return {
        "lead_score": score,
        "priority": priority,
        "action": "Call within 10 minutes" if score > 70 else "Add to email sequence"
    }