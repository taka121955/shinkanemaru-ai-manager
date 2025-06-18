# pages/page2_input_result.py

import streamlit as st
from utils.calc_ecp import calculate_ecp_amount

def show_page():
    st.title("② 勝敗入力")

    # ▼ 競艇場名・レース番号入力
    venue = st.text_input("🏟 競艇場名（例：唐津）")
    race_number = st.text_input("🎯 レース番号（例：1R）")

    # ▼ 勝敗選択
    result = st.radio("勝敗", ["的中", "不的中"], index=1)

    # ▼ オッズ入力
    odds = st.number_input("オッズ", min_value=1.0, max_value=100.0, value=1.5, step=0.1)

    # ▼ 資金モード選択
    st.markdown("💰 **ベット金額（ECP方式で自動計算）**")
    fund = st.radio("資金モード", [1300, 3900, 10000], format_func=lambda x: f"{x}円")

    # ▼ 自動ベット金額（3波）を計算
    bet_list = calculate_ecp_amount(result, odds, fund)

    # ▼ 表示
    st.markdown("### 💸 自動ベット金額（3波）")
    for i, val in enumerate(bet_list):
        st.markdown(f"- 第{i+1}波： `{val}` 円")

    # ▼ 登録ボタン
    if st.button("登録する"):
        st.success("✅ 登録が完了しました（仮処理）")

# 呼び出し
show_page()
