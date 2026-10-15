
import pandas as pd
from model import predict_fraud

# Load the sample transactions
data = pd.read_csv("sample_transactions.csv")

# Keep the actual labels for comparison
actual_labels = data["Class"].astype(int)

# Select only the 29 features used by the model
features = data.drop(columns=["id", "Class"])

# Make sure the feature order matches training
feature_names = [f"V{i}" for i in range(1, 29)] + ["Amount"]
features = features[feature_names]

# Predict each transaction
predictions = []

for _, row in features.iterrows():
    prediction, probability = predict_fraud(row.tolist())
    predictions.append(prediction)

# Compare predictions with actual labels
results = pd.DataFrame({
    "Actual Class": actual_labels,
    "Predicted Class": predictions
})

results["Correct"] = (
    results["Actual Class"] == results["Predicted Class"]
)

print(results.to_string(index=False))

accuracy = results["Correct"].mean() * 100
print(f"\nSample accuracy: {accuracy:.2f}%")

