def classify_difficulty(scli_score):
    if scli_score >= 7:
        return "High Difficulty"
    elif scli_score >= 4:
        return "Medium Difficulty"
    else:
        return "Low Difficulty"
