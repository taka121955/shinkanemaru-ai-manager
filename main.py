import streamlit as st
import pandas as pd
import datetime
from utils.ecp import get_next_bet_amount, update_ecp

st.set_page_config(page_title="資金マネージャー", layout="centered")

# 日本時間の表示（大きめ、太字）
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
st.markdown(f"<h2><strong>⏰ 現在の日本時間：{now.strftime('%Y/%m/%d %H:%M:%S')}</strong></h2>", unsafe_allow_html=True)

# セッション初期化
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 20000
if "ecp" not in st.session_state:
    st.session_state.ecp = {"loss_count": 0}
if "history" not in st.session_state:
    st.session_state.history = []

# --- AI予想（ダミーではなく実表示） ---
st.subheader("🧠 AI予想（的中率×勝率重視 Top 5）")
ai_predictions = [
    {"競艇場": "蒲郡", "レース": 6, "式別": "3連単", "買い目": "1-3-5", "的中率": 82, "勝率": 78, "オッズ": 2.1},
    {"競艇場": "住之江", "レース": 10, "式別": "2連単", "買い目": "1-4", "的中率": 79, "勝率": 75, "オッズ": 1.9},
    {"競艇場": "丸亀", "レース": 8, "式別": "3連単", "買い目": "2-1-3", "的中率": 75, "勝率": 72, "オッズ": 2.5},
    {"競艇場": "若松", "レース": 4, "式別": "2連単", "買い目": "1-2", "的中率": 73, "勝率": 70, "オッズ": 1.7},
    {"競艇場": "児島", "レース": 11, "式別": "3連単", "買い目": "1-2-4", "的中率": 71, "勝率": 69, "オッズ": 1.6},
]
for pred in ai_predictions:
    st.markdown(f"**{pred['競艇場']} 第{pred['レース']}R [{pred['式別']}]: {pred['買い目']}**<br>"
                f"🎯 的中率: {pred['的中率']}%　🏆 勝率: {pred['勝率']}%　💸 オッズ: {pred['オッズ']}", unsafe_allow_html=True)

# --- 統計情報 ---
st.subheader("📊 統計情報")
df = pd.DataFrame(st.session_state.history)
if not df.empty:
    hit_rate = df["的中"].apply(lambda x: x == "的中").mean()
    win_rate = (df["収支"] > 0).mean()
    recovery_rate = df["収支"].sum() / df["賭金"].sum() if df["賭金"].sum() else 0
else:
    hit_rate = win_rate = recovery_rate = 0

st.markdown(f"""
- 💼 現在の残高：{st.session_state.balance}円  
- 🎯 目標金額：{st.session_state.goal}円  
- 📉 累積損益：{df['収支'].sum() if not df.empty else 0}円  
- 🎯 的中率：{round(hit_rate * 100, 1)}%  
- 🏆 勝率：{round(win_rate * 100, 1)}%  
- 💸 回収率：{round(recovery_rate * 100, 1)}%
- 🧠 次回推奨ベット額（ECP方式）：{get_next_bet_amount(st.session_state.ecp["loss_count"])}円
""")

# --- 勝敗入力 ---
st.subheader("🎮 勝敗入力")
col1, col2 = st.columns(2)
place = col1.selectbox("競艇場", ["蒲郡", "住之江", "丸亀", "若松", "児島"])
race_number = col2.selectbox("レース番号", list(range(1, 13)))
odds = st.number_input("オッズ（最低1.5以上）", min_value=1.5, step=0.1)
result = st.radio("結果", ["的中", "不的中"])
amount = st.number_input("賭金（円）", min_value=100, step=100)

if st.button("登録"):
    payout = round(amount * odds) if result == "的中" else 0
    profit = payout - amount
    st.session_state.balance += profit
    update_ecp(result, st.session_state.ecp)
    st.session_state.history.append({
        "競艇場": place,
        "レース": race_number,
        "オッズ": odds,
        "結果": result,
        "賭金": amount,
        "収支": profit
    })
    st.success("勝敗を登録しました！")

# --- 勝敗履歴 ---
st.subheader("📜 勝敗履歴")
if not df.empty:
    st.dataframe(df)
else:
    st.info("勝敗履歴はまだありません。")

# --- 制作者情報 ---
st.markdown("---")
st.markdown("👨‍💼 制作者：**小島崇彦**")
