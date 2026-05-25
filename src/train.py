import joblib
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score

from preprocess import load_data, preprocess_data

# Load dataset
df = load_data("../data/telco_churn.csv")

# Preprocess
X_train, X_test, y_train, y_test, scaler = preprocess_data(df)

# Model
model = XGBClassifier(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=5,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# Metrics
accuracy = accuracy_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_prob)

print("Accuracy:", accuracy)
print("ROC-AUC:", roc_auc)

print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "../models/churn_model.pkl")
joblib.dump(scaler, "../models/scaler.pkl")

print("Model saved successfully!")