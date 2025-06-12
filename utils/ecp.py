def reset_ecp():
    return {
        "loss": [],
        "base": 100
    }

def get_next_bet_amount(ecp_state):
    loss_count = len(ecp_state["loss"])
    if loss_count == 0:
        return 100
    elif loss_count == 1:
        return 300
    elif loss_count == 2:
        return 900
    elif loss_count == 3:
        return 2000
    elif loss_count == 4:
        return 6000
    else:
        return ecp_state["base"]  # リセット
