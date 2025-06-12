import streamlit as st
import pandas as pd
import random

from utils.ecp import get_next_bet_amount

st.set_page_config(page_title="新金丸法 × AI予想マネージャー", layout="centered")

if "records" not in st.session_state:
    st.session_state.records = []
if "initial_capital" not in st.session_state:
    st.session_state.initial_capital = 10000
if "goal_capital" not in st.session_state:
    st.session_state.goal_capital = 20000

st.title("🎰 新金丸法 × AI予想マネージャー")
st.markdown("---")

total_profit = sum([r["収支"] for r in st.session_state.records])
current_balance = st.session_state.initial_capital + total_profit
st.markdown(f"💼現在の残高：{current_balance}円")
st.markdown(f"🎯目標金額：{st.session_state.goal_capital}円")
st.markdown(f"📉累積{'損益' if total_profit < 0 else '利益'}：{total_profit}円")

wins = sum(1 for r in st.session_state.records if r["結果"] == "的中")
total_bets = len(st.session_state.records)
hit_rate = (wins / total_bets * 100) if total_bets else 0
roi = (total_profit / sum(r["賭け金"] for r in st.session_state.records) * 100) if total_bets else 0

st.markdown(f"🎯的中率：{hit_rate:.1f}%")
st.markdown(f"🏆勝率：{hit_rate:.1f}%")
st.markdown(f"💸回収率：{roi:.1f}%")

next_bet = get_next_bet_amount(st.session_state.records)
st.markdown(f"🧠次回推奨ベット額（ECP）： {next_bet}円")

if st.button("1からスタート"):
    st.session_state.records = []
    st.experimental_rerun()

st.markdown("---")

def mock_ai_predictions():
    venues = ["住之江", "大村", "浜名湖", "児島", "鳴門"]
    races = [f"{i}R" for i in range(1, 13)]
    predictions = []
    for _ in range(3):
        predictions.append({
            "競艇場": random.choice(venues),
            "レース": random.choice(races),
            "スコア": round(random.uniform(0.7, 0.95), 2)
        })
    predictions.sort(key=lambda x: x["スコア"], reverse=True)
    return predictions

ai_predictions = mock_ai_predictions()
top = ai_predictions[0]

st.markdown("## 📊AI予想（的中率 × 勝率 スコア上位3レース）")
for pred in ai_predictions:
    st.markdown(f"🛶：{pred['競艇場']} 🎯：{pred['レース']} 🧠スコア：{pred['スコア']}")

st.markdown("### 📌 AI推奨レース（的中率×勝率 最上位）")
st.markdown(f"🛶：{top['競艇場']} 🎯：{top['レース']} 🧠スコア：{top['スコア']}")

st.markdown("## 🎯ベット記録入力")
col1, col2 = st.columns(2)
venue = col1.selectbox("競艇場名", ["住之江", "大村", "浜名湖", "児島", "鳴門"])
race = col2.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
bet_amount = st.number_input("賭け金（円）", min_value=100, step=100, value=next_bet)
odds = st.number_input("オッズ", min_value=1.0, step=0.1)
result = st.radio("結果", ["的中", "不的中"])

if st.button("記録する"):
    profit = int(bet_amount * (odds - 1)) if result == "的中" else -bet_amount
    st.session_state.records.append({
        "競艇場": venue,
        "レース": race,
        "賭け金": bet_amount,
        "オッズ": odds,
        "結果": result,
        "収支": profit
    })
    st.experimental_rerun()

st.markdown("## 📋決算表")
if st.session_state.records:
    df = pd.DataFrame(st.session_state.records)
    df["累積収支"] = df["収支"].cumsum() + st.session_state.initial_capital
    st.dataframe(df, use_container_width=True)
else:
    st.info("まだベット記録がありません。")
