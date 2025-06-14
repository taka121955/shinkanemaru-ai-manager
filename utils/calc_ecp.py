# utils/calc_ecp.py

def calculate_next_bet(records, odds):
    if not records or len(records) == 0:
        return 100  # 初回は100円ベット

    last = records[-1]
    last_hit = last.get("的中", False)
    last_bet = last.get("賭け金", 100)

    if last_hit:
        return 100
    else:
        if odds >= 2.0:
            return int(last_bet * 1.5)
        else:
            return int(last_bet * 2.0)
