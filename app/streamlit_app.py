import streamlit as st
import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import sys
import os
from pathlib import Path

# Path setup
app_dir = Path(__file__).parent
project_root = app_dir.parent
sys.path.append(str(project_root / "src"))

from preprocess import load_data

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="ChurnGuard AI",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# LOAD MODEL
# -----------------------------
@st.cache_resource
def load_model():
    model_path = project_root / "models" / "churn_model.pkl"
    scaler_path = project_root / "models" / "scaler.pkl"
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    return model, scaler

model, scaler = load_model()

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_dataset():
    data_path = project_root / "data" / "telco_churn.csv"
    return load_data(str(data_path))

df = load_dataset()

# -----------------------------
# TITLE
# -----------------------------
st.title("📊 ChurnGuard AI")
st.markdown("### AI-Powered Customer Churn Prediction Dashboard")

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("Customer Information")

tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 12)

monthly_charges = st.sidebar.slider(
    "Monthly Charges",
    0,
    150,
    70
)

total_charges = st.sidebar.slider(
    "Total Charges",
    0,
    10000,
    1000
)

senior_citizen = st.sidebar.selectbox(
    "Senior Citizen",
    [0, 1]
)

# -----------------------------
# INPUT DATA
# -----------------------------
input_data = [
    1,
    senior_citizen,
    1,
    0,
    tenure,
    1,
    0,
    1,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    0,
    1,
    monthly_charges,
    total_charges
]

input_df = pd.DataFrame([input_data])

input_scaled = scaler.transform(input_df)

# -----------------------------
# DASHBOARD COLUMNS
# -----------------------------
col1, col2 = st.columns(2)

# -----------------------------
# CHURN DISTRIBUTION
# -----------------------------
with col1:

    churn_fig = px.histogram(
        df,
        x="Churn",
        color="Churn",
        title="Customer Churn Distribution",
        text_auto=True
    )

    churn_fig.update_layout(
        height=400
    )

    st.plotly_chart(
        churn_fig,
        use_container_width=True
    )

# -----------------------------
# MONTHLY CHARGES VS TENURE
# -----------------------------
with col2:

    scatter_fig = px.scatter(
        df,
        x="MonthlyCharges",
        y="tenure",
        color="Churn",
        title="Monthly Charges vs Tenure",
        hover_data=["Contract"]
    )

    scatter_fig.update_layout(
        height=400
    )

    st.plotly_chart(
        scatter_fig,
        use_container_width=True
    )

# -----------------------------
# PREDICTION SECTION
# -----------------------------
st.markdown("---")

st.subheader("🔍 Predict Customer Churn")

if st.button("Predict Churn"):

    prediction = model.predict(input_scaled)[0]

    probability = model.predict_proba(input_scaled)[0][1]

    # -----------------------------
    # PREDICTION RESULT
    # -----------------------------
    if prediction == 1:

        st.error(
            f"⚠️ Customer likely to churn ({probability:.2%})"
        )

    else:

        st.success(
            f"✅ Customer likely to stay ({1 - probability:.2%})"
        )

    # -----------------------------
    # PROBABILITY GAUGE
    # -----------------------------
    gauge_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability * 100,
        title={'text': "Churn Probability"},
        gauge={
            'axis': {'range': [0, 100]}
        }
    ))

    gauge_fig.update_layout(height=400)

    st.plotly_chart(
        gauge_fig,
        use_container_width=True
    )

    # -----------------------------
    # SHAP EXPLAINABILITY
    # -----------------------------
    st.subheader("🧠 SHAP Explainability")

    explainer = shap.Explainer(model)

    shap_values = explainer(input_scaled)

    fig, ax = plt.subplots(
        figsize=(8, 4)
    )

    shap.plots.waterfall(
        shap_values[0],
        show=False
    )

    st.pyplot(
        fig,
        use_container_width=True
    )

# -----------------------------
# DATA PREVIEW
# -----------------------------
st.markdown("---")

st.subheader("📁 Dataset Preview")

st.dataframe(
    df.head(),
    use_container_width=True
)