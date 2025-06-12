import streamlit as st
import pandas as pd
from datetime import datetime
from pytz import timezone

# データベースの初期化
if "results" not in st.session_state:
    st.session_state.results = []

# 日本時間の現在時刻
japan_time = datetime.now(timezone("Asia/Tokyo")).strftime("%Y/%m/%d %H:%M:%S")
st.markdown("🕰️ **現在の日本時間**")
st.markdown(f"### {japan_time}")

# 予想表示（仮 → 本番表示）
ai_predictions = [
    {"場": "桐生", "レース": "8R", "式別": "3連複", "艇番": "1-2-4", "オッズ": 7.5},
    {"場": "住之江", "レース": "1R", "式別": "単勝", "艇番": "3", "オッズ": 2.1},
    {"場": "福岡", "レース": "10R", "式別": "2連単", "艇番": "1-2", "オッズ": 3.9},
    {"場": "不明", "レース": "5R", "式別": "3連単", "艇番": "1-4-2", "オッズ": None},
    {"場": "不明", "レース": "7R", "式別": "3連単", "艇番": "3-1-2", "オッズ": None}
]

st.markdown("## 🧠AI予想（的中率 × 勝率重視）")
for pred in ai_predictions:
    odds_display = f"{pred['オッズ']}倍" if pred['オッズ'] else "不明"
    st.markdown(
        f"📍{pred['場']} 第{pred['レース']}｜式別：{pred['式別']}｜艇番：{pred['艇番']}｜オッズ：{odds_display}"
    )

# 統計データの計算
df = pd.DataFrame(st.session_state.results)
total_bets = df["賭金"].sum() if not df.empty else 0
total_return = (df["賭金"] * df["オッズ"] * (df["結果"] == "的中")).sum() if not df.empty else 0
wins = (df["結果"] == "的中").sum() if not df.empty else 0
win_rate = (wins / len(df)) * 100 if not df.empty else 0
success_rate = win_rate
recovery_rate = (total_return / total_bets) * 100 if total_bets > 0 else 0
profit = total_return - total_bets
balance = 10000 + profit
target = 20000

st.markdown("## 📊統計データ")
st.markdown(f"- 💼 現在の残高：{int(balance)}円")
st.markdown(f"- 🎯 目標金額：{target}円")
st.markdown(f"- 🧾 累積損益：{int(profit)}円")
st.markdown(f"- 🎯 的中率：{success_rate:.1f}%")
st.markdown(f"- 🏆 勝率：{win_rate:.1f}%")
st.markdown(f"- 💴 回収率：{recovery_rate:.1f}%")
st.markdown(f"- 🧠 次回推奨賭金（ECP方式）：{100 if profit >= 0 else 300}円")

# 勝敗入力フォーム
st.markdown("## 🎮勝敗入力")
with st.form(key="form"):
    col1, col2 = st.columns(2)
    date = col1.date_input("日付", datetime.now()).strftime("%Y/%m/%d")
    stadium = col2.selectbox("競艇場", ["住之江", "丸亀", "大村", "蒲郡", "福岡", "平和島"])

    col3, col4 = st.columns(2)
    race = col3.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
    odds = col4.number_input("オッズ（1.5以上）", min_value=1.5, step=0.01, value=1.5)

    bet = st.number_input("賭金", min_value=100, step=100, value=100)

    result = st.radio("結果", ["的中", "不的中"])

    submitted = st.form_submit_button("記録する")
    if submitted:
        st.session_state.results.append({
            "日付": date,
            "競艇場": stadium,
            "レース": race,
            "オッズ": odds,
            "賭金": bet,
            "結果": result
        })
        st.success("✅記録しました！")

# 履歴表示
st.markdown("## 📖勝敗履歴")
if not df.empty:
    st.dataframe(df[::-1], use_container_width=True)

# クレジット
st.markdown("---")
st.markdown("制作者：小島崇彦")
