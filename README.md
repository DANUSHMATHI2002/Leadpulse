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

To achieve high precision in lead scoring, we utilized a **Random Forest Ensemble**. This choice was strategic based on the nature of sales data:

* **Ensemble Logic:**
  The model constructs multiple decision trees during training and combines their outputs. It uses **Bagging (Bootstrap Aggregating)** to ensure no single noisy data point dominates predictions.

* **Handling Non-Linearity:**
  Web behavioral data (e.g., time spent vs. pages viewed) is highly non-linear. Random Forest effectively captures these relationships without requiring heavy feature engineering or scaling.

* **Feature Importance:**
  The model ranks features by their influence on prediction outcomes. This powers the **Behavioral Influence** chart in the dashboard.

---

### 🔄 The MLOps Framework: MLflow

We integrated MLflow to transform this project into a complete **Machine Learning Lifecycle system**:

1. **Experiment Tracking**

   * Logs hyperparameters such as `n_estimators` and `max_depth`
   * Tracks evaluation metrics: **Accuracy, Precision, Recall**

2. **Artifact Logging**

   * Stores trained `.pkl` models
   * Saves feature column schema for consistent inference

3. **Reproducibility**

   * Maintains a version-controlled record of experiments
   * Enables auditing and rollback of model versions

---

## 📈 Key Features

* ⚡ **Real-Time Lead Scoring**
  Instantly predicts conversion probability using the trained model

* 🗂️ **Audit Trail & Persistence**
  SQLite database logs every prediction for tracking and analysis

* 🔮 **What-If Simulation**
  Simulates how engagement improvements affect conversion likelihood

* 🎯 **Strategic Directives**
  Automatically categorizes leads:

  * **Hot Leads → Immediate Call**
  * **Cold Leads → Email Nurture**

---

## 📂 Project Structure

```
Leadpulse/
├── data/                  # Raw and processed datasets
├── models/
│   ├── lead_model.pkl     # Trained Random Forest model
│   └── model_columns.pkl  # Feature columns used for inference
├── src/
│   └── dashboard.py       # Streamlit application & SQLite logic
├── train.py               # MLflow training & experiment script
├── requirements.txt       # Project dependencies
├── LICENSE                # MIT License
└── README.md              # Project documentation
```

---

## 💻 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/DANUSHMATHI2002/Leadpulse.git
cd Leadpulse
```

---

### 2️⃣ Set Up Virtual Environment (Recommended)

#### 🪟 Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### 🍎 macOS / 🐧 Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🚀 How to Run

### 🧪 Step 1: Model Training

Run the training script to:

* Initialize MLflow experiment tracking
* Train the Random Forest model
* Save artifacts in the `/models` directory

```bash
python train.py
```

---

### 📊 Step 2: Launch the Dashboard

Start the interactive Streamlit application:

```bash
streamlit run src/dashboard.py
```

---

## 📊 Application Workflow

1. User inputs lead interaction data
2. Model processes features and predicts conversion probability
3. Lead is classified (Hot / Cold)
4. Recommendation is generated
5. Result is logged into SQLite database
6. Dashboard updates with insights and visualizations

---

## 📌 Future Enhancements

* 🔗 CRM Integration (Salesforce, HubSpot)
* ⚡ Real-time streaming data pipelines
* 🤖 AutoML for hyperparameter tuning
* 🔐 Role-based access control for dashboard
* ☁️ Cloud-native deployment (AWS/GCP/Azure)

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🤝 Contributing

Contributions are welcome!

Steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your fork
5. Open a Pull Request

---

## ⭐ Support

If you found this project useful, consider giving it a **star ⭐ on GitHub** — it helps increase visibility and supports the project!
