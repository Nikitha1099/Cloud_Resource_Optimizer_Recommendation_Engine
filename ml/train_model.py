import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv("data/cloud_cost_data.csv")

# Drop timestamp (not needed for training)
df = df.drop(columns=["timestamp"])

# Features and labels
X = df[["cpu", "memory", "storage"]]
y = df["cost"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "models/cloud_cost_model.pkl")
print(" Model retrained and saved to models/cloud_cost_model.pkl")
