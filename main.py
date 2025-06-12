import streamlit as st
import pandas as pd
from utils.ecp import calculate_next_bet
from utils.ai_predictor import get_ai_predictions

st.set_page_config(page_title="新金丸法 × AI予想マネージャー", layout="centered")

# 初期化
if "data" not in st.session_state:
    st.session_state.data = []
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "target" not in st.session_state:
    st.session_state.target = 20000
if "wave" not in st.session_state:
    st.session_state.wave = 0

st.title("💰 新金丸法 × AI予想マネージャー")

# 残高・目標・収支表示
total_profit = sum([row["収支"] for row in st.session_state.data])
wins = sum([1 for row in st.session_state.data if row["結果"] == "的中"])
losses = sum([1 for row in st.session_state.data if row["結果"] == "不的中"])
trades = len(st.session_state.data)
win_rate = (wins / trades * 100) if trades > 0 else 0
hit_rate = win_rate
roi = (total_profit / (sum([row["賭け金"] for row in st.session_state.data]) or 1)) * 100

st.markdown(f"💼現在の残高：{st.session_state.balance}円")
st.markdown(f"🎯目標金額：{st.session_state.target}円")
st.markdown(f"📈累積利益：{total_profit}円")
st.markdown(f"🎯的中率：{hit_rate:.1f}%")
st.markdown(f"🏆勝率：{win_rate:.1f}%")
st.markdown(f"💸回収率：{roi:.1f}%")

# 🧠次回推奨ベット額
next_bet = calculate_next_bet(st.session_state.data, st.session_state.balance)
st.markdown(f"🧠次回推奨ベット額（ECP）：{next_bet}円")

# 📊 AI予想表示
st.subheader("📊 AI予想（的中率 × 勝率 スコア上位3レース）")
predictions = get_ai_predictions()
for pred in predictions:
    st.markdown(f"🏟️：{pred['競艇場']} 🎯：{pred['レース']} 🧠スコア：{pred['score']:.2f}")

st.markdown("---")

# 入力フォーム
st.subheader("🎫 レース結果を記録")
col1, col2 = st.columns(2)
with col1:
    place = st.selectbox("競艇場名", ["住之江", "大村", "尼崎", "蒲郡", "若松", "平和島", "児島", "丸亀", "徳山", "唐津", "芦屋", "福岡"])
with col2:
    race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])

col3, col4 = st.columns(2)
with col3:
    bet = st.number_input("賭け金（円）", min_value=100, step=100)
with col4:
    odds = st.number_input("オッズ", min_value=1.1, step=0.1)

result = st.radio("結果", ("的中", "不的中"))

if st.button("記録する"):
    profit = int(bet * odds - bet) if result == "的中" else -int(bet)
    st.session_state.data.append({
        "競艇場": place,
        "レース": race,
        "賭け金": bet,
        "オッズ": odds,
        "結果": result,
        "収支": profit,
        "累積収支": st.session_state.balance + profit
    })
    st.session_state.balance += profit

    # 1からやり直し条件
    if st.session_state.balance <= 0 or st.session_state.balance >= st.session_state.target:
        st.success("🎉 条件達成！アプリをリセットします。")
        st.session_state.data = []
        st.session_state.balance = 10000
        st.experimental_rerun()

# 表示
st.subheader("📋 決算記録")
df = pd.DataFrame(st.session_state.data)
st.dataframe(df, use_container_width=True)

if st.button("🔄 1からスタート（記録削除）"):
    st.session_state.data = []
    st.session_state.balance = 10000
    st.experimental_rerun()
