import streamlit as st
import pandas as pd
from utils.ecp import get_next_bet_amount, reset_ecp
from datetime import datetime
import pytz

st.set_page_config(page_title="AI予想 × 新金丸法 × 資金マネージャー", layout="centered")
st.title("🧠AI予想 × 新金丸法 × 資金マネージャー")

# セッション初期化
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["競艇場", "レース", "賭け金", "オッズ", "結果", "収支", "累積収支"])
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 20000
if "ecp" not in st.session_state:
    st.session_state.ecp = reset_ecp()

# 日本時間
japan_time = datetime.now(pytz.timezone("Asia/Tokyo"))
st.markdown(f"### 🕒 現在の日本時間：**{japan_time.strftime('%Y年%m月%d日 %H:%M:%S')}**")

# 入力
with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        place = st.selectbox("競艇場", ["住之江", "大村", "丸亀", "平和島", "唐津"])
        race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
    with col2:
        odds = st.number_input("オッズ（1.5以上）", min_value=1.5, value=1.5, step=0.01)
        bet = st.number_input("賭け金（円）", min_value=100, step=100, value=100)
    result = st.radio("的中／不的中", ["的中", "不的中"])
    submitted = st.form_submit_button("記録")

# 処理
if submitted:
    payout = int(bet * odds) if result == "的中" else 0
    profit = payout - bet
    df = st.session_state.df
    new_balance = st.session_state.balance + profit
    df.loc[len(df)] = [place, race, bet, odds, result, profit, new_balance]
    st.session_state.balance = new_balance
    st.session_state.df = df

    if result == "的中":
        st.session_state.ecp["loss_count"] = 0
        st.session_state.ecp["win_count"] += 1
    else:
        st.session_state.ecp["loss_count"] += 1

    st.success("✅ 記録を保存しました。")

# 統計
df = st.session_state.df
hit_count = df[df["結果"] == "的中"].shape[0]
total = df.shape[0]
hit_rate = hit_count / total if total else 0
win_rate = hit_rate
recovery_rate = df["収支"].sum() / df["賭け金"].sum() if df["賭け金"].sum() else 0

st.markdown("## 📊統計情報")
st.markdown(f"""
- 💼 現在の残高：{st.session_state.balance}円  
- 🎯 目標金額：{st.session_state.goal}円  
- 📉 累積損益：{df['収支'].sum()}円  
- 🎯 の中間率：{round(hit_rate * 100, 1)}%  
- 🏆 勝率：{round(win_rate * 100, 1)}%  
- 💸 回収率：{round(recovery_rate * 100, 1)}%  
- 🧠 次回推奨ベット額（ECP方式）：{get_next_bet_amount(st.session_state.ecp["loss_count"])}円
""")

# AI予想（仮→本物モデルに差し替え可能）
st.markdown("## 🧠AI予想（的中率 × 勝率重視）")
mock_ai = [
    {"競艇場": "住之江", "レース": "9R", "スコア": 0.86},
    {"競艇場": "住之江", "レース": "11R", "スコア": 0.77},
    {"競艇場": "住之江", "レース": "1R", "スコア": 0.7},
    {"競艇場": "大村", "レース": "5R", "スコア": 0.68},
    {"競艇場": "丸亀", "レース": "7R", "スコア": 0.66},
]
for i in mock_ai:
    st.markdown(f"🎯 {i['競艇場']} {i['レース']} 🧠 スコア：{i['スコア']}")

# 決算表
st.markdown("## 📋決算表")
st.dataframe(df)

# リセット
if st.button("1からスタート"):
    st.session_state.df = pd.DataFrame(columns=df.columns)
    st.session_state.balance = 10000
    st.session_state.ecp = reset_ecp()
    st.success("🔁 初期化しました")
