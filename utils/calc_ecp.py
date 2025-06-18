# utils/calc_ecp.py
def calculate_ecp_amount(result: str, odds: float, fund: int) -> int:
    if result == "的中":
        return 100  # 的中時は100円固定ベットなど
    else:
        # 不的中時：段階に応じた再計算（例）
        if fund == 1300:
            return 300
        elif fund == 3900:
            return 900
        elif fund == 10000:
            return 1500
        else:
            return 100
