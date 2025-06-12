import streamlit as st
import pandas as pd
from datetime import datetime
from utils.ecp import get_next_bet_amount

# セッション初期化
if 'data' not in st.session_state:
    st.session_state.data = []

if 'balance' not in st.session_state:
    st.session_state.balance = 10000

if 'goal' not in st.session_state:
    st.session_state.goal = 20000

if 'ecp' not in st.session_state:
    st.session_state.ecp = {'loss_count': 0}

# 競艇場とレース番号（プルダウン用）
boat_races = ["若松", "住之江", "大村", "丸亀", "平和島", "芦屋", "常滑", "蒲郡", "津", "唐津", "徳山", "宮島"]
race_numbers = [f"{i}R" for i in range(1, 13)]

# 現在時刻（日本時間）
jst = datetime.utcnow().astimezone()
st.markdown(f"<h4>🕐 日本時間：<b>{jst.strftime('%Y-%m-%d %H:%M:%S')}</b></h4>", unsafe_allow_html=True)

st.title("📝 勝敗入力")

# 入力UI
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    stadium = st.selectbox("競艇場", boat_races)
with col2:
    race_number = st.selectbox("レース番号", race_numbers)
with col3:
    odds = st.number_input("オッズ（1.5以上）", min_value=1.5, step=0.1)
with col4:
    bet_amount = st.number_input("賭金", min_value=0, step=100)
with col5:
    result = st.radio("的中", ["的中", "不的中"])

# 登録
if st.button("記録"):
    payout = int(bet_amount * odds) if result == "的中" else 0
    profit = payout - bet_amount
    st.session_state.data.append({
        "日付": jst.strftime('%Y-%m-%d'),
        "競艇場": stadium,
        "レース": race_number,
        "オッズ": odds,
        "賭金": bet_amount,
        "的中": result,
        "収支": profit
    })

    st.session_state.balance += profit

    # ECP方式：負けた回数カウント
    if result == "的中":
        st.session_state.ecp["loss_count"] = 0
    else:
        st.session_state.ecp["loss_count"] += 1

    st.success("✅ 記録を保存しました。")

# 統計表示
df = pd.DataFrame(st.session_state.data)
hit_count = len(df[df["的中"] == "的中"])
total_count = len(df)
hit_rate = hit_count / total_count if total_count else 0
win_rate = hit_count / total_count if total_count else 0
recovery_rate = df["収支"].sum() / df["賭金"].sum() if not df.empty and df["賭金"].sum() > 0 else 0

st.markdown("### 📊 統計情報")
st.markdown(f"""
- 💼 現在の残高：{st.session_state.balance}円  
- 🎯 目標金額：{st.session_state.goal}円  
- 📉 累積損益：{df["収支"].sum() if not df.empty else 0}円  
- 🎯 的中率：{round(hit_rate * 100, 1)}%  
- 🏆 勝率：{round(win_rate * 100, 1)}%  
- 💸 回収率：{round(recovery_rate * 100, 1)}%  
- 🧠 次回推奨ベット額（ECP方式）：{get_next_bet_amount(st.session_state.ecp["loss_count"])}円
""")

# 勝敗履歴
st.markdown("### 📉 勝敗履歴")
if not df.empty:
    st.dataframe(df)
else:
    st.info("まだ記録がありません。")
