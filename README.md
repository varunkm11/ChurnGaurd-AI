# 📊 ChurnGuard AI - Customer Churn Prediction

An AI-powered web application for predicting customer churn using machine learning. Built with Streamlit, XGBoost, and SHAP for explainable AI.

## 🌟 Features

- **Interactive Dashboard** - Visualize customer churn patterns with interactive charts
- **Real-time Predictions** - Predict customer churn probability based on input features
- **Explainable AI** - SHAP values show which features influence predictions
- **Data Insights** - Explore churn distribution and customer behavior patterns
- **Professional UI** - Clean, responsive interface with Plotly visualizations

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ChurnGaurd\ AI
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run app/app.py
   ```

5. **Open in browser**
   - Navigate to `http://localhost:8501`

### Cloud Deployment

Deploy to [Streamlit Cloud](https://streamlit.io/cloud) in minutes:

1. Push your repository to GitHub
2. Visit [streamlit.io/cloud](https://streamlit.io/cloud)
3. Create new app and select:
   - Repository: Your GitHub repo
   - Main file path: `app/app.py`

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions.

## 📦 Requirements

- Python 3.12+
- See `requirements.txt` for all dependencies

## 🏗️ Project Structure

```
ChurnGaurd AI/
├── app/
│   └── app.py                        # Main Streamlit app
├── src/
│   ├── preprocess.py                 # Data preprocessing functions
│   ├── train.py                      # Model training script
│   ├── predict.py                    # Prediction utilities
│   └── utils.py                      # Helper functions
├── models/
│   ├── churn_model.pkl               # Trained XGBoost model
│   └── scaler.pkl                    # StandardScaler for feature scaling
├── data/
│   └── telco_churn.csv               # Customer churn dataset
├── .streamlit/
│   ├── config.toml                   # Streamlit configuration
│   └── secrets.toml.example          # Secrets template
├── notebooks/                        # Jupyter notebooks for analysis
├── requirements.txt                  # Python dependencies
├── runtime.txt                       # Python version
└── DEPLOYMENT_GUIDE.md               # Deployment instructions
```

## 🤖 Model Details

- **Algorithm**: XGBoost Classifier
- **Features**: 19 customer features
- **Training Data**: Telecommunications customer churn dataset
- **Metrics**:
  - Accuracy: ~80%
  - ROC-AUC: ~0.85

## 📊 Dashboard Sections

1. **Churn Distribution** - Histogram of churn vs non-churn customers
2. **Tenure vs Monthly Charges** - Scatter plot showing customer patterns
3. **Prediction Section** - Input customer details and predict churn probability
4. **Explainability** - SHAP waterfall plot showing feature contributions
5. **Dataset Preview** - View raw customer data

## 🎯 How to Use

### Make Predictions

1. Use the sidebar to input customer information:
   - Tenure (months)
   - Monthly charges ($)
   - Total charges ($)
   - Senior citizen status

2. Click **"Predict Churn"** button

3. View results:
   - Churn probability gauge
   - Risk assessment (warning/success)
   - SHAP explainability chart

### Interpret Results

- **Red (⚠️)**: Customer likely to churn
- **Green (✅)**: Customer likely to stay
- **SHAP values**: Show which features most influence the prediction

## 🔧 Configuration

Edit `.streamlit/config.toml` to customize:
- Theme colors
- Page layout
- Sidebar behavior
- Upload file size limits

## 📝 Environment Variables

Create `.streamlit/secrets.toml` for sensitive data:
```toml
# Example
database_url = "your-database-url"
api_key = "your-api-key"
```

Access with: `st.secrets["database_url"]`

## 🛠️ Development

### Training a New Model

```bash
python src/train.py
```

This updates:
- `models/churn_model.pkl`
- `models/scaler.pkl`

### Making Predictions (Programmatically)

```python
import joblib
from src.preprocess import load_data

model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# Your prediction logic
```

## 📊 Dataset

The project uses the Telco Customer Churn dataset with:
- 7,043 customer records
- 19 features (demographics, services, charges)
- Binary target: Churn (Yes/No)

## 🚨 Troubleshooting

| Issue | Solution |
|-------|----------|
| Model not found | Ensure `models/` folder is committed to Git |
| Import errors | Run `pip install -r requirements.txt` |
| Slow predictions | Models are cached; restart app to clear cache |
| Path errors | Use `streamlit run app/app.py` |

## 📚 Libraries Used

- **streamlit** - Web app framework
- **xgboost** - Machine learning
- **scikit-learn** - ML preprocessing & metrics
- **pandas** - Data manipulation
- **plotly** - Interactive visualizations
- **shap** - Model explainability
- **matplotlib** - Static plots
- **joblib** - Model serialization

## 📄 License

[Add your license here]

## 👨‍💻 Author

[Your name/organization]

## 📧 Support

For issues and questions, please:
1. Check [Troubleshooting](#troubleshooting) section
2. Review [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
3. Check Streamlit [documentation](https://docs.streamlit.io)

---

**Last Updated**: May 2024
**Deployment Ready**: ✅ Yes
**Status**: Production Ready
