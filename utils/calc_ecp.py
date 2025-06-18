# utils/calc_ecp.py

def calculate_ecp_amount(result, odds, fund):
    """
    ECP方式（簡略版）でベット金額を1つだけ自動計算します。

    Parameters:
    - result: "的中" or "不的中"
    - odds: float（オッズ、現時点では未使用でもOK）
    - fund: int（資金モード：1300, 3900, 10000）

    Returns:
    - int：ベットすべき金額
    """

    if result == "的中":
        return 0  # 的中なら次のベットは不要

    if fund == 1300:
        return 100  # ECPモード：1300円 → 100円からスタート
    elif fund == 3900:
        return 300  # 3900円 → 300円スタート
    elif fund == 10000:
        return 500  # 10000円 → 500円スタート
    else:
        return 0  # 不正な資金額
