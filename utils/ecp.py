def get_next_bet_amount(records):
    """
    新金丸法 × ECP方式：1:3:9の3段階で資金配分
    総資金は10,000円想定。3段階目は最大で9,000円まで。
    """
    losses = [r for r in records if r["結果"] == "不的中"]
    count = len(losses)

    if count % 3 == 0:
        return 100  # 1回目
    elif count % 3 == 1:
        return 300  # 2回目
    else:
        return 900  # 3回目
