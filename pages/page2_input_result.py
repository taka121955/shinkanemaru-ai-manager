import streamlit as st
from utils.calc_ecp import calculate_ecp_amount  # 自作ECP関数を使用

def show_page():
    st.title("② 勝敗入力 × 自動ベット金額 💴")

    # 入力項目
    result = st.radio("勝敗", ["的中", "不的中"])
    odds = st.number_input("オッズ", min_value=1.0, step=0.1, value=1.5)

    # 資金モード
    st.markdown("### 💰 資金モード")
    fund_mode = st.radio("選択", ["1300円", "3900円", "10000円"])

    # 金額に変換
    fund_value = {"1300円": 1300, "3900円": 3900, "10000円": 10000}[fund_mode]

    # 自動計算（1つの金額のみ表示）
    amount = calculate_ecp_amount(result, odds, fund_value)

    # 表示
    st.markdown("### ✅ 自動ベット金額")
    st.metric(label="💸 金額", value=f"{amount} 円")

    if st.button("登録する"):
        st.success("記録されました！")
