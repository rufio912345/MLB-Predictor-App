import streamlit as st
import pandas as pd
import subprocess

st.title("⚾ MLB Predictor App")

# Run the prediction script explicitly and capture errors clearly
result = subprocess.run(["python", "predict_today.py"], capture_output=True, text=True)

if result.returncode == 0:
    st.success("Predictions generated successfully!")
else:
    st.error(f"⚠️ Error running prediction script: {result.stderr}")

# Load today's predictions clearly into Streamlit
try:
    predictions = pd.read_csv('todays_predictions.csv')
    st.write("✅ Today's MLB Predictions:")
    st.dataframe(predictions)
except Exception as e:
    st.error(f"⚠️ Error loading predictions: {e}")
