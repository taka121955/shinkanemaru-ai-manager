import streamlit as st
import pandas as pd
import datetime
from utils.ecp import get_next_bet_amount

st.set_page_config(page_title="新金丸AI資金マネージャー", layout="centered")
st.title("🎯 新金丸AI × ECP方式 資金マネージャー")
jst_now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
st.caption(f"🕒 日本時間：{jst_now.strftime('%Y/%m/%d %H:%M:%S')}")

# 初期値
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 20000
if "ecp" not in st.session_state:
    st.session_state.ecp = {"loss_count": 0}
if "history" not in st.session_state:
    st.session_state.history = []

# 資金入力
st.subheader("💼 資金設定")
col1, col2 = st.columns(2)
with col1:
    st.session_state.balance = st.number_input("現在の残高（円）", value=st.session_state.balance, step=100)
with col2:
    st.session_state.goal = st.number_input("目標金額（円）", value=st.session_state.goal, step=100)

# 勝敗入力
st.subheader("🎯 勝敗入力")
col3, col4 = st.columns(2)
with col3:
    race_result = st.radio("レース結果", ["未入力", "的中", "外れ"], index=0)
with col4:
    odds = st.number_input("オッズ（的中時）", min_value=1.5, value=1.5, step=0.1)

bet_amount = get_next_bet_amount(st.session_state.ecp["loss_count"])

# AI予想（仮）
st.subheader("🧠 AI予想（的中率 × 勝率重視）")
ai_predictions = [
    {"競艇場": "多摩川", "レース": 5, "式別": "3連単", "予想": "1-3-4"},
    {"競艇場": "児島", "レース": 7, "式別": "3連単", "予想": "2-1-5"},
    {"競艇場": "丸亀", "レース": 4, "式別": "3連単", "予想": "3-4-1"},
    {"競艇場": "住之江", "レース": 10, "式別": "3連単", "予想": "4-1-2"},
    {"競艇場": "若松", "レース": 6, "式別": "3連単", "予想": "5-2-1"},
]
for pred in ai_predictions:
    st.markdown(f"- 📍{pred['競艇場']} {pred['レース']}R [{pred['式別']}]: **{pred['予想']}**")

# 結果記録
if st.button("✅ 結果を記録"):
    if race_result == "的中":
        profit = int(bet_amount * (odds - 1))
        st.session_state.balance += profit
        st.session_state.ecp["loss_count"] = 0
        outcome = "的中"
    elif race_result == "外れ":
        st.session_state.balance -= bet_amount
        st.session_state.ecp["loss_count"] += 1
        outcome = "外れ"
    else:
        outcome = "未入力"

    if race_result != "未入力":
        st.session_state.history.append({
            "日付": jst_now.strftime("%Y/%m/%d %H:%M:%S"),
            "結果": outcome,
            "ベット額": bet_amount,
            "オッズ": odds,
            "収支": profit if outcome == "的中" else -bet_amount,
            "残高": st.session_state.balance
        })
        st.success("記録しました！")

# 成績表示
df = pd.DataFrame(st.session_state.history)
if not df.empty:
    hit_rate = (df["結果"] == "的中").mean()
    win_rate = (df["収支"] > 0).mean()
    recovery_rate = df["収支"].sum() / df["ベット額"].sum() + 1 if df["ベット額"].sum() > 0 else 0
else:
    hit_rate = win_rate = recovery_rate = 0

st.markdown(f"""
- 💼 現在の残高：{st.session_state.balance}円  
- 🎯 目標金額：{st.session_state.goal}円  
- 📉 累積損益：{df['収支'].sum() if not df.empty else 0}円  
- 🎯 的中率：{round(hit_rate * 100, 1)}%  
- 🏆 勝率：{round(win_rate * 100, 1)}%  
- 💸 回収率：{round(recovery_rate * 100, 1)}%
- 🧠 次回推奨ベット額（ECP方式）：{bet_amount}円
""")

if not df.empty:
    st.dataframe(df[::-1], use_container_width=True)

# リセット
if st.button("🔄 1からスタート（記録リセット）"):
    st.session_state.balance = 10000
    st.session_state.goal = 20000
    st.session_state.ecp = {"loss_count": 0}
    st.session_state.history = []
    st.success("リセットしました。")
