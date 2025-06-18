# utils/calc_ecp.py

def calculate_ecp_amount(result, odds, fund):
    """
    ECP方式（簡略）でベット金額を1つだけ算出。
    result: "的中" または "不的中"
    odds: オッズ（float）
    fund: 総資金（int）
    """

    if result == "的中":
        return 0  # 的中した場合は次のベットなし（またはスキップ）

    # 初期ベット金額（資金に応じてベースを変更）
    if fund == 1300:
        return 100
    elif fund == 3900:
        return 300
    elif fund == 10000:
        return 500
    else:
        return 0  # 想定外の資金額
