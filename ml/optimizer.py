import pandas as pd
import numpy as np
import warnings
import joblib

warnings.filterwarnings("ignore")

# Load baseline (latest usage from logs)
df = pd.read_csv("data/cloud_cost_data.csv")
baseline = df.iloc[-1]

cpu = baseline["cpu"]
memory = baseline["memory"]
storage = baseline["storage"]
baseline_cost = baseline["cost"]

print("\n Baseline (latest usage from logs):")
print(f"CPU: {cpu}, Memory: {memory} GB, Storage: {storage} GB, Cost: ${baseline_cost:.2f}")

# Load trained ML model
model = joblib.load("models/cloud_cost_model.pkl")

# User-defined constraints (workload needs)
min_cpu = max(2, cpu - 2)       # allow reduction by at most 2 CPUs
min_memory = max(2, memory - 2) # allow reduction by at most 2 GB
min_storage = max(50, storage - 200) # allow reduction by at most 200 GB

cpu_range = range(min_cpu, cpu + 1)
memory_range = range(min_memory, memory + 1)
storage_range = range(min_storage, storage + 1, 50)

results = []

# Search space
for c in cpu_range:
    for m in memory_range:
        for s in storage_range:
            predicted_cost = model.predict([[c, m, s]])[0]
            savings_pct = ((baseline_cost - predicted_cost) / baseline_cost) * 100
            results.append({
                "cpu": c,
                "memory": m,
                "storage": s,
                "predicted_cost": round(predicted_cost, 2),
                "savings_percent": round(savings_pct, 2)
            })

# Sort by cost
results = sorted(results, key=lambda x: x["predicted_cost"])

# Show top 5 options
print("\n Top Optimization Suggestions (meeting workload needs):")
for r in results[:5]:
    print(f"- CPU: {r['cpu']}, Memory: {r['memory']} GB, Storage: {r['storage']} GB | "
          f"Cost: ${r['predicted_cost']} | Savings: {r['savings_percent']}%")
