import streamlit as st
import pandas as pd
from predict_today import (
    moneyline_picks, 
    runline_picks, 
    total_picks,
    player_prop_picks, 
    correct_score_picks
)

st.title("⚾ MLB Predictor App - Daily Top Picks")

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

# Best possible 5-leg parlay from all picks
all_picks = pd.concat([
    moneyline_picks.assign(Category="Moneyline"),
    runline_picks.assign(Category="Runline"),
    total_picks.assign(Category="Total"),
    player_prop_picks.assign(Category="Player Prop"),
    correct_score_picks.assign(Category="Correct Score")
])

best_parlay = all_picks.sort_values(by="Probability (%)", ascending=False).head(5)

st.header("🚀 Best 5-Leg Parlay Recommendation")
st.dataframe(best_parlay[["Category", "Game", "Pick", "Probability (%)"]])
