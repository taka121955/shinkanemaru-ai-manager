# utils/race_generator.py

def generate_race_list(venues):
    """
    各競艇場に対して、1R〜12Rまでのレースを全て生成。
    例：住之江 → 1R〜12R、浜名湖 → 1R〜12R など
    """
    all_races = []

    for venue in venues:
        for race_no in range(1, 13):  # 1〜12R
            all_races.append({
                "venue": venue,
                "race_no": race_no
            })

    return all_races
