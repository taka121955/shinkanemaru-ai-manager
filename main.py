import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
import os
from utils.ecp import get_next_bet_amount, update_ecp
from utils.ai_predictor import get_ai_predictions

# CSVファイルの保存先
DATA_FILE = "bet_history.csv"

# 日本時間を取得
japan_tz = pytz.timezone("Asia/Tokyo")
now = datetime.now(japan_tz).strftime("%Y/%m/%d %H:%M:%S")

st.title("🧠AI予想（的中率 × 勝率重視）")
st.markdown(f"🕰️現在の日本時間\n\n### {now}")

# 📊 AI予想
st.subheader("🧠AI予想（的中率 × 勝率重視）")
predictions = get_ai_predictions()

for pred in predictions[:5]:  # 上位5件のみ表示
    odds = f"{pred['オッズ']}倍" if pred.get("オッズ") else "不明"
    st.markdown(
        f"📍{pred['場']} 第{pred['レース']}R｜式別：{pred['式別']}｜艇番：{pred['艇番']}｜オッズ：{odds}"
    )

# 📈 統計表示
st.subheader("📊統計データ")

if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame(columns=["日付", "競艇場", "レース", "オッズ", "賭金", "結果"])

df["収支"] = df.apply(lambda row: (row["オッズ"] * row["賭金"] - row["賭金"]) if row["結果"] == "的中" else -row["賭金"], axis=1)
current_balance = 10000 + df["収支"].sum()
wins = df[df["結果"] == "的中"]
win_rate = len(wins) / len(df) * 100 if len(df) > 0 else 0
hit_rate = win_rate
recovery_rate = (df["収支"].sum() / df["賭金"].sum()) * 100 if df["賭金"].sum() > 0 else 0
next_bet = get_next_bet_amount(current_balance)

st.markdown(f"""
- 💼現在の残高：{int(current_balance)}円
- 🎯目標金額：20000円
- 🧾累積損益：{int(df['収支'].sum())}円
- 🎯的中率：{hit_rate:.1f}%
- 🏆勝率：{win_rate:.1f}%
- 💸回収率：{recovery_rate:.1f}%
- 🧠次回推奨 賭金（ECP方式） ：{next_bet}円
""")

# 📝 勝敗入力
st.subheader("🎮勝敗入力")
with st.form("bet_form"):
    col1, col2 = st.columns(2)
    with col1:
        date = st.date_input("日付", value=datetime.now(japan_tz).date())
        place = st.selectbox("競艇場", ["住之江", "平和島", "蒲郡", "大村", "桐生", "丸亀", "若松", "福岡"])
    with col2:
        race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
        odds = st.number_input("オッズ（1.5以上）", min_value=1.5, step=0.01)
        bet = st.number_input("賭金", min_value=100, step=100)
    result = st.radio("結果", ["的中", "不的中"])
    submitted = st.form_submit_button("記録する")

    if submitted:
        new_record = {
            "日付": str(date),
            "競艇場": place,
            "レース": race.replace("R", ""),
            "オッズ": odds,
            "賭金": bet,
            "結果": result
        }
        new_df = pd.DataFrame([new_record])
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)
        st.success("✅記録しました！")
        st.experimental_rerun()

# 📚 勝敗履歴表示
st.subheader("📖勝敗履歴")
st.dataframe(df.sort_values("日付", ascending=False), use_container_width=True)

st.markdown("制作者：小島崇彦")
