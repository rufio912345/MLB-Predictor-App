import pandas as pd

# Simulated data clearly structured for your final format (replace this with your real prediction code soon)
moneyline_picks = pd.DataFrame({
    "Game": ["Orioles @ Guardians", "Blue Jays @ Tigers", "Padres @ Cardinals", "Yankees @ Red Sox", "Mets @ Phillies"],
    "Pick": ["Orioles ML", "Blue Jays ML", "Padres ML", "Yankees ML", "Phillies ML"],
    "Probability (%)": [74.3, 73.1, 72.0, 71.6, 70.2]
})

runline_picks = pd.DataFrame({
    "Game": ["Orioles @ Guardians", "Blue Jays @ Tigers", "Padres @ Cardinals", "Dodgers @ Rockies", "Astros @ Mariners"],
    "Pick": ["Orioles -1.5", "Blue Jays -1.5", "Padres -1.5", "Dodgers -1.5", "Astros -1.5"],
    "Probability (%)": [72.5, 71.9, 70.8, 70.1, 69.8]
})

total_picks = pd.DataFrame({
    "Game": ["Orioles @ Guardians", "Blue Jays @ Tigers", "Padres @ Cardinals", "Rays @ Royals", "Giants @ Cubs"],
    "Pick": ["Over 8.5", "Under 9.0", "Over 7.5", "Under 10.0", "Over 8.0"],
    "Probability (%)": [69.7, 68.9, 68.2, 67.9, 67.5]
})

player_prop_picks = pd.DataFrame({
    "Player": ["A. Judge", "S. Ohtani", "J. Soto", "R. Acuña", "V. Guerrero Jr."],
    "Prop": ["HR", "Over 1.5 Hits", "RBI", "SB", "Over 0.5 Runs"],
    "Probability (%)": [70.5, 70.1, 69.7, 69.5, 69.1]
})

correct_score_picks = pd.DataFrame({
    "Game": ["Orioles @ Guardians", "Blue Jays @ Tigers", "Padres @ Cardinals", "Yankees @ Red Sox", "Mets @ Phillies"],
    "Predicted Score": ["5-3", "4-2", "6-4", "3-2", "4-3"],
    "Probability (%)": [66.5, 66.0, 65.5, 65.2, 64.9]
})

# Combine all clearly into one Excel or CSV for easy loading by Streamlit
with pd.ExcelWriter("todays_predictions.xlsx") as writer:
    moneyline_picks.to_excel(writer, sheet_name="Moneyline Picks", index=False)
    runline_picks.to_excel(writer, sheet_name="Runline Picks", index=False)
    total_picks.to_excel(writer, sheet_name="Total Picks", index=False)
    player_prop_picks.to_excel(writer, sheet_name="Player Prop Picks", index=False)
    correct_score_picks.to_excel(writer, sheet_name="Correct Score Picks", index=False)
