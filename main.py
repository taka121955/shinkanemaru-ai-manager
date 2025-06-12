from datetime import datetime
import streamlit as st
import pandas as pd
from utils.ecp import get_next_bet_amount

# タイトルと日本時間表示
st.title("🧠AI予想 × 新金丸法 × 資金マネージャー")
japan_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
st.caption(f"⏰ 日本時間（UTCベース）：{japan_time}")

# 初期化
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 20000
if "ecp" not in st.session_state:
    st.session_state.ecp = {"loss_count": 0}
if "bets" not in st.session_state:
    st.session_state.bets = []

# 📌 勝敗記録入力
with st.form("record_form"):
    st.subheader("🎯 勝敗入力")
    col1, col2 = st.columns(2)
    with col1:
        stadium = st.selectbox("競艇場", ["住之江", "大村", "丸亀", "芦屋", "児島"])
        race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
    with col2:
        odds = st.number_input("オッズ（1.5以上）", min_value=1.5, step=0.1)
        result = st.radio("的中／不的中", ["的中", "不的中"])
    submitted = st.form_submit_button("記録")
    if submitted:
        profit = int(100 * odds) - 100 if result == "的中" else -100
        st.session_state.balance += profit
        if result == "的中":
            st.session_state.ecp["loss_count"] = 0
        else:
            st.session_state.ecp["loss_count"] += 1
        st.session_state.bets.append({
            "競艇場": stadium,
            "レース": race,
            "賭け金": 100,
            "オッズ": odds,
            "結果": result,
            "収支": profit,
            "累積収支": st.session_state.balance
        })
        st.success("✅ 記録を保存しました。")

# 📊 決算と統計
df = pd.DataFrame(st.session_state.bets)
hit_rate = (df["結果"] == "的中").mean() if not df.empty else 0.0
win_rate = hit_rate
recovery_rate = ((df["収支"].sum() + len(df) * 100) / (len(df) * 100)) if not df.empty else 0.0

# 統計情報表示
st.markdown(f"""
### 📊 統計情報

- 💼 現在の残高：{st.session_state.balance}円  
- 🎯 目標金額：{st.session_state.goal}円  
- 📈 累積損益：{df['収支'].sum() if not df.empty else 0}円  
- 🎯 的中率：{round(hit_rate * 100, 1)}%  
- 🏆 勝率：{round(win_rate * 100, 1)}%  
- 💸 回収率：{round(recovery_rate * 100, 1)}%  
- 🧠 次回推奨ベット額（ECP方式）：{get_next_bet_amount(st.session_state.ecp['loss_count'])}円
""")

# 決算表
if not df.empty:
    st.subheader("📋 決算表")
    st.dataframe(df)

# 🔮 AI予想（的中率 × 勝率）TOP5（仮のスコア例）
st.subheader("🧠AI予想（的中率×勝率重視）")
predictions = [
    {"競艇場": "住之江", "レース": "9R", "式別": "3連単", "買い目": "1-2-3", "score": 0.86},
    {"競艇場": "住之江", "レース": "11R", "式別": "3連単", "買い目": "1-3-2", "score": 0.77},
    {"競艇場": "住之江", "レース": "1R", "式別": "3連単", "買い目": "1-2-4", "score": 0.70},
    {"競艇場": "大村", "レース": "5R", "式別": "3連単", "買い目": "2-1-5", "score": 0.68},
    {"競艇場": "丸亀", "レース": "7R", "式別": "3連単", "買い目": "3-2-1", "score": 0.66},
]
for p in predictions:
    st.markdown(f"- 🏟️ {p['競艇場']} 🎯 {p['レース']} {p['式別']}：{p['買い目']}（スコア：{p['score']}）")
