def implied_probability(american_odds):
    if american_odds > 0:
        risk = 100
        win = american_odds
    else:
        risk = abs(american_odds)
        win = 100
    probability = risk/(risk +win)
    return probability 