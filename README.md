# ☁️ Cloud Cost Prediction using Machine Learning

A powerful and lightweight machine learning model that predicts **cloud infrastructure cost** based on key resource inputs: CPU, memory, and storage. This helps teams estimate spend **before** provisioning resources — enabling **better cost control and planning**.

---

## 🧠 Overview

Cloud services offer unmatched scalability and flexibility — but without cost control, they can become **financially inefficient**. Organizations often struggle to anticipate the future costs of their workloads, leading to unexpected billing surprises.

This project builds an end-to-end ML pipeline that:

- Ingests structured infrastructure usage data
- Trains a regression model to predict cloud cost
- Serves the model via a REST API using FastAPI
- Provides real-time cost estimates

It helps developers, architects, and cloud teams make **data-driven financial decisions** on their resource provisioning.

---

## ❓ Problem Statement

Cloud providers like AWS, GCP, and Azure provide billing dashboards and cost estimators, but:

- They are **reactive**: You see costs after consumption
- They are **manual**: No API to forecast based on custom input
- They lack **custom ML logic** that reflects internal pricing models

This project solves that by allowing users to **predict cloud costs dynamically**, based on CPU, memory, and storage values — all in an extensible, API-driven manner.

---

## 🔍 Solution Approach

We model the problem as a **regression task**, where:

- **Inputs:** Number of vCPUs, RAM (in GB), and Storage (in GB)
- **Target:** Monthly cost (USD)

---



---

##  Real-World Impact

###  Why Predict Cloud Costs?

Predicting cloud costs before provisioning infrastructure is like knowing your electricity bill before turning on the appliances.

Cloud pricing is complex — driven by:
-  vCPUs
-  RAM (GB)
-  Storage (GB)

With this model:
-  Avoid surprise cloud bills
-  Simulate infra costs for upcoming deployments
-  Align with your budgeting strategy

### 👤 Example Use Case 1: DevOps/Developer Team

> “I need a VM with 8 CPUs, 32 GB RAM, 500 GB storage. What’s the monthly cost?”

Rather than guess, call the API → get estimate → decide → save costs 💰

### 👤 Use Case 2: Product / Finance Team

> “We expect 20,000 new users next month. Can we model cost for scaled infra?”

This tool allows the team to simulate and compare different resource combinations **before provisioning** anything.

---
### Steps:

1. **Prepare a synthetic dataset** of cloud resource combinations and corresponding costs
2. **Train a regression model** using scikit-learn
3. **Serialize the model** using Pickle
4. **Serve predictions** via a FastAPI app at a `/predict` endpoint
5. **Accept JSON input** and return real-time cost estimate

The current model uses a basic `LinearRegression`, but it can be easily extended to other ML or even XGBoost models as needed.

---

## 🧠 Technologies Used

| Layer          | Tech                    |
|----------------|-------------------------|
| ML Modeling    | scikit-learn, pandas    |
| API Framework  | FastAPI + Uvicorn       |
| Packaging      | joblib                  |
| Data Source    | CSV (or future AWS Cost Explorer) |
| Language       | Python 3.9+             |

---

## 🗂️ Folder Structure
```
cloud-cost-forecasting/
├── ml/
│   └── train_model.py           # Trains the model and saves .pkl
├── data/
│   └── cloud_cost_data.csv      # Sample dataset with cost mapping
├── models/
│   └── cloud_cost_model.pkl     # Trained ML model
├── app.py                       # FastAPI app exposing /predict endpoint
├── requirements.txt             # Python packages needed
├── README.md                    # Project documentation
└── LICENSE                      # MIT License
```

---

## 🛠️ Installation and Setup

### 1. Install Python

Ensure Python 3.9 is installed:

```bash
python --version

If not, install from: https://www.python.org/downloads/

### 2. Clone the Repository
'''bash
git clone https://github.com/Nikitha1099/cloud-cost-forecasting.git
cd cloud-cost-forecasting

### 3. Create Virtual Environment
'''bash
python -m venv venv
venv\Scripts\activate     # On Windows
# OR
source venv/bin/activate # On macOS/Linux

### 4. Install Dependencies
'''bash
pip install -r requirements.txt

### 5. Train the ML Model
'''bash
python ml/train_model.py

This creates a trained cloud_cost_model.pkl file under models/.

### 6. Launch FastAPI Server
'''bash
uvicorn app:app --reload

Go to browser: http://127.0.0.1:8000/docs
You'll see Swagger UI for sending predictions.

---
##  Example Use Cases
Here’s how this prediction service can be used in real-world scenarios:

- Pre-Provisioning Checks: Estimate cost before launching instances.

- Developer Portals: Let devs choose resources and preview pricing.

- Internal Dashboards: Integrate with tools like Grafana or Streamlit.

- Budget Alerts: Combine with automation to warn about overages.

- Resource Scaling: Simulate the financial impact of scale-up/scale-down.

## 📈 Impact and Significance
-   This project represents a real-world FinOps tool.

-   Makes cloud usage predictable and transparent

-   Educates developers on linking infrastructure metrics with business metrics

-   Serves as a foundation for deeper cloud cost optimization

-   Can be deployed as a microservice or integrated into enterprise systems

---

