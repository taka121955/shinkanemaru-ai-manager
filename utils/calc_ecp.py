def calculate_ecp_amount(result, odds, fund):
    """
    ECP方式の自動計算（3波分割）
    """
    if result == "的中":
        return [100, 0, 0]  # 的中時は次の波不要

    if fund == 1300:
        return [100, 300, 900]
    elif fund == 3900:
        return [300, 900, 2700]
    elif fund == 10000:
        return [1300, 2600, 6100]
    else:
        return [0, 0, 0]  # 想定外の資金入力の場合もリストで返す
