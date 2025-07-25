import streamlit as st
import pandas as pd
from predict_today import predictions_df

st.title("⚾ MLB Predictor App - Real Daily Picks")

# Display today's real predictions
st.header("🔥 Today's MLB Predictions")
st.dataframe(predictions_df)

# Clearly show best 5-leg parlay (highest probabilities)
best_parlay = predictions_df.sort_values(by="Probability (%)", ascending=False).head(5)

st.header("🚀 Recommended 5-Leg Parlay Today")
st.dataframe(best_parlay)
