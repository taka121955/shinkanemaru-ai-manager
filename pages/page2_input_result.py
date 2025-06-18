# pages/page2_input_result.py

import streamlit as st
from utils.calc_ecp import calculate_ecp_amount

def show_page():
    st.title("② 勝敗入力")

    # 勝敗選択
    result = st.radio("勝敗", ["的中", "不的中"], index=1)

    # オッズ入力
    odds = st.number_input("オッズ", min_value=1.0, max_value=100.0, value=1.5, step=0.1)

    # 資金モード選択
    st.markdown("💰 **ベット金額（ECP方式で自動計算）**")
    fund = st.radio("資金モード", [1300, 3900, 10000], format_func=lambda x: f"{x}円")

    # 自動ベット金額を計算
    bet_amount = calculate_ecp_amount(result, odds, fund)

    st.markdown(f"### 💸 自動ベット金額：`{bet_amount}` 円")

    if st.button("登録する"):
        st.success("✅ 登録が完了しました（仮処理）")

# 呼び出し
show_page()
