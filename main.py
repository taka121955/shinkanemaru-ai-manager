import streamlit as st
import pandas as pd
import os
import csv
from datetime import datetime
import pytz

from utils.ecp import get_next_bet_amount, update_ecp
from utils.ai_predictor import get_ai_predictions

st.set_page_config(page_title="資金マネージャー", layout="wide")
st.title("📊資金管理 × 🤖AI予想")

# 現在の日本時間表示
st.markdown("🕰️ **現在の日本時間**")
jst_now = datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y/%m/%d %H:%M:%S')
st.write(jst_now)

# AI予想（5件）
st.markdown("🧠 **AI予想（的中率 × 勝率重視）**")
predictions = get_ai_predictions()
for pred in predictions[:5]:
    st.markdown(f"📍{pred['場']} 第{pred['レース']}R｜式別：{pred['式別']}｜艇番：{pred['艇番']}｜オッズ：{pred.get('オッズ', '不明')}倍")

# 統計情報読み込み
file_path = "data/records.csv"
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    df["収支"] = df.apply(lambda row: row["賭金"] * row["オッズ"] - row["賭金"] if row["結果"] == "的中" else -row["賭金"], axis=1)
else:
    df = pd.DataFrame(columns=["日付", "競艇場", "レース", "オッズ", "賭金", "結果", "収支"])

# 統計データ表示
initial_balance = 10000
target_balance = 20000
current_balance = initial_balance + df["収支"].sum()
wins = df[df["結果"] == "的中"]
total_bets = len(df)
hit_rate = len(wins) / total_bets * 100 if total_bets else 0
win_rate = hit_rate
recovery_rate = (df["収支"].sum() / df["賭金"].sum()) * 100 if df["賭金"].sum() > 0 else 0
next_bet = get_next_bet_amount(current_balance - initial_balance)

st.markdown("📊 **統計データ**")
st.markdown(f"- 💼 現在の残高：{int(current_balance)}円")
st.markdown(f"- 🎯 目標金額：{target_balance}円")
st.markdown(f"- 📄 累積損益：{int(current_balance - initial_balance)}円")
st.markdown(f"- 🎯 的中率：{hit_rate:.1f}%")
st.markdown(f"- 🏆 勝率：{win_rate:.1f}%")
st.markdown(f"- 💸 回収率：{recovery_rate:.1f}%")
st.markdown(f"- 🧠 次回推奨賭金（ECP方式）：{int(next_bet)}円")

# 勝敗入力
st.markdown("🎮 **勝敗入力**")
with st.form(key="record_form"):
    date = st.date_input("日付", datetime.now(pytz.timezone('Asia/Tokyo')))
    place = st.selectbox("競艇場", ["大村", "住之江", "丸亀", "蒲郡", "福岡", "桐生", "平和島"])
    race_number = st.text_input("レース番号", value="1R")
    odds = st.number_input("オッズ（1.5以上）", min_value=1.5, step=0.01)
    bet_amount = st.number_input("賭金", min_value=100, step=100)
    result = st.radio("結果", ["的中", "不的中"])
    submitted = st.form_submit_button("記録する")

    if submitted:
        with open(file_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([date, place, race_number, odds, bet_amount, result])
        st.success("✅ 記録しました！")
        st.rerun()

# 履歴表示
st.markdown("📖 **勝敗履歴**")
st.dataframe(df[::-1], use_container_width=True)

# CSVダウンロード
st.download_button("📥 データをダウンロード", data=df.to_csv(index=False).encode("utf-8"), file_name="bet_record.csv")

st.markdown("---")
st.markdown("制作：小島崇彦")
