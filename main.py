import streamlit as st
import pandas as pd
from datetime import datetime
from utils.ecp import get_next_bet_amount

st.set_page_config(layout="wide")
st.title("📊AI予想 × 新金丸法 × 資金マネージャー")

# ①日本時間表示
jst_time = datetime.utcnow().astimezone().strftime("%Y-%m-%d %H:%M:%S（日本時間）")
st.markdown(f"<h3 style='font-size:24px; font-weight:bold;'>🕒 {jst_time}</h3>", unsafe_allow_html=True)

# ②AI予想（仮データ）
st.markdown("## 🧠AI予想（的中率 × 勝率重視）")
ai_predictions = [
    {"競艇場": "住之江", "レース": "9R", "スコア": 0.86},
    {"競艇場": "住之江", "レース": "11R", "スコア": 0.77},
    {"競艇場": "住之江", "レース": "1R", "スコア": 0.7},
    {"競艇場": "大村", "レース": "5R", "スコア": 0.68},
    {"競艇場": "丸亀", "レース": "7R", "スコア": 0.66},
]
for pred in ai_predictions:
    st.write(f"🏟️ {pred['競艇場']} 🎯{pred['レース']} 🧠スコア：{pred['スコア']}")

# セッション初期化
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["日付", "競艇場", "レース", "オッズ", "賭金", "的中", "収支"])
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 20000
if "ecp" not in st.session_state:
    st.session_state.ecp = {"loss_count": 0}

df = st.session_state.data

# ③統計情報
st.markdown("## 📈統計情報")

if not df.empty:
    hit_count = len(df[df["的中"] == "的中"])
    win_count = hit_count
    hit_rate = hit_count / len(df)
    win_rate = win_count / len(df)
    recovery_rate = df["収支"].sum() / df["賭金"].sum() if df["賭金"].sum() else 0
else:
    hit_rate = win_rate = recovery_rate = 0.0

if not df.empty and "収支" in df.columns and df["収支"].sum() >= 0:
    next_bet = 100
else:
    next_bet = get_next_bet_amount(st.session_state.ecp["loss_count"])

st.markdown(f"""
- 💼 現在の残高：{st.session_state.balance}円  
- 🎯 目標金額：{st.session_state.goal}円  
- 📉 累積損益：{df['収支'].sum() if not df.empty else 0}円  
- 🎯 的中率：{round(hit_rate * 100, 1)}%  
- 🏆 勝率：{round(win_rate * 100, 1)}%  
- 💸 回収率：{round(recovery_rate * 100, 1)}%  
- 🧠 次回推奨ベット額（ECP方式）：{next_bet}円
""")

# ④勝敗入力
st.markdown("## ✏️勝敗入力")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    place = st.selectbox("競艇場", ["住之江", "大村", "丸亀", "若松", "芦屋", "浜名湖", "児島"])
with col2:
    race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
with col3:
    odds = st.number_input("オッズ（1.5以上）", min_value=1.5, step=0.1)
with col4:
    amount = st.number_input("賭金", min_value=0, step=100)
with col5:
    result = st.radio("的中／不的中", ["的中", "不的中"])

if st.button("記録"):
    profit = round(amount * (odds - 1)) if result == "的中" else -amount
    new_row = pd.DataFrame([{
        "日付": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "競艇場": place,
        "レース": race,
        "オッズ": odds,
        "賭金": amount,
        "的中": result,
        "収支": profit
    }])
    st.session_state.data = pd.concat([st.session_state.data, new_row], ignore_index=True)
    st.session_state.balance += profit
    if result == "的中":
        st.session_state.ecp["loss_count"] = 0
    else:
        st.session_state.ecp["loss_count"] += 1
    st.success("✅記録を保存しました。")

# ⑤勝敗履歴
st.markdown("## 📊勝敗履歴")
st.dataframe(st.session_state.data, use_container_width=True)

# 制作者情報
st.markdown("---")
st.markdown("👤 制作者：小島崇彦")
