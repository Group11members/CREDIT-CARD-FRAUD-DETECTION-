
import joblib
import numpy as np
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "final_model.pkl"
PREPROCESSOR_PATH = BASE_DIR / "models" / "scaler.pkl"

model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)


def predict_fraud(features):
    feature_names = [f"V{i}" for i in range(1, 29)] + ["Amount"]

    features = np.asarray(features, dtype=float).reshape(1, -1)

    if features.shape[1] != model.n_features_in_:
        raise ValueError("The model requires exactly 29 features.")

    features_df = pd.DataFrame(features, columns=feature_names)

    scaled_features = preprocessor.transform(features_df)

    prediction = model.predict(scaled_features)[0]

    probability = None

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(scaled_features)[0][1]

    return int(prediction), probability