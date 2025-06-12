import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
from utils.ecp import get_next_bet_amount

# 初期化
if "data" not in st.session_state:
    st.session_state.data = []
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 20000
if "ecp" not in st.session_state:
    st.session_state.ecp = {"loss_count": 0}

# ✅ 日本時間表示（大きく太字）
jst = pytz.timezone('Asia/Tokyo')
now_japan = datetime.now(jst).strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f"<h2>🕒 日本時間：<b>{now_japan}</b></h2>", unsafe_allow_html=True)

# ①AI予想（仮で静的表示：後で本物のロジックに変更可能）
st.subheader("🧠 AI予想（的中率 × 勝率重視）")
ai_predictions = [
    {"競艇場": "住之江", "レース": "9R", "スコア": 0.86},
    {"競艇場": "住之江", "レース": "11R", "スコア": 0.77},
    {"競艇場": "住之江", "レース": "1R", "スコア": 0.70},
    {"競艇場": "大村", "レース": "5R", "スコア": 0.68},
    {"競艇場": "丸亀", "レース": "7R", "スコア": 0.66},
]
for pred in ai_predictions:
    st.write(f"🏟️ {pred['競艇場']} 🎯 {pred['レース']} 🧠 スコア：{pred['スコア']}")

# ②統計情報
df = pd.DataFrame(st.session_state.data)
hit_count = len(df[df["結果"] == "的中"]) if not df.empty and "結果" in df.columns else 0
win_count = len(df[df["収支"] > 0]) if not df.empty else 0
total = len(df) if not df.empty else 0
hit_rate = hit_count / total if total > 0 else 0
win_rate = win_count / total if total > 0 else 0
recovery_rate = df["収支"].sum() / (df["賭金"].sum()) if not df.empty and df["賭金"].sum() > 0 else 0

next_bet = 100 if df["収支"].sum() >= 0 else get_next_bet_amount(st.session_state.ecp["loss_count"])

st.markdown(f"""
## 📊 統計情報
- 💼 現在の残高：{st.session_state.balance}円  
- 🎯 目標金額：{st.session_state.goal}円  
- 📉 累積損益：{df['収支'].sum() if not df.empty else 0}円  
- 🎯 的中率：{round(hit_rate * 100, 1)}%  
- 🏆 勝率：{round(win_rate * 100, 1)}%  
- 💸 回収率：{round(recovery_rate * 100, 1)}%
- 🧠 次回推奨ベット額（ECP方式）：{next_bet}円
""")

# ③勝敗入力
st.subheader("📋 勝敗入力")

race_place = st.selectbox("競艇場", ["若松", "丸亀", "住之江", "大村"])
race_number = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
odds = st.number_input("オッズ（1.5以上）", min_value=1.5, value=1.5, step=0.1)
bet_amount = st.number_input("賭金", min_value=100, value=next_bet, step=100)
result = st.radio("的中 / 不的中", ["的中", "不的中"])

# ④記録
if st.button("記録"):
    payout = int(bet_amount * odds) if result == "的中" else 0
    profit = payout - bet_amount
    st.session_state.balance += profit
    if result == "的中":
        st.session_state.ecp["loss_count"] = 0
    else:
        st.session_state.ecp["loss_count"] += 1
    st.session_state.data.append({
        "日付": now_japan,
        "競艇場": race_place,
        "レース": race_number,
        "オッズ": odds,
        "賭金": bet_amount,
        "的中": result,
        "収支": profit
    })
    st.success("✅ 記録を保存しました。")

# ⑤履歴表示
st.subheader("📊 勝敗履歴")
if st.session_state.data:
    hist_df = pd.DataFrame(st.session_state.data)
    st.dataframe(hist_df)
else:
    st.info("まだ記録がありません。")

# ⑥制作者クレジット
st.markdown("---")
st.markdown("👨‍💻 制作者：小島崇彦")
