def reset_ecp_state():
    return {
        "losses": 0,
        "base_bets": [100, 300, 900],
        "phase_bets": [13000, 26000, 61000]
    }

def get_next_bet_amount(state):
    losses = state["losses"]
    base = state["base_bets"]

    # 第一波（100 → 300 → 900）
    if losses < len(base):
        return base[losses]
    # 第二波突入（合計13000円の回収目指す）
    elif losses == 3:
        return 2000
    elif losses == 4:
        return 4000
    elif losses == 5:
        return 7000
    else:
        # 損切りまたは資金が尽きたら1から
        return base[0]
