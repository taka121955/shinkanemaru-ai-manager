def reset_ecp():
    return {
        "loss_count": 0,
        "base_bet": 100,
    }

def get_next_bet_amount(loss_count):
    if loss_count == 0:
        return 100
    elif loss_count == 1:
        return 300
    elif loss_count == 2:
        return 900
    else:
        return 100
