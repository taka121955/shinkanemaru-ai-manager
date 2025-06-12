import streamlit as st
import pandas as pd
from utils.ecp import get_next_bet_amount, reset_ecp

st.set_page_config(page_title="新金丸法 × ECP 資金マネージャー", layout="centered")

# 初期化
if "records" not in st.session_state:
    st.session_state.records = []
if "ecp_state" not in st.session_state:
    st.session_state.ecp_state = reset_ecp()
if "initial_capital" not in st.session_state:
    st.session_state.initial_capital = 10000
if "target_capital" not in st.session_state:
    st.session_state.target_capital = 20000

st.title("💸 新金丸法 × ECP 資金マネージャー")

# 資金設定
with st.form("資金設定", clear_on_submit=False):
    col1, col2 = st.columns(2)
    with col1:
        initial = st.number_input("初期資金（円）", min_value=100, value=st.session_state.initial_capital, step=100)
    with col2:
        target = st.number_input("目標金額（円）", min_value=100, value=st.session_state.target_capital, step=100)
    if st.form_submit_button("設定反映"):
        st.session_state.initial_capital = initial
        st.session_state.target_capital = target
        st.success("資金設定を更新しました")

# 🧠 AI予想（簡易版：ランダム予想）
import random
st.subheader("🔮AIの予想")
ai_prediction = {
    "競艇場": random.choice(["住之江", "丸亀", "大村", "多摩川"]),
    "レース": f"{random.randint(1, 12)}R",
    "理由": random.choice(["初戦", "波穏やか", "展示タイム好調", "イン逃げ傾向"])
}
st.markdown(f"🏟️：{ai_prediction['競艇場']} 🎯：{ai_prediction['レース']} 🧠理由：{ai_prediction['理由']}")

# ベット入力
st.subheader("🎯ベット記録入力")
col1, col2 = st.columns(2)
with col1:
    place = st.selectbox("競艇場名", ["住之江", "丸亀", "大村", "多摩川", "蒲郡", "児島", "芦屋"])
with col2:
    race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])

col3, col4, col5 = st.columns(3)
with col3:
    amount = st.number_input("賭け金額（円）", min_value=100, step=100)
with col4:
    odds = st.number_input("オッズ（1.0以上）", min_value=1.0, value=1.5, step=0.1)
with col5:
    result = st.radio("結果", ["的中", "不的中"], horizontal=True)

if st.button("記録する"):
    profit = amount * (odds - 1) if result == "的中" else -amount
    st.session_state.records.append({
        "競艇場": place,
        "レース": race,
        "賭け金": amount,
        "オッズ": odds,
        "結果": result,
        "収支": int(profit)
    })

# 決算表
st.subheader("📋 決算表")
if st.session_state.records:
    df = pd.DataFrame(st.session_state.records)
    df["累積収支"] = df["収支"].cumsum() + st.session_state.initial_capital
    st.dataframe(df, use_container_width=True)

    total_profit = df["収支"].sum()
    current_balance = st.session_state.initial_capital + total_profit
    win_count = df[df["結果"] == "的中"].shape[0]
    total_count = df.shape[0]
    hit_rate = (win_count / total_count * 100) if total_count else 0
    win_rate = hit_rate  # 競艇1点買い想定
    investment = df["賭け金"].sum()
    return_rate = ((df["収支"].sum() + investment) / investment * 100) if investment > 0 else 0

    st.markdown(f"📈累積損益：{int(total_profit)}円")
    st.markdown(f"🎯の中間率：{hit_rate:.1f}%")
    st.markdown(f"🏆勝率：{win_rate:.1f}%")
    st.markdown(f"💸回収率：{return_rate:.1f}%")
    st.markdown(f"💼現在の残高：{int(current_balance)}円")

    # ECP次回ベット額
    bet = get_next_bet_amount(st.session_state.ecp_state)
    st.markdown(f"🧠次回推奨ベット額（ECP）：{bet}円")
else:
    st.info("まだ記録がありません。")

# リセット
if st.button("1からスタート"):
    st.session_state.records = []
    st.session_state.ecp_state = reset_ecp()
    st.experimental_rerun()
