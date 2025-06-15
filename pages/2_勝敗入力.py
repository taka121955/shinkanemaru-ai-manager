import streamlit as st
import pandas as pd
import os
from datetime import datetime
from utils.calc_ecp import calculate_next_bet

st.title("✍️ 勝敗入力フォーム")
st.markdown("🎯 **AI予想をベースに入力**")

# 競艇場・式別プルダウン
stadiums = ["住之江", "丸亀", "蒲郡", "常滑", "福岡", "若松", "平和島"]
formulas = ["単勝", "2連単", "3連単"]

# 初期資金・積立金セッション
if "initial_fund" not in st.session_state:
    st.session_state.initial_fund = 10000
if "reserve_fund" not in st.session_state:
    st.session_state.reserve_fund = 0

# 過去データ読み込み
csv_path = "results.csv"
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    history = df.to_dict(orient="records")
else:
    df = pd.DataFrame(columns=["日付", "競艇場", "式別", "反省内容", "賭け金", "的中", "波", "ステップ"])
    history = []

# 次の賭け金算出
bet, wave, step, updated_reserve = calculate_next_bet(
    history,
    initial_fund=st.session_state.initial_fund,
    reserve_fund=st.session_state.reserve_fund
)

if bet is None:
    st.error("❌ 資金が不足しています。リセットが必要です。")
    if st.button("🔁 リセット"):
        st.session_state.initial_fund = 10000
        st.session_state.reserve_fund = 0
        st.success("✅ 初期状態にリセットしました")
    st.stop()

# 入力フォーム
with st.form("form"):
    col1, col2 = st.columns(2)
    stadium = col1.selectbox("競艇場", stadiums)
    formula = col2.selectbox("式別", formulas)

    reflection = st.text_input("反省内容（例：1-3-4）")
    is_hit = st.checkbox("🎯 的中した")
    st.markdown(f"💰 **自動賭金（ECP）：{bet}円**")

    submitted = st.form_submit_button("✅ 登録する")
    if submitted:
        new_row = {
            "日付": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "競艇場": stadium,
            "式別": formula,
            "反省内容": reflection,
            "賭け金": bet,
            "的中": is_hit,
            "波": wave,
            "ステップ": step
        }

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(csv_path, index=False)

        # 資金更新
        if is_hit:
            st.session_state.reserve_fund += bet
        else:
            st.session_state.initial_fund -= bet

        st.success("✅ 勝敗記録を登録しました。")
