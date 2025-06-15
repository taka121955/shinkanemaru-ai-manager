# utils/calc_ecp.py

def get_ecp_wave_distribution():
    return {
        "wave1": [100, 300, 900],
        "wave2": [200, 600, 1800],
        "wave3": [600, 1800, 3600],
    }

def calculate_next_bet(records, initial_fund, reserve_fund):
    wave_config = get_ecp_wave_distribution()
    total_fund = initial_fund + reserve_fund

    # 初回：第1波の100円
    if not records:
        return 100, 1, 1, reserve_fund

    # 波ごとの進捗確認
    current_wave = 1
    current_step = 1
    loss_sum = 0

    # 成功判定：過去どこかで的中があったか
    for record in records[::-1]:
        if record.get("的中", False):
            break
        loss_sum += record.get("賭け金", 0)

    # 波・ステップを決定
    total_steps = sum(len(v) for v in wave_config.values())
    for wave in range(1, 4):
        steps = wave_config[f"wave{wave}"]
        for step_index in range(len(steps)):
            if len(records) < total_steps:
                current_wave = wave
                current_step = step_index + 1
                break
        else:
            continue
        break

    # ベット金額
    try:
        bet = wave_config[f"wave{current_wave}"][current_step - 1]
    except IndexError:
        return None, current_wave, current_step, reserve_fund

    # 積立金から補填（第1波でのみ使う）
    if current_wave == 1 and bet > initial_fund:
        if reserve_fund >= bet - initial_fund:
            reserve_fund -= (bet - initial_fund)
            initial_fund = 0
        else:
            return None, current_wave, current_step, reserve_fund

    # 残高チェック
    if bet > total_fund:
        return None, current_wave, current_step, reserve_fund

    return bet, current_wave, current_step, reserve_fund
