import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="新金丸AIマネージャー", layout="centered")

# タイトルと日本時間
st.title("📅現在の日本時間")
japan_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
st.header(japan_time.strftime("%Y/%m/%d %H:%M:%S"))

# データ保存用CSV
CSV_FILE = "bet_history.csv"

# データの読み込み
try:
    df = pd.read_csv(CSV_FILE)
except FileNotFoundError:
    df = pd.DataFrame(columns=["日付", "競艇場", "レース", "オッズ", "賭金", "結果", "収支"])
    df.to_csv(CSV_FILE, index=False)

# 統計データの計算
total = len(df)
hit_count = len(df[df["結果"] == "的中"])
hit_rate = round((hit_count / total) * 100, 1) if total > 0 else 0
win_rate = hit_rate
total_bet = df["賭金"].sum()
total_profit = df["収支"].sum()
recovery_rate = round((total_profit / total_bet) * 100, 1) if total_bet > 0 else 0
start_balance = 10000
current_balance = start_balance + total_profit

# 統計表示
st.subheader("📊統計データ")
st.markdown(f"""
- 💼 現在の残高：{int(current_balance)}円
- 🎯 目標金額：20000円
- 📄 累積損益：{int(total_profit)}円
- 🎯 的中率：{hit_rate}%
- 🏆 勝率：{win_rate}%
- 💸 回収率：{recovery_rate}%
- 🧠 次回推奨賭金（ECP方式）：100円
""")

# 勝敗入力フォーム
st.subheader("🎮勝敗入力")
with st.form("bet_form"):
    date = st.date_input("日付", value=datetime.date.today())
    stadium = st.selectbox("競艇場", ["住之江", "丸亀", "平和島", "蒲郡", "大村", "桐生", "若松", "福岡", "徳山"])
    race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
    odds = st.number_input("オッズ（1.5以上）", min_value=1.5, value=1.5, step=0.01)
    bet = st.number_input("賭金", min_value=100, value=100, step=100)
    result = st.radio("結果", ["的中", "不的中"])
    submitted = st.form_submit_button("記録する")

    if submitted:
        profit = int(bet * (odds - 1)) if result == "的中" else -bet
        new_data = pd.DataFrame([[str(date), stadium, race, odds, bet, result, profit]], columns=df.columns)
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)
        st.success("✅記録しました！")

# 勝敗履歴表示
st.subheader("📖勝敗履歴")
st.dataframe(df)

# フッター
st.markdown("---")
st.markdown("制作者：小島崇彦")
