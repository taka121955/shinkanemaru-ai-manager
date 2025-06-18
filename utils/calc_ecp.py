def calculate_ecp_amount(result_type="外れ"):
    # 仮のECP金額ロジック
    if result_type == "的中":
        return 100
    else:
        return 300  # 外れ時にベット額増加（例）
