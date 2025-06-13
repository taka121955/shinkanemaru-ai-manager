# utils/calc_ecp.py
def calculate_next_bet(funds, loss_count):
    base = 100
    if loss_count == 0:
        return base
    elif loss_count == 1:
        return base * 3
    elif loss_count == 2:
        return base * 9
    else:
        return base * 9
