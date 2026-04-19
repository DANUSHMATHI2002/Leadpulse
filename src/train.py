import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import mlflow
import mlflow.sklearn

def train_professional_model():
    # 1. Load the real data
    df = pd.read_csv('data/leads.csv')

    # 2. DATA CLEANING (The "Professional" Touch)
    # The 'Select' value in this dataset is basically a Null. Let's fix that.
    df = df.replace('Select', np.nan)
    
    # Drop columns with too many missing values (more than 40%)
    limit = len(df) * 0.6
    df = df.dropna(thresh=limit, axis=1)

    # For this version, let's pick the most important features
    features = ['TotalVisits', 'Total Time Spent on Website', 'Page Views Per Visit', 'Lead Origin', 'Lead Source']
    target = 'Converted'
    
    # Keep only what we need and drop rows with missing values in these specific columns
    df = df[features + [target]].dropna()

    # 3. ENCODING
    # Convert text categories into numbers so the model can read them
    X = df[features]
    y = df[target]
    
    # Simple way for the API: Get Dummies (One-Hot Encoding)
    X = pd.get_dummies(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. MLFLOW EXPERIMENT TRACKING
    mlflow.set_experiment("LeadPulse_Sales_Scoring")

    with mlflow.start_run():
        # Define Model Parameters
        n_estimators = 100
        max_depth = 7
        
        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        model.fit(X_train, y_train)

        # Calculate Metrics
        accuracy = model.score(X_test, y_test)
        
        # Log to MLFlow (This creates the "Innovation" on your resume)
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.sklearn.log_model(model, "random_forest_model")

        print(f"✅ Model trained with Accuracy: {accuracy:.2%}")

        # 5. SAVE FOR PRODUCTION
        joblib.dump(model, 'models/lead_model.pkl')
        # Save the column names so our API knows the order of 1s and 0s
        joblib.dump(X.columns.tolist(), 'models/model_columns.pkl')
        print("✅ Production artifacts saved to /models")

if __name__ == "__main__":
    train_professional_model()