def calculate_next_bet(df):
    if df.empty:
        return 100  # 初回は100円

    last_bet = df["賭金"].iloc[-1]
    last_result = df["的中"].iloc[-1]

    if last_result == "的中":
        return 100
    else:
        # ECP方式: 損失を回収するための3ステップ（100円→300円→900円）
        losses = df[df["的中"] == "不的中"]
        loss_count = len(losses)
        if loss_count == 1:
            return 300
        elif loss_count == 2:
            return 900
        else:
            return 100  # リセット
