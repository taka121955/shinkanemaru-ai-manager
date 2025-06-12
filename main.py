import streamlit as st
import pandas as pd
from datetime import datetime
from utils.ecp import get_next_bet_amount

st.set_page_config(page_title="新金丸AI資金マネージャー", layout="centered")

st.title("💰 新金丸AI資金マネージャー")
st.markdown("### 📊 AI予想とECP方式に基づく資金管理")

if "history" not in st.session_state:
    st.session_state.history = []
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 20000
if "ecp" not in st.session_state:
    st.session_state.ecp = {"loss_count": 0}

# --- 統計処理 ---
df = pd.DataFrame(st.session_state.history)
if not df.empty:
    total_bets = len(df)
    wins = df[df["的中／不的中"] == "的中"]
    hit_rate = len(wins) / total_bets if total_bets else 0
    win_rate = len(wins[wins["収支"] > 0]) / total_bets if total_bets else 0
    recovery_rate = df["収支"].sum() / df["賭金"].sum() if df["賭金"].sum() > 0 else 0
    cumulative_profit = df["収支"].sum()
else:
    hit_rate = win_rate = recovery_rate = cumulative_profit = 0

# --- 時刻（日本時間） ---
japan_time = datetime.utcnow().astimezone().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"### 🕒 日本時間：<span style='color:green;font-size:24px;font-weight:bold'>{japan_time}</span>", unsafe_allow_html=True)

# --- ステータス ---
next_bet = get_next_bet_amount(
    st.session_state.ecp["loss_count"],
    st.session_state.balance,
    cumulative_profit
) if cumulative_profit <= 0 else 100

st.markdown(f"""
- 💼 現在の残高：{st.session_state.balance}円  
- 🎯 目標金額：{st.session_state.goal}円  
- 📉 累積損益：{cumulative_profit}円  
- 🎯 的中率：{round(hit_rate * 100, 1)}%  
- 🏆 勝率：{round(win_rate * 100, 1)}%  
- 💸 回収率：{round(recovery_rate * 100, 1)}%  
- 🧠 次回推奨ベット額（ECP方式）：{next_bet}円
""")

st.markdown("---")

# --- 入力フォーム ---
st.markdown("### 🎯 勝敗入力")
with st.form("bet_form"):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        stadium = st.selectbox("競艇場", ["住之江", "戸田", "平和島", "大村", "蒲郡"])
    with col2:
        race_number = st.selectbox("レース番号", list(range(1, 13)))
    with col3:
        odds = st.number_input("オッズ", min_value=1.5, step=0.1)
    with col4:
        result = st.selectbox("結果", ["的中", "不的中"])
    amount = st.number_input("賭金（円）", min_value=100, step=100)

    submitted = st.form_submit_button("記録する")
    if submitted:
        payout = int(amount * odds) if result == "的中" else 0
        profit = payout - amount
        st.session_state.balance += profit

        if result == "不的中":
            st.session_state.ecp["loss_count"] += 1
        else:
            st.session_state.ecp["loss_count"] = 0

        st.session_state.history.append({
            "競艇場": stadium,
            "レース": f"{race_number}R",
            "オッズ": odds,
            "的中／不的中": result,
            "賭金": amount,
            "払戻": payout,
            "収支": profit
        })
        st.success("✅ 記録を追加しました。")

# --- 履歴表示 ---
if not df.empty:
    st.markdown("### 🗂️ 勝敗履歴")
    st.dataframe(df[::-1], use_container_width=True)

# --- リセット ---
if st.button("🔁 1からスタート（履歴削除）"):
    st.session_state.history = []
    st.session_state.balance = 10000
    st.session_state.ecp = {"loss_count": 0}
    st.success("🔄 全記録をリセットしました。")
