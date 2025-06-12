import streamlit as st
import pandas as pd
from datetime import datetime
from utils.ecp import get_next_bet_amount

st.set_page_config(page_title="AI予想 × 新金丸法 × 資金マネージャー", layout="wide")

# --- 初期化 ---
if "history" not in st.session_state:
    st.session_state.history = []

if "balance" not in st.session_state:
    st.session_state.balance = 10000

if "goal" not in st.session_state:
    st.session_state.goal = 20000

if "ecp" not in st.session_state:
    st.session_state.ecp = {"loss_count": 0}

# --- 勝敗入力フォーム ---
st.title("📝 勝敗入力")

col1, col2, col3, col4, col5 = st.columns(5)

venue = col1.selectbox("競艇場", ["若松", "住之江", "丸亀", "大村", "平和島", "蒲郡"])
race_number = col2.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
odds = col3.number_input("オッズ（1.5以上）", min_value=1.5, step=0.1)
bet_amount = col4.number_input("賭金", min_value=100, step=100)
result = col5.radio("的中／不的中", ["的中", "不的中"])

if st.button("記録"):
    payout = int(bet_amount * odds) if result == "的中" else 0
    profit = payout - bet_amount
    st.session_state.history.append({
        "日付": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "競艇場": venue,
        "レース": race_number,
        "オッズ": odds,
        "賭金": bet_amount,
        "的中": result,
        "収支": profit
    })

    st.session_state.balance += profit
    if profit < 0:
        st.session_state.ecp["loss_count"] += 1
    else:
        st.session_state.ecp["loss_count"] = 0

    st.success("✅ 記録を保存しました。")

# --- 統計情報 ---
df = pd.DataFrame(st.session_state.history)

st.header("📊 統計情報")

hit_count = len(df[df["的中"] == "的中"]) if not df.empty and "的中" in df else 0
win_count = hit_count
loss_count = len(df[df["的中"] == "不的中"]) if not df.empty and "的中" in df else 0
total_bets = len(df)
cumulative_profit = df["収支"].sum() if not df.empty else 0

hit_rate = hit_count / total_bets if total_bets > 0 else 0
win_rate = win_count / total_bets if total_bets > 0 else 0
recovery_rate = df["収支"].sum() / df["賭金"].sum() if not df.empty and df["賭金"].sum() > 0 else 0

next_bet = get_next_bet_amount(st.session_state.ecp["loss_count"])
if cumulative_profit > 0:
    next_bet = 100

st.markdown(f'''
### 📈 統計情報
- 💼 現在の残高：{st.session_state.balance}円  
- 🎯 目標金額：{st.session_state.goal}円  
- 📉 累積損益：{cumulative_profit}円  
- 🎯 的中率：{round(hit_rate * 100, 1)}%  
- 🏆 勝率：{round(win_rate * 100, 1)}%  
- 💸 回収率：{round(recovery_rate * 100, 1)}%  
- 🧠 次回推奨ベット額（ECP方式）：{next_bet}円  
- 🕒 日本時間：**{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}**
''')

# --- 勝敗履歴 ---
st.header("📊 勝敗履歴")
st.dataframe(df)
