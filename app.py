import streamlit as st
import pandas as pd
from predict_today import todays_predictions

st.title("⚾ MLB Predictor App")

# Generate today's predictions explicitly within Streamlit
try:
    # Save predictions explicitly
    todays_predictions.to_csv('todays_predictions.csv', index=False)
    st.success("Predictions generated successfully!")
except Exception as e:
    st.error(f"⚠️ Error generating predictions: {e}")

# Load today's predictions clearly into Streamlit
try:
    predictions = pd.read_csv('todays_predictions.csv')
    st.write("✅ Today's MLB Predictions:")
    st.dataframe(predictions)
except Exception as e:
    st.error(f"⚠️ Error loading predictions: {e}")
