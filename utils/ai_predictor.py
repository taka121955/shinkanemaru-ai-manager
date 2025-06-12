import random

def generate_ai_predictions():
    race_data = []
    venues = ["住之江", "尼崎", "大村", "戸田", "唐津"]
    rounds = [f"{r}R" for r in range(1, 13)]
    boats = ["1号艇", "2号艇", "3号艇", "4号艇", "5号艇", "6号艇"]
    for _ in range(5):
        venue = random.choice(venues)
        round_ = random.choice(rounds)
        boat = random.choice(boats)
        score = round(random.uniform(0.65, 0.95), 2)
        race_data.append({
            "競艇場": venue,
            "レース": round_,
            "式別": "単勝",
            "艇番": boat,
            "スコア": score
        })
    race_data.sort(key=lambda x: x["スコア"], reverse=True)
    return race_data
