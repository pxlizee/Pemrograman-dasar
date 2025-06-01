import pandas as pd

def updateScore(score):
    if score < 0:
        return 0
    elif score > 100:
        return 100
    else:
        return score

def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
    

scores = pd.read_excel("skor.xlsx")
scores["New Score"] = scores["Score"].apply(updateScore)
scores["Grade"] = scores["New Score"].apply(grade)
scores.to_excel('skor_updated.xlsx', index=False)
