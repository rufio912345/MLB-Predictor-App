import streamlit as st
import pandas as pd
from predict_today import (moneyline_picks, runline_picks, total_picks,
                           player_prop_picks, correct_score_picks)

st.title("⚾ MLB Predictor App - Daily Picks")

# Display each clearly structured section
st.header("🔥 Top 5 Moneyline Picks")
st.dataframe(moneyline_picks)

st.header("💪 Top 5 Run Line Picks")
st.dataframe(runline_picks)

st.header("📊 Top 5 Total (Over/Under) Picks")
st.dataframe(total_picks)

st.header("👤 Top 5 Player Prop Picks")
st.dataframe(player_prop_picks)

st.header("🎯 Top 5 Correct Score Predictions")
st.dataframe(correct_score_picks)

# Explicitly create best 5-leg parlay clearly based on highest probabilities
best_parlay = pd.concat([
    moneyline_picks.head(1),
    runline_picks.head(1),
    total_picks.head(1),
    player_prop_picks.head(1).rename(columns={"Player": "Game", "Prop": "Pick"}),
    correct_score_picks.head(1).rename(columns={"Predicted Score": "Pick"})
]).reset_index(drop=True)

st.header("🚀 Best 5-Leg Parlay of the Day")
st.dataframe(best_parlay)
