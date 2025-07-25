import streamlit as st
import pandas as pd
import subprocess

st.title("⚾ MLB Predictor App")

# Run your prediction script clearly
subprocess.run(["python", "predict_today.py"])

# Load today's predictions clearly into Streamlit
try:
    predictions = pd.read_csv('todays_predictions.csv')
    st.success("✅ Today's MLB predictions:")
    st.dataframe(predictions)
except Exception as e:
    st.error(f"⚠️ Error loading predictions: {e}")
