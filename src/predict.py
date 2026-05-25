import joblib
import numpy as np

# Load model and scaler
model = joblib.load("../models/churn_model.pkl")
scaler = joblib.load("../models/scaler.pkl")


def predict_churn(data):

    data = np.array(data).reshape(1, -1)

    data_scaled = scaler.transform(data)

    prediction = model.predict(data_scaled)[0]
    probability = model.predict_proba(data_scaled)[0][1]

    return prediction, probability