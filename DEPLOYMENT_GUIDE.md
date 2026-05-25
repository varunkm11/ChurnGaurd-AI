# ChurnGuard AI - Streamlit Cloud Deployment Guide

## Prerequisites

- GitHub account with your repository pushed
- Streamlit Cloud account (free at [streamlit.io](https://streamlit.io))

## Deployment Steps

### 1. Push Your Repository to GitHub

```bash
git add .
git commit -m "Prepare for Streamlit Cloud deployment"
git push origin main
```

### 2. Deploy to Streamlit Cloud

1. Go to [streamlit.io](https://streamlit.io)
2. Click **"New app"**
3. Select your repository, branch, and specify the file path:
   - **Repository**: Select your repo
   - **Branch**: `main` (or your default branch)
   - **Main file path**: `app/app.py`

### 3. Configuration

The app uses the following configuration file:
- `.streamlit/config.toml` - Streamlit settings (already configured)

### 4. Secrets Management (if needed)

If your app needs API keys or credentials:
1. In Streamlit Cloud app settings, go to **Secrets**
2. Add your secrets in the format (TOML):
   ```toml
   api_key = "your-key-here"
   database_url = "your-url-here"
   ```
3. Access them in your app using: `st.secrets["api_key"]`

## File Structure

```
ChurnGaurd AI/
├── app/
│   └── app.py                # Main Streamlit application
├── src/
│   ├── preprocess.py         # Data preprocessing
│   ├── train.py              # Model training
│   ├── predict.py            # Predictions
│   └── utils.py              # Utilities
├── models/
│   ├── churn_model.pkl       # Trained XGBoost model
│   └── scaler.pkl            # StandardScaler for preprocessing
├── data/
│   └── telco_churn.csv       # Dataset
├── .streamlit/
│   ├── config.toml           # Streamlit configuration
│   └── secrets.toml.example  # Template for secrets
├── requirements.txt          # Python dependencies
├── runtime.txt               # Python version specification
└── README.md                 # Project documentation
```

## Key Features Implemented for Deployment

✅ **Fixed Relative Paths** - App uses correct path resolution for Streamlit Cloud
✅ **Caching** - Models and data are cached to improve performance
✅ **Configuration File** - `.streamlit/config.toml` for optimal settings
✅ **Dependencies** - All packages listed in `requirements.txt`
✅ **Python Version** - Specified in `runtime.txt`

## Requirements Met

The project includes:
- **streamlit** - Web framework
- **scikit-learn** - Machine learning preprocessing
- **xgboost** - Model library
- **pandas** - Data manipulation
- **joblib** - Model serialization
- **plotly** - Interactive visualizations
- **shap** - Model explainability
- **matplotlib** - Static visualizations

## Troubleshooting

### Model or Data Not Found
- Ensure `models/` and `data/` folders are committed to GitHub
- Check that `.gitignore` doesn't exclude these folders

### Import Errors
- Verify all dependencies are in `requirements.txt`
- Check Python version in `runtime.txt` matches your development environment

### Performance Issues
- The app caches models and data using `@st.cache_resource` and `@st.cache_data`
- SHAP explainability might be slow for large datasets - consider optimizing

## Local Testing Before Deployment

Test locally to ensure everything works:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app/app.py
```

## Monitoring & Logs

After deployment:
1. View logs in Streamlit Cloud app settings
2. Monitor app performance
3. Check for any runtime errors

## Next Steps

1. Update `README.md` with project description and usage instructions
2. Consider adding data caching strategy for large datasets
3. Optimize SHAP explainability for production use
4. Add error handling for edge cases
5. Consider implementing user authentication if needed

---

For more information, visit [Streamlit Documentation](https://docs.streamlit.io/)
