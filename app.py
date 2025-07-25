import streamlit as st
import pandas as pd
import subprocess

st.title("⚾ MLB Predictor App")

# Explicitly run your prediction script first
try:
    subprocess.run(["python", "predict_today.py"], check=True)
    st.success("Predictions generated successfully!")
except Exception as e:
    st.error(f"⚠️ Error running prediction script: {e}")

# Load today's predictions clearly into Streamlit
try:
    predictions = pd.read_csv('todays_predictions.csv')
    st.write("✅ Today's MLB Predictions:")
    st.dataframe(predictions)
except Exception as e:
    st.error(f"⚠️ Error loading predictions: {e}")
