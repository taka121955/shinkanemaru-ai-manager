def calculate_next_bet(results, initial_fund, target_amount):
    """
    ECP方式の次回賭け金を計算。
    条件：
    - 残金が100円未満なら0を返す
    - 目標金額に到達したら0を返す

    引数:
    - results: 勝敗データのリスト（辞書）
    - initial_fund: 初期資金（例：10000）
    - target_amount: 目標金額（例：20000）
    """

    total_spent = sum([r["wager"] for r in results])
    total_earned = sum([r["wager"] * r["odds"] if r.get("hit") else 0 for r in results])

    current_balance = initial_fund + total_earned - total_spent

    if current_balance < 100:
        return 0
    if current_balance >= target_amount:
        return 0

    # 基本ロジック：100円ずつ掛け金上げるシンプルモデル
    return 100
