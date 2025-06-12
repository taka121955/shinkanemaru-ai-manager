import streamlit as st
import pandas as pd
from utils.ecp import get_next_bet_amount, reset_ecp

st.title("🎯 AI予想 × 新金丸法 × 資金マネージャー")

# セッション初期化
if "bets" not in st.session_state:
    st.session_state.bets = []
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "target" not in st.session_state:
    st.session_state.target = 20000

# AI予想（仮ロジックでランダム5件）
st.subheader("📊 AI予想（的中率×勝率スコア 上位5レース）")
ai_predictions = [
    {"競艇場": "住之江", "レース": "9R", "式別": "3連単", "賭け先": "1-2-3", "スコア": 0.86},
    {"競艇場": "住之江", "レース": "11R", "式別": "2連単", "賭け先": "1-3", "スコア": 0.77},
    {"競艇場": "住之江", "レース": "1R", "式別": "単勝", "賭け先": "1", "スコア": 0.70},
    {"競艇場": "大村", "レース": "5R", "式別": "3連単", "賭け先": "2-1-4", "スコア": 0.65},
    {"競艇場": "丸亀", "レース": "10R", "式別": "2連単", "賭け先": "4-6", "スコア": 0.61},
]
st.dataframe(pd.DataFrame(ai_predictions))

# 入力フォーム
st.subheader("🎯 ベット記録入力")
with st.form("bet_form"):
    col1, col2 = st.columns(2)
    place = col1.selectbox("競艇場", sorted(set(r["競艇場"] for r in ai_predictions)))
    race = col2.selectbox("レース番号", sorted(set(r["レース"] for r in ai_predictions if r["競艇場"] == place)))
    odds = st.number_input("オッズ（1.0以上）", min_value=1.0, step=0.1)
    result = st.selectbox("結果", ["的中", "不的中"])
    submitted = st.form_submit_button("記録")

if submitted:
    bet = get_next_bet_amount(len(st.session_state.bets))
    profit = round(bet * odds - bet) if result == "的中" else -bet
    st.session_state.balance += profit
    st.session_state.bets.append({
        "競艇場": place,
        "レース": race,
        "賭け金": bet,
        "オッズ": odds,
        "結果": result,
        "収支": profit,
        "累積収支": st.session_state.balance
    })
    st.success("✅ 記録が追加されました。")

# 統計計算
wins = sum(1 for b in st.session_state.bets if b["結果"] == "的中")
total = len(st.session_state.bets)
profit_total = sum(b["収支"] for b in st.session_state.bets)
hit_rate = wins / total * 100 if total else 0
recovery = sum(b["オッズ"] * b["賭け金"] if b["結果"] == "的中" else 0 for b in st.session_state.bets)
total_bet = sum(b["賭け金"] for b in st.session_state.bets)
recovery_rate = recovery / total_bet * 100 if total_bet else 0

# 統計表示
st.subheader("📈 統計情報")
st.markdown(f"""
- 💼 現在の残高：{st.session_state.balance}円  
- 🎯 目標金額：{st.session_state.target}円  
- 📈 累積利益：{profit_total}円  
- 🎯 的中率：{hit_rate:.1f}%  
- 🏆 勝率：{hit_rate:.1f}%  
- 💸 回収率：{recovery_rate:.1f}%  
- 🧠 次回推奨ベット額（ECP方式）：{get_next_bet_amount(len(st.session_state.bets))}円
""")

# 決算表
st.subheader("📄 決算表")
df = pd.DataFrame(st.session_state.bets)
st.dataframe(df)

# リセットボタン
if st.button("1からスタート"):
    st.session_state.bets = []
    st.session_state.balance = 10000
