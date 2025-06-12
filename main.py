import streamlit as st
from datetime import datetime
import pandas as pd
from utils.ecp import get_next_bet_amount, reset_ecp

st.set_page_config(page_title="賭神様", layout="centered")

# 初期化
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 20000
if "ecp" not in st.session_state:
    st.session_state.ecp = reset_ecp()
if "history" not in st.session_state:
    st.session_state.history = []

# 📌 ヘッダー
st.title("🧠AI予想 × 💰新金丸法 × 📊資金マネージャー")

# 📊 統計情報
df = pd.DataFrame(st.session_state.history)

hit_rate = (
    df[df["結果"] == "的中"].shape[0] / df[df["結果"] != "未入力"].shape[0]
    if not df.empty and df[df["結果"] != "未入力"].shape[0] > 0 else 0
)
win_rate = hit_rate
recovery_rate = (
    df["収支"].sum() / (df["賭け金"].sum()) * 100
    if not df.empty and df["賭け金"].sum() > 0 else 0
)

# ⏰ 日本時間表示
now = datetime.now()
japan_time = now.strftime("%Y/%m/%d %H:%M:%S")

st.markdown(f"""
⏰ **現在時刻（日本時間）**：{japan_time}  
💼 **現在の残高**：{st.session_state.balance}円  
🎯 **目標金額**：{st.session_state.goal}円  
📉 **累積損益**：{df["収支"].sum() if not df.empty else 0}円  
🎯 **的中率**：{round(hit_rate * 100, 1)}%  
🏆 **勝率**：{round(win_rate * 100, 1)}%  
💸 **回収率**：{round(recovery_rate, 1)}%  
🧠 **次回推奨ベット額（ECP方式）**：{get_next_bet_amount(st.session_state.ecp["loss_count"])}円
""")

# 🎯 ベット入力
st.subheader("🎯 ベット記録入力")

col1, col2 = st.columns(2)
with col1:
    race_place = st.selectbox("競艇場", ["住之江", "戸田", "蒲郡", "丸亀", "児島", "大村", "平和島", "桐生", "常滑", "芦屋", "若松", "下関", "びわこ", "唐津", "尼崎", "福岡", "津", "徳山", "多摩川", "江戸川", "鳴門"])
with col2:
    race_number = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])

col3, col4 = st.columns(2)
with col3:
    odds = st.number_input("オッズ（1.5以上）", min_value=1.5, value=1.5, step=0.1)
with col4:
    result = st.radio("レース結果", ["的中", "不的中"])

# 💰 賭け金（自動計算）
bet_amount = get_next_bet_amount(st.session_state.ecp["loss_count"])

# 🔘 記録ボタン
if st.button("✅ 結果を記録"):
    if result == "的中":
        profit = int(bet_amount * (odds - 1))
        st.session_state.balance += profit
        st.session_state.ecp["loss_count"] = 0
        outcome = "的中"
    else:
        st.session_state.balance -= bet_amount
        st.session_state.ecp["loss_count"] += 1
        profit = -bet_amount
        outcome = "不的中"

    st.session_state.history.append({
        "競艇場": race_place,
        "レース": race_number,
        "賭け金": bet_amount,
        "オッズ": odds,
        "結果": outcome,
        "収支": profit,
        "累積収支": st.session_state.balance
    })
    st.success("記録が追加されました。")

# 📈 AI予想（ダミー処理 → 後ほどAI連携可）
st.subheader("🧠AI予想（的中率 × 勝率重視）")

# ダミー予想（固定TOP5スコア）
ai_predictions = [
    {"競艇場": "住之江", "レース": "9R", "スコア": 0.86},
    {"競艇場": "住之江", "レース": "11R", "スコア": 0.77},
    {"競艇場": "住之江", "レース": "1R", "スコア": 0.70},
    {"競艇場": "大村", "レース": "5R", "スコア": 0.68},
    {"競艇場": "丸亀", "レース": "7R", "スコア": 0.66},
]

for pred in ai_predictions:
    st.markdown(f"🏟️ {pred['競艇場']} 🎯 {pred['レース']} 🧠 スコア：{pred['スコア']}")

# 📋 決算表表示
if not df.empty:
    st.subheader("📋 決算表")
    st.dataframe(df, use_container_width=True)

# 🔁 リセット
if st.button("1からスタート"):
    st.session_state.balance = 10000
    st.session_state.goal = 20000
    st.session_state.ecp = reset_ecp()
    st.session_state.history = []
    st.experimental_rerun()
