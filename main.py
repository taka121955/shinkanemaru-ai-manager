import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

# タイトル時間表示
jst = pytz.timezone("Asia/Tokyo")
now = datetime.now(jst).strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"🕓 **現在の日本時間**\n\n### {now}")

# ===== AI予想表示（仮） =====
st.markdown("🧠 **AI予想（的中率 × 勝率重視）**")
ai_predictions = [
    {"場": "桐生", "レース": "8", "式別": "3連複", "買い目": "1-2-4", "オッズ": 7.5},
    {"場": "住之江", "レース": "1", "式別": "単勝", "買い目": "3", "オッズ": 2.1},
    {"場": "福岡", "レース": "10", "式別": "2連単", "買い目": "1-2", "オッズ": 3.9},
]
for pred in ai_predictions:
    st.markdown(
        f"📍{pred['場']} 第{pred['レース']}R ｜ {pred['式別']}：{pred['買い目']} ｜ オッズ：{pred['オッズ']}"
    )

# ===== 統計情報 =====
st.markdown("📊 **統計情報**")
if "history" not in st.session_state:
    st.session_state.history = []

df = pd.DataFrame(st.session_state.history)

balance = 10000
target = 20000
total_profit = sum([int(d["収支"]) for d in st.session_state.history]) if st.session_state.history else 0
hit_count = len([d for d in st.session_state.history if d["的中／不的中"] == "的中"])
hit_rate = round(hit_count / len(st.session_state.history) * 100, 1) if st.session_state.history else 0.0
win_rate = hit_rate  # 同じ扱い
recovery_rate = round((total_profit / sum([int(d["賭金"]) for d in st.session_state.history])) * 100, 1) if sum([int(d["賭金"]) for d in st.session_state.history]) else 0.0
loss_count = len([d for d in st.session_state.history if d["的中／不的中"] == "不的中"])
next_bet = [100, 300, 900, 100][min(loss_count, 3)]

st.markdown(f"""
- 💼 現在の残高：{balance}円  
- 🎯 目標金額：{target}円  
- 📉 累積損益：{total_profit}円  
- 🎯 的中率：{hit_rate}%  
- 🏆 勝率：{win_rate}%  
- 💸 回収率：{recovery_rate}%  
- 🧠 次回推奨賭金（ECP方式）：{next_bet}円
""")

# ===== 勝敗入力 =====
st.markdown("🎮 **勝敗入力**")
with st.form("record_form"):
    date = st.date_input("日付", value=datetime.now(jst).date())
    stadium = st.selectbox("競艇場", ["住之江", "平和島", "若松", "大村", "桐生", "福岡"])
    race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
    odds = st.number_input("オッズ（1.5以上）", min_value=1.5, step=0.1)
    bet = st.number_input("賭金", min_value=100, step=100)
    result = st.radio("結果", ["的中", "不的中"])
    submitted = st.form_submit_button("記録")

    if submitted:
        profit = int(bet * odds) - bet if result == "的中" else -int(bet)
        st.session_state.history.append({
            "日付": str(date),
            "競艇場": stadium,
            "レース": race,
            "オッズ": odds,
            "賭金": int(bet),
            "的中／不的中": result,
            "収支": profit
        })
        st.success("✅ 記録しました！")

# ===== 勝敗履歴 =====
st.markdown("📖 **勝敗履歴**")
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df)

# ===== フッター =====
st.markdown("制作者：小島崇彦")
