def calculate_next_bet(remaining_budget, odds, history):
    """
    次の賭け金をECP戦略に基づいて計算する関数
    :param remaining_budget: 現在の残高（円）
    :param odds: 予想されるオッズ（float）
    :param history: 過去のベット履歴（今は未使用）
    :return: 次回賭け金（円）
    """
    try:
        if odds <= 1:
            return 0  # オッズが1以下なら意味がない

        # 基本的なECP計算式（履歴は使用しないシンプルバージョン）
        bet = int(remaining_budget / (odds - 1))

        # 残高を超える賭け金は出さない
        return min(bet, remaining_budget)

    except Exception as e:
        print(f"ベット計算エラー: {e}")
        return 0
