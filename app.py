import streamlit as st
import pandas as pd

st.title("⚾ MLB Predictor App - Daily Top Picks")

# Load predictions explicitly from the saved Excel file
predictions = pd.ExcelFile("todays_predictions.xlsx")

# Clearly display each category
st.header("🔥 Top 5 Moneyline Picks")
st.dataframe(predictions.parse("Moneyline Picks"))

st.header("💪 Top 5 Run Line Picks")
st.dataframe(predictions.parse("Runline Picks"))

st.header("📊 Top 5 Total (Over/Under) Picks")
st.dataframe(predictions.parse("Total Picks"))

st.header("👤 Top 5 Player Prop Picks")
st.dataframe(predictions.parse("Player Prop Picks"))

st.header("🎯 Top 5 Correct Score Predictions")
st.dataframe(predictions.parse("Correct Score Picks"))

# Best possible 5-leg parlay (highest probabilities from all picks)
all_picks = pd.concat([
    predictions.parse("Moneyline Picks").assign(Category="Moneyline"),
    predictions.parse("Runline Picks").assign(Category="Runline"),
    predictions.parse("Total Picks").assign(Category="Total"),
    predictions.parse("Player Prop Picks").assign(Category="Player Prop"),
    predictions.parse("Correct Score Picks").assign(Category="Correct Score")
])

best_parlay = all_picks.sort_values(by="Probability (%)", ascending=False).head(5)

st.header("🚀 Recommended 5-Leg Parlay Today")
st.dataframe(best_parlay[["Category", "Game", "Pick", "Probability (%)"]])
