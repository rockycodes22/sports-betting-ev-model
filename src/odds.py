def implied_probability(american_odds):
    if american_odds > 0:
        risk = 100
        win = american_odds
    else:
        risk = abs(american_odds)
        win = 100
    probability = risk/(risk +win)
    return probability 

def remove_vig(implied_probs):
    fair_probs =[]
    total = sum(implied_probs)
    for i in implied_probs:
        fixed_prob =i/ total
        fair_probs.append(fixed_prob)
    return fair_probs