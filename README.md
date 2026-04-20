# 🎯 LeadPulse: Strategic Sales Intelligence

**Developers:** Danushmathi Pathmanaban & Srivarshan Meiprakash  
**Project Type:** End-to-End MLOps & Predictive Analytics    
**Deployment:** Streamlit Community Cloud  

---

## 🚀 Project Overview

LeadPulse is a full-stack Machine Learning application designed to prioritize sales leads using predictive analytics. By analyzing historical interaction data, the system identifies **"Hot Leads"** with a high probability of conversion.

This enables sales teams to:

* Focus on high-value opportunities
* Optimize workflow efficiency
* Maximize ROI through data-driven decision-making

---

## 🛠️ Tech Stack

* **Machine Learning:** Random Forest Classifier (Scikit-Learn)
* **MLOps:** MLflow (Experiment tracking & Model versioning)
* **Frontend:** Streamlit & Plotly (Interactive UI)
* **Database:** SQLite (Persistent Lead Audit Trail)
* **Environment:** Python 3.11

---

## 🧠 Technical Deep-Dive

### 🌲 The Algorithm: Random Forest Classifier

To achieve high precision in lead scoring, we utilized a **Random Forest Ensemble**:

* Ensemble of decision trees using Bagging
* Handles non-linear behavioral patterns
* Provides feature importance for insights

---

### 🔄 The MLOps Framework: MLflow

We integrated MLflow to transform this project into a complete Machine Learning lifecycle system:

* Experiment tracking
* Artifact storage
* Model reproducibility

---

## 🏗️ MLOps Lifecycle: MLflow Integration

To move beyond "Notebook-based" development, this project utilizes **MLflow** to manage the end-to-end Machine Learning lifecycle. This ensures that every model deployed to the dashboard is reproducible and scientifically tracked.

### 1. Experiment Tracking

Every training run is captured in the MLflow tracking server. We log:

* **Hyperparameters:** `n_estimators`, `max_depth`, `min_samples_split`
* **Performance Metrics:** Accuracy, Precision, Recall, F1-Score
* **System Metadata:** Execution time, user credentials, and git commit hashes

### 2. Artifact Logging & Model Versioning

Instead of manually moving files, MLflow automatically packages:

* Serialized **Random Forest model** (`.pkl`)
* **Environment dependencies** for reproducibility
* **Feature signatures** to ensure correct input structure

### 3. Reproducibility & Governance

MLflow maintains a complete audit trail of experiments:

* Compare multiple model versions
* Track improvements over time
* Roll back to best-performing models easily

---

## 🛠️ How to View the MLflow Dashboard

If running locally:

```bash
mlflow ui
```

Then open:

```
http://localhost:5000
```

---

## 📈 Key Features

* ⚡ Real-Time Lead Scoring
* 🗂️ SQLite Audit Trail
* 🔮 What-If Simulation
* 🎯 Strategic Lead Classification

---

## 📂 Project Structure

```
Leadpulse/
├── data/
├── models/
│   ├── lead_model.pkl
│   └── model_columns.pkl
├── src/
│   └── dashboard.py
├── train.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 💻 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/DANUSHMATHI2002/Leadpulse.git
cd Leadpulse
```

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🚀 How to Run

### Train Model

```bash
python train.py
```

### Run Dashboard

```bash
streamlit run src/dashboard.py
```

---

## 📌 Future Enhancements

* CRM integrations
* Real-time pipelines
* AutoML tuning
* Role-based dashboards

---

## 📜 License

MIT License

---

## 🤝 Contributing

```bash
git add README.md
git commit -m "Added MLOps and MLflow lifecycle documentation"
git push
```

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub!
