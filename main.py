import streamlit as st
import pandas as pd
from datetime import datetime
from utils.ecp import get_next_bet_amount, update_ecp
from utils.ai_predictor import get_ai_predictions

st.set_page_config(page_title="AI資金マネージャー", layout="centered")

st.markdown("## 🕒現在の日本時間")
now_japan = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"<h2 style='font-size: 24px; font-weight: bold'>{now_japan}</h2>", unsafe_allow_html=True)

st.markdown("## 🧠AI予想（的中率 × 勝率重視）")
ai_preds = get_ai_predictions()
for pred in ai_preds:
    st.markdown(f"📍{pred['場']} 第{pred['レース']}R | {pred['式別']}：{pred['艇番']} | オッズ：{pred['オッズ']}")

st.markdown("## 📊統計情報")

if "history" not in st.session_state:
    st.session_state.history = []

df = pd.DataFrame(st.session_state.history)

balance = 10000
target = 20000
profit = df["収支"].sum() if "収支" in df.columns else 0
wins = df[df["的中／不的中"] == "的中"] if "的中／不的中" in df.columns else pd.DataFrame()
hit_rate = len(wins) / len(df) * 100 if len(df) > 0 else 0
win_rate = hit_rate
recovery_rate = (df["収支"].sum() / df["収支"].abs().sum()) * 100 if "収支" in df.columns and df["収支"].abs().sum() > 0 else 0

loss_count = len(df[df["的中／不的中"] == "不的中"]) if "的中／不的中" in df.columns else 0
next_bet = get_next_bet_amount(loss_count, balance) if profit <= 0 else 100

st.markdown(f"""
- 💼現在の残高：{balance}円
- 🎯目標金額：{target}円
- 📈累積損益：{profit}円
- 🎯的中率：{hit_rate:.1f}%
- 🏆勝率：{win_rate:.1f}%
- 💸回収率：{recovery_rate:.1f}%
- 🧠次回推奨賭金（ECP方式）：{next_bet}円
""")

st.markdown("## 🎮勝敗入力")
with st.form("input_form"):
    date = st.date_input("日付", datetime.now()).strftime("%Y/%m/%d")
    place = st.selectbox("競艇場", ["若松", "住之江", "大村", "桐生", "平和島", "福岡"])
    race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
    odds = st.number_input("オッズ（1.5以上）", min_value=1.5, step=0.1)
    bet = st.number_input("賭金", min_value=100, step=100)
    result = st.radio("結果", ["的中", "不的中"])
    submitted = st.form_submit_button("記録")

if submitted:
    payout = int(bet * odds) if result == "的中" else 0
    profit = payout - bet
    st.session_state.history.append({
        "日付": date,
        "競艇場": place,
        "レース": race,
        "オッズ": odds,
        "賭金": bet,
        "的中／不的中": result,
        "収支": profit
    })
    update_ecp(result)
    st.success("✅ 記録しました！")

st.markdown("## 📖勝敗履歴")
if not df.empty:
    st.dataframe(df)

st.markdown("---")
st.markdown("制作：小島崇彦")
