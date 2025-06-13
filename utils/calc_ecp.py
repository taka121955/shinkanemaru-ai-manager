def calculate_next_bet(df):
    if df.empty:
        return 100
    losses = df[df["収支"] < 0]
    if losses.empty:
        return 100
    total_deficit = -losses["収支"].sum()
    return int(total_deficit / 2 + 100)  # 仮ECP計算（例）
