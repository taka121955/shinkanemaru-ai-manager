import streamlit as st
import pandas as pd
import datetime
import pytz
from utils.ecp import get_next_bet_amount
from utils.ai_predictor import get_ai_predictions

st.set_page_config(page_title="AI予想 × 新金丸法 × 資金マネージャー", layout="centered")

# 📅 現在の日本時間
jst = pytz.timezone('Asia/Tokyo')
now = datetime.datetime.now(jst)
st.markdown("### 🕰️現在の日本時間")
st.markdown(f"## **{now.strftime('%Y/%m/%d %H:%M:%S')}**")

# 🤖 AI予想表示
st.markdown("## 🧠AI予想（中率×勝率重視）")
try:
    predictions = get_ai_predictions()
    for pred in predictions:
        st.markdown(f"🏁 {pred['場']} 🎯{pred['レース']}R 🧠 {pred['式別']}【{pred['艇番'] }】 スコア：{pred['score']}")
except Exception as e:
    st.error("❌ AI予想の読み込みに失敗しました")

# 📊 統計情報
st.markdown("## 📊統計情報")

if "data" not in st.session_state:
    st.session_state.data = []

df = pd.DataFrame(st.session_state.data)

hit_rate = df["的中"].value_counts().get("的中", 0) / len(df) if not df.empty else 0
win_rate = df["的中"].value_counts().get("的中", 0) / len(df) if not df.empty else 0
recovery_rate = (df["収支"].sum() / df["賭金"].sum()) if not df.empty and df["賭金"].sum() > 0 else 0

next_bet = 100 if df["収支"].sum() >= 0 else get_next_bet_amount(
    sum(1 for x in st.session_state.data if x["的中"] == "不的中"),
    st.session_state.get("balance", 10000)
)

st.markdown(f"""
- 💼 現在の残高：{st.session_state.get("balance", 10000)}円  
- 🎯 的中率：{round(hit_rate * 100, 1)}%  
- 🧠 回収率：{round(recovery_rate * 100, 1)}%  
- 🧠 次回推奨ベット額（ECP方式）：{next_bet}円
""")

# 🎯 勝敗入力
st.markdown("## ✏️勝敗入力")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    stadium = st.selectbox("競艇場", ["住之江", "大村", "丸亀", "若松", "芦屋"])
with col2:
    race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
with col3:
    odds = st.number_input("オッズ（1.5以上）", min_value=1.5, step=0.1, value=1.5)
with col4:
    bet_amount = st.number_input("賭金", min_value=100, step=100, value=100)
with col5:
    result = st.radio("的中／不的中", ["的中", "不的中"])

if st.button("記録"):
    payout = int(bet_amount * odds) if result == "的中" else 0
    profit = payout - bet_amount
    st.session_state.data.append({
        "日付": now.strftime("%Y-%m-%d %H:%M:%S"),
        "競艇場": stadium,
        "レース": race,
        "オッズ": odds,
        "賭金": bet_amount,
        "的中": result,
        "収支": profit
    })
    st.success("✅ 記録を保存しました。")

# 📘 勝敗履歴
st.markdown("## 📘勝敗履歴")
if not df.empty:
    st.dataframe(df)

# 👤 制作者名
st.markdown("---")
st.markdown("### 👤 制作者：小島崇彦")
