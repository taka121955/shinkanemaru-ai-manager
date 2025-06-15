def calculate_next_bet(records, base_fund, reserve_fund):
    # 波ごとの総資金
    waves = [1300, 2600, 6100]
    # 各波の分配（1:2:4 → 1:3:9）を展開済み
    wave_distribution = [
        [100, 300, 900],    # 第1波
        [200, 600, 1800],   # 第2波
        [600, 1800, 3600],  # 第3波
    ]

    # 残高計算
    if not records:
        return wave_distribution[0], 0, 0, "第一波①"

    # 最後の履歴を参照
    last = records[-1]
    last_win = last.get("的中", False)
    last_wave = last.get("波", "第一波①")
    used_fund = last.get("賭け金", 0)

    # 勝った場合：第一波に戻し、積立金に追加
    if last_win:
        reserve_fund += used_fund
        return wave_distribution[0], base_fund, reserve_fund, "第一波①"

    # 波と段階の管理
    wave_map = {
        "第一波①": ("第一波②", wave_distribution[0][1]),
        "第一波②": ("第一波③", wave_distribution[0][2]),
        "第一波③": ("第二波①", wave_distribution[1][0]),
        "第二波①": ("第二波②", wave_distribution[1][1]),
        "第二波②": ("第二波③", wave_distribution[1][2]),
        "第二波③": ("第三波①", wave_distribution[2][0]),
        "第三波①": ("第三波②", wave_distribution[2][1]),
        "第三波②": ("第三波③", wave_distribution[2][2]),
    }

    # 最後の波に応じた次ステップ
    next_step, next_amount = wave_map.get(last_wave, ("RESET", 0))

    # 第三波③まで来たらリセット
    if next_step == "RESET":
        return wave_distribution[0], base_fund, 0, "第一波①（リセット）"

    # 積立金使用処理（第一波のみ）
    if "第一波" in next_step:
        if reserve_fund >= next_amount:
            reserve_fund -= next_amount
        else:
            # 積立不足：本資金から補填
            base_fund -= next_amount - reserve_fund
            reserve_fund = 0
    else:
        base_fund -= next_amount

    # 残高チェック
    if base_fund < 0:
        return wave_distribution[0], 10000, 0, "第一波①（リセット）"

    # 次の金額を返す（単体金額ではなくセット全体）
    current_wave_index = int(next_step[2]) - 1  # "第二波①" → 1
    return wave_distribution[current_wave_index], base_fund, reserve_fund, next_step
