import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="資金管理アプリ", layout="wide")

# 初期セッション状態
if "data" not in st.session_state:
    st.session_state.data = []

if "balance" not in st.session_state:
    st.session_state.balance = 10000

if "goal" not in st.session_state:
    st.session_state.goal = 20000

# ユーザーインターフェース
st.markdown(f"### 🕙 現在の日本時間：**<span style='font-size:28px;font-weight:bold'>{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}</span>**", unsafe_allow_html=True)

# ダミーAI予想（仮でなく固定）
st.subheader("🧠 AI予想（勝率・的中率重視）")
ai_predictions = [
    {"競艇場": "平和島", "レース": "1R", "式別": "3連単", "艇番": "1-2-3", "オッズ": 5.6},
    {"競艇場": "住之江", "レース": "2R", "式別": "2連単", "艇番": "2-4", "オッズ": 3.8},
    {"競艇場": "戸田", "レース": "3R", "式別": "単勝", "艇番": "6", "オッズ": 2.1},
    {"競艇場": "浜名湖", "レース": "4R", "式別": "3連単", "艇番": "1-3-4", "オッズ": 7.4},
    {"競艇場": "徳山", "レース": "5R", "式別": "2連単", "艇番": "5-1", "オッズ": 4.9},
]

df_ai = pd.DataFrame(ai_predictions)
st.table(df_ai)

# 統計
df = pd.DataFrame(st.session_state.data)
if not df.empty:
    total_bet = df["賭金"].sum()
    total_return = df["払戻"].sum()
    win_count = df[df["的中"] == "的中"].shape[0]
    hit_rate = win_count / len(df) * 100
    recovery_rate = (total_return / total_bet) * 100 if total_bet else 0
else:
    total_bet = total_return = win_count = hit_rate = recovery_rate = 0

# 統計情報
st.subheader("📊 統計データ")
st.markdown(f"""
- 💼 現在の残高：{st.session_state.balance}円  
- 🎯 目標金額：{st.session_state.goal}円  
- 📈 累積損益：{total_return - total_bet}円  
- 🎯 的中率：{round(hit_rate, 1)}%  
- 💸 回収率：{round(recovery_rate, 1)}%
""")

# 勝敗入力
st.subheader("📝 勝敗入力")
col1, col2, col3 = st.columns(3)
with col1:
    place = st.selectbox("競艇場", ["平和島", "住之江", "戸田", "浜名湖", "徳山"])
with col2:
    race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
with col3:
    bet_amount = st.number_input("賭金（円）", min_value=100, step=100)

col4, col5 = st.columns(2)
with col4:
    odds = st.number_input("オッズ", min_value=1.5, step=0.1)
with col5:
    result = st.radio("的中/不的中", ["的中", "不的中"])

# 登録処理
if st.button("記録を追加"):
    payout = int(bet_amount * odds) if result == "的中" else 0
    st.session_state.data.append({
        "日時": datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
        "競艇場": place,
        "レース": race,
        "賭金": bet_amount,
        "オッズ": odds,
        "的中": result,
        "払戻": payout,
        "収支": payout - bet_amount
    })
    st.session_state.balance += payout - bet_amount
    st.success("記録を追加しました。")

# 履歴表示
st.subheader("📚 勝敗履歴")
if df.empty:
    st.info("記録がまだありません。")
else:
    df = pd.DataFrame(st.session_state.data)
    st.dataframe(df)

# 制作者情報
st.markdown("---")
st.markdown("#### 👤 制作者：小島崇彦")
