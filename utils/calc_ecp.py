def calc_ecp(mode):
    # 例：資金モードに応じたベット金額分配
    if mode == "1300円":
        return [100, 300, 900]
    elif mode == "3900円":
        return [300, 900, 2700]
    elif mode == "10000円":
        return [1000, 3000, 6000]
    else:
        return [0, 0, 0]
