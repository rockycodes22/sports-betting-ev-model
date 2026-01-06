# Convert American odds to implied probability
def implied_probability(american_odds):
    if american_odds > 0:
        risk = 100
        win = american_odds
    else:
        risk = abs(american_odds)
        win = 100
    probability = risk/(risk +win)
    return probability 

# Remove the vig from a list of implied probabilities
def remove_vig(implied_probs):
    fair_probs =[]
    total = sum(implied_probs)
    for i in implied_probs:
        fixed_prob =i/ total
        fair_probs.append(fixed_prob)
    return fair_probs

# Convert soccer moneyline odds to implied probabilities without vig
def soccer_moneyline_fair_probs(home_odds, draw_odds, away_odds):
    home_prob = implied_probability(home_odds)
    draw_prob = implied_probability(draw_odds)
    away_prob = implied_probability(away_odds)
    implied_probs = [home_prob, draw_prob, away_prob]
    fair_probs = remove_vig(implied_probs)
    return {
        "home" : fair_probs[0],
        "draw" : fair_probs[1],
        "away" : fair_probs[2]
    }

