import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

st.set_page_config(layout="wide")

# 日本時間の表示
jst = pytz.timezone('Asia/Tokyo')
now = datetime.now(jst).strftime("%Y/%m/%d %H:%M:%S")
st.markdown("### 🕓現在の日本時間")
st.markdown(f"## **{now}**")

# AI予想（ダミーデータ）
st.markdown("## 🧠AI予想（中率×勝率重視）")
ai_predictions = [
    {"場": "桐生", "R": "8R", "式別": "3連複", "予想": "1-2-4", "オッズ": 7.5},
    {"場": "住之江", "R": "1R", "式別": "単勝", "予想": "3", "オッズ": 2.1},
    {"場": "福岡", "R": "10R", "式別": "2連単", "予想": "1-2", "オッズ": 3.9},
]
for pred in ai_predictions:
    st.markdown(f"📍{pred['場']} 第{pred['R']}｜{pred['式別']}：{pred['予想']}｜オッズ：{pred['オッズ']}")

# セッション状態初期化
if "records" not in st.session_state:
    st.session_state.records = []

# 統計計算
df = pd.DataFrame(st.session_state.records)
total_bets = df["賭金"].sum() if not df.empty else 0
wins = df[df["的中/不的中"] == "的中"]
win_rate = len(wins) / len(df) * 100 if not df.empty else 0
hit_rate = len(wins) / len(df) * 100 if not df.empty else 0
profit = (df["収支"].sum() if "収支" in df.columns else 0) if not df.empty else 0
recovery = (df["収支"].sum() / total_bets * 100) if total_bets != 0 else 0

# ECP方式の次回賭金
loss_count = len(df[df["的中/不的中"] == "不的中"]) if not df.empty else 0
ecp_bet = [100, 300, 900]
next_bet = ecp_bet[loss_count] if loss_count < len(ecp_bet) else 100

# 統計情報
st.markdown("## 📊統計情報")
st.markdown(f"- 💼現在の残高：{10000 + profit}円")
st.markdown(f"- 🎯目標金額：20000円")
st.markdown(f"- 📉累積損益：{profit}円")
st.markdown(f"- 🎯的中率：{hit_rate:.1f}%")
st.markdown(f"- 🏆勝率：{win_rate:.1f}%")
st.markdown(f"- 💸回収率：{recovery:.1f}%")
st.markdown(f"- 🧠次回推奨賭金（ECP方式）：{next_bet}円")

# 勝敗入力
st.markdown("## 🎮勝敗入力")
with st.form("input_form"):
    col1, col2 = st.columns(2)
    date = col1.date_input("日付", value=datetime.now(jst).date())
    place = col2.selectbox("競艇場", ["住之江", "桐生", "福岡", "平和島", "大村", "若松"])
    race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
    odds = st.number_input("オッズ（1.5以上）", min_value=1.5, value=1.5, step=0.1)
    amount = st.number_input("賭金", min_value=100, step=100, value=100)
    result = st.radio("結果", ["的中", "不的中"])
    submitted = st.form_submit_button("記録")

    if submitted:
        gain = int(amount * odds) if result == "的中" else 0
        st.session_state.records.append({
            "日付": date.strftime("%Y-%m-%d"),
            "競艇場": place,
            "レース": race,
            "オッズ": odds,
            "賭金": amount,
            "的中/不的中": result,
            "収支": gain - amount
        })
        st.success("✅記録しました！")

# 勝敗履歴表示
st.markdown("## 📖勝敗履歴")
if st.session_state.records:
    df = pd.DataFrame(st.session_state.records)
    st.dataframe(df)

# 制作者表記
st.markdown("#### 制作者：小島崇彦")
