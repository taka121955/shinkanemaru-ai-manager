def calculate_next_bet(records, balance):
    """
    ECP方式：第一波（1000円 → 3000円 → 9000円）の資金戦略でベット額を提案
    """

    # 分割資金
    base_unit = 10000  # 仮に元資金が10000円前提
    wave1 = [100, 300, 900]  # 第一波の配分（例：1300円 → 100:300:900）

    losses = [r for r in records if r["結果"] == "不的中"]
    loss_count = len(losses) % 3

    # 波数に応じてベット額変化（最大3連敗まで）
    try:
        return wave1[loss_count]
    except IndexError:
        return 100  # リセット（またはエラー対策）
