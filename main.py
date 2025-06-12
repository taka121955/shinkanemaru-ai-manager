import streamlit as st
import pandas as pd
from utils.ecp import get_next_bet_amount, reset_ecp_state

st.set_page_config(page_title="新金丸法 × ECP 資金マネージャー", layout="centered")

if "records" not in st.session_state:
    st.session_state.records = []
if "ecp_state" not in st.session_state:
    st.session_state.ecp_state = reset_ecp_state()

st.title("💰 新金丸法 × ECP 資金マネージャー")

# 初期資金と目標金額入力
initial_capital = st.number_input("初期資金（円）", min_value=1000, step=100, value=10000)
target_capital = st.number_input("目標金額（円）", min_value=initial_capital, step=100, value=initial_capital * 2)

st.subheader("🎯 ベット記録")

col1, col2 = st.columns(2)
with col1:
    place = st.selectbox("競艇場", ["住之江", "尼崎", "大村", "蒲郡", "その他"])
with col2:
    race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])

bet_amount = get_next_bet_amount(st.session_state.ecp_state)
odds = st.number_input("オッズ（最低1.5）", min_value=1.5, step=0.1)
result = st.radio("結果", ["的中", "不的中"])

if st.button("記録する"):
    if result == "的中":
        profit = int(bet_amount * (odds - 1))
        st.session_state.ecp_state = reset_ecp_state()
    else:
        profit = -bet_amount
        st.session_state.ecp_state["losses"] += 1

    st.session_state.records.append({
        "競艇場": place,
        "レース": race,
        "賭け金": bet_amount,
        "オッズ": odds,
        "結果": result,
        "収支": profit
    })

# 1からスタート機能
if st.button("🔁 1からスタート（記録リセット）"):
    st.session_state.records = []
    st.session_state.ecp_state = reset_ecp_state()

st.subheader("📋 収支決算表")
if st.session_state.records:
    df = pd.DataFrame(st.session_state.records)
    df["累積収支"] = df["収支"].cumsum() + initial_capital
    st.dataframe(df, use_container_width=True)

    total_profit = df["収支"].sum()
    balance = initial_capital + total_profit

    win_count = df[df["結果"] == "的中"].shape[0]
    lose_count = df[df["結果"] == "不的中"].shape[0]
    total_count = win_count + lose_count
    hit_rate = (win_count / total_count) * 100 if total_count else 0
    win_rate = hit_rate
    return_rate = (df[df["結果"] == "的中"]["収支"].sum() / df["賭け金"].sum()) * 100 if df["賭け金"].sum() else 0

    st.markdown(f"### 💼 現在の残高：{balance} 円")
    st.markdown(f"### 📈 累積利益：{total_profit} 円")
    st.markdown(f"### 🎯 的中率：{hit_rate:.1f}%")
    st.markdown(f"### 🏆 勝率：{win_rate:.1f}%")
    st.markdown(f"### 💸 回収率：{return_rate:.1f}%")

    if balance >= target_capital:
        st.success("🎉 目標金額に到達しました！")
    elif balance <= 0:
        st.error("😢 資金が尽きました…")
    
    st.markdown(f"### 🧠 次回推奨ベット額（ECP）：{get_next_bet_amount(st.session_state.ecp_state)} 円")
else:
    st.info("記録がまだありません。賭け情報を入力してください。")
