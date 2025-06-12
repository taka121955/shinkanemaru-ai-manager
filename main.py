import streamlit as st
import pandas as pd
import datetime
from utils.ecp import get_next_bet_amount, update_ecp
from utils.ai_predictor import get_ai_predictions

st.set_page_config(layout="wide")
st.markdown("<h2><b>⏰ 日本時間：{}</b></h2>".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")), unsafe_allow_html=True)

# データ初期化
if "records" not in st.session_state:
    st.session_state.records = []
if "ecp" not in st.session_state:
    st.session_state.ecp = {"loss_count": 0}
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 20000

# 勝敗履歴データ
df = pd.DataFrame(st.session_state.records)

# AI予想エリア
st.subheader("🧠AI予想（的中率 × 勝率重視）")
ai_predictions = get_ai_predictions()
for pred in ai_predictions:
    st.markdown(f"🏟️ {pred['場']} 🎯{pred['レース']}R 🧠 スコア：{pred['score']}")

# 統計情報
st.subheader("📊統計情報")
try:
    hit_count = df[df["結果"] == "的中"].shape[0]
    total_count = df.shape[0]
    hit_rate = hit_count / total_count if total_count else 0
    win_rate = hit_rate
    recovery_rate = df["収支"].sum() / df["賭金"].sum() if not df.empty and df["賭金"].sum() > 0 else 0
except KeyError:
    hit_rate = win_rate = recovery_rate = 0

# 資金がプラスならベット100円固定
if not df.empty and df["収支"].sum() >= 0:
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

# 勝敗入力エリア
st.subheader("✏️勝敗入力")
cols = st.columns(5)
site = cols[0].selectbox("競艇場", ["住之江", "大村", "丸亀", "芦屋", "若松"])
race = cols[1].selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
odds = cols[2].number_input("オッズ（1.5以上）", min_value=1.5, step=0.1, value=1.5)
bet = cols[3].number_input("賭金", min_value=100, step=100, value=next_bet)
result = cols[4].radio("的中／不的中", ["的中", "不的中"])

if st.button("記録"):
    payout = int(bet * odds) if result == "的中" else -bet
    st.session_state.records.append({
        "日付": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "競艇場": site,
        "レース": race,
        "オッズ": odds,
        "賭金": bet,
        "結果": result,
        "収支": payout
    })
    st.session_state.balance += payout
    update_ecp(result)
    st.success("✅記録を保存しました。")

# 勝敗履歴
st.subheader("📊勝敗履歴")
if not df.empty:
    st.dataframe(df)

# フッター
st.markdown("---")
st.markdown("👨‍💻 制作者：小島崇彦")
