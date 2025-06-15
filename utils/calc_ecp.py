
def calculate_next_bets(records, initial_funds, reserve_funds):
    waves = [
        {"total": 1300, "pattern": [100, 300, 900]},
        {"total": 2600, "pattern": [200, 600, 1800]},
        {"total": 6100, "pattern": [600, 1800, 3600]}
    ]

    # 現在の波のインデックス
    wave_index = 0
    next_bet_pattern = waves[wave_index]["pattern"]

    # 的中履歴からどこまで消化されたかを確認
    for i in range(len(records) - 1, -1, -1):
        if records[i].get("波") == "リセット":
            break
        if records[i].get("的中") is True:
            break
        if records[i].get("的中") is False:
            wave_index += 1

    if wave_index >= len(waves):
        return "リセット"

    # 残高チェック
    required = waves[wave_index]["total"]
    available = initial_funds + reserve_funds
    if available < required:
        return "リセット"

    return {
        "波": wave_index + 1,
        "分配": next_bet_pattern,
        "必要資金": required
    }
