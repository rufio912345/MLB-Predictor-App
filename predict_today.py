import pandas as pd

# Example predictions (clearly structured for immediate testing)
todays_predictions = pd.DataFrame({
    "Game": ["Orioles @ Guardians", "Blue Jays @ Tigers", "Padres @ Cardinals"],
    "Bet Type": ["Moneyline", "Run Line", "Total Runs"],
    "Pick": ["Orioles ML", "Blue Jays -1.5", "Over 8.5"],
    "Probability (%)": [74.3, 71.8, 69.7]
})

# Save explicitly to CSV for Streamlit to load
todays_predictions.to_csv("todays_predictions.csv", index=False)
