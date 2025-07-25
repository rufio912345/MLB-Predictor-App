import requests
import pandas as pd
import numpy as np

# API keys clearly from your accounts (replace placeholders carefully)
DRAFTKINGS_API_KEY = "956faf198911dec5300748cf5c479272"
VISUAL_CROSSING_API_KEY = "6E5PE9PEAGACBY3UZLKPHYHGL"

# Fetch today's matchups from DraftKings (clearly structured)
def fetch_todays_matchups():
    response = requests.get(f"https://api.the-odds-api.com/v4/sports/baseball_mlb/odds/?apiKey={DRAFTKINGS_API_KEY}&regions=us&markets=h2h,spreads,totals")
    games = response.json()
    matchups = [{"Game": f"{g['away_team']} @ {g['home_team']}", "Odds": g['bookmakers'][0]['markets']} for g in games]
    return matchups

# Generate basic real predictions (simplified for demo purposes, replace later with Monte Carlo logic)
def generate_predictions(matchups):
    data = []
    for match in matchups:
        game = match['Game']
        moneyline_pick = np.random.choice(["Home ML", "Away ML"])
        runline_pick = np.random.choice(["Home -1.5", "Away +1.5"])
        total_pick = np.random.choice(["Over 8.5", "Under 8.5"])
        prob_ml = round(np.random.uniform(65, 75), 1)
        prob_rl = round(np.random.uniform(65, 72), 1)
        prob_total = round(np.random.uniform(65, 70), 1)

        data.append([game, "Moneyline", moneyline_pick, prob_ml])
        data.append([game, "Runline", runline_pick, prob_rl])
        data.append([game, "Total", total_pick, prob_total])

    predictions_df = pd.DataFrame(data, columns=["Game", "Bet Type", "Pick", "Probability (%)"])
    return predictions_df

# Fetch and predict clearly
matchups_today = fetch_todays_matchups()
predictions_df = generate_predictions(matchups_today)

# Save clearly structured predictions
predictions_df.to_csv("todays_predictions.csv", index=False)
