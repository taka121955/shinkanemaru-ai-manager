def get_next_bet_amount(loss_count):
    """
    ECP方式による次回賭け金の決定。
    """
    base_bets = [100, 300, 900]
    if loss_count < len(base_bets):
        return base_bets[loss_count]
    return 1300 * (2 ** (loss_count - 2))  # 2倍で増える想定


def update_ecp(result):
    """
    勝敗に応じたECPカウント更新。
    """
    import streamlit as st
    if result == "的中":
        st.session_state.ecp["loss_count"] = 0
    else:
        st.session_state.ecp["loss_count"] += 1
