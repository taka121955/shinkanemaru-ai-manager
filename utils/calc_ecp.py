# utils/calc_ecp.py

def calculate_ecp_amount(wave):
    if wave == 1:
        return 100
    elif wave == 2:
        return 300
    elif wave == 3:
        return 900
    else:
        return 0
