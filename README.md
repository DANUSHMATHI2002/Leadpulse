# 🎯 LeadPulse: Strategic Sales Intelligence

**Developer:** Danushmathi Pathmanaban  
**Project Type:** End-to-End MLOps & Predictive Analytics  
**Deployment:** Streamlit Community Cloud

## 🚀 Project Overview
LeadPulse is a full-stack Machine Learning application designed to prioritize sales leads using predictive analytics. By analyzing historical interaction data, the system identifies "Hot Leads" with a high probability of conversion, allowing sales teams to optimize their workflow and focus human effort where it generates the highest ROI.

## 🛠️ Tech Stack
- **Machine Learning:** Random Forest Classifier (Scikit-Learn)
- **MLOps:** MLflow (Experiment tracking & Model versioning)
- **Frontend:** Streamlit & Plotly (Interactive UI)
- **Database:** SQLite (Persistent Lead Audit Trail)
- **Environment:** Python 3.11

---

## 🧠 Technical Deep-Dive

### The Algorithm: Random Forest Classifier
To achieve high precision in lead scoring, I utilized a **Random Forest Ensemble**. This choice was strategic based on the nature of sales data:
- **Ensemble Logic:** The model constructs an array of decision trees during training. It uses **Bagging (Bootstrap Aggregating)** to ensure that no single outlier or noisy data point can skew the prediction.
- **Handling Non-Linearity:** Web behavioral data (time spent vs. pages viewed) rarely follows a straight line. Random Forest effectively captures these complex, non-linear relationships without requiring extensive feature scaling.
- **Feature Importance:** One of the core strengths of this model is its ability to rank which behaviors (e.g., "Total Time Spent") most strongly correlate with a sale. This powers the "Behavioral Influence" chart in the dashboard.

### The MLOps Framework: MLflow
I integrated **MLflow** to move the project from a "static script" to a professional **Machine Learning Lifecycle**:
1. **Experiment Tracking:** I logged every training run with specific hyperparameters (like `n_estimators` and `max_depth`) alongside metrics like **Accuracy, Precision, and Recall**. This ensured that the "Golden Model" deployed was statistically the best performer.
2. **Artifact Logging:** Automated the storage of the trained `.pkl` models and feature column signatures. This creates a bridge between the training environment and the production dashboard, preventing "Dependency Hell."
3. **Reproducibility:** By using MLflow, I maintained a technical "Lab Notebook" of the model's evolution, allowing for seamless auditing and the ability to roll back to previous versions if needed.

---

## 📈 Key Features
- **Real-Time Lead Scoring:** Dynamic probability calculation using the trained Random Forest model.
- **Audit Trail & Persistence:** Integrated SQLite backend to log every prediction, allowing managers to track sales performance over time.
- **What-If Simulation:** An interactive optimizer that allows users to simulate how increasing engagement (e.g., 25% more time on site) impacts the conversion score.
- **Strategic Directives:** The system automatically categorizes leads (Hot/Cold) and provides recommended actions (Immediate Call vs. Email Nurture) via a high-contrast visual interface.

---

## 🏁 Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/DANUSHMATHI2002/Leadpulse.git](https://github.com/DANUSHMATHI2002/Leadpulse.git)
cd Leadpulse


*This project was developed as part of a Master's portfolio to demonstrate end-to-end ML lifecycle management (MLOps), from data preprocessing to cloud deployment.*
