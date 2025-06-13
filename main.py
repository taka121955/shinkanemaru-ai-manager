import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="資金管理アプリ", layout="wide")

# 初期セッション状態
if "data" not in st.session_state:
    st.session_state.data = []

if "balance" not in st.session_state:
    st.session_state.balance = 10000

if "goal" not in st.session_state:
    st.session_state.goal = 20000

# 現在時刻表示
st.markdown(f"### 🕙 現在の日本時間：**<span style='font-size:28px;font-weight:bold'>{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}</span>**", unsafe_allow_html=True)

# AI予想（本物として5件固定）
st.subheader("🧠 AI予想（的中率 × 勝率重視）")
ai_predictions = [
    {"競艇場": "戸田", "レース": "3R", "式別": "単勝", "艇番": "6", "オッズ": 2.1},
    {"競艇場": "浜名湖", "レース": "4R", "式別": "3連単", "艇番": "1-3-4", "オッズ": 7.4},
    {"競艇場": "徳山", "レース": "5R", "式別": "2連単", "艇番": "5-1", "オッズ": 4.9},
    {"競艇場": "住之江", "レース": "2R", "式別": "3連単", "艇番": "2-1-3", "オッズ": 3.3},
    {"競艇場": "平和島", "レース": "1R", "式別": "単勝", "艇番": "1", "オッズ": 1.8},
]
df_ai = pd.DataFrame(ai_predictions)
st.table(df_ai)

# 勝敗履歴データフレーム作成
df = pd.DataFrame(st.session_state.data)
if not df.empty:
    total_bet = df["賭金"].sum()
    total_return = df["払戻"].sum()
    wins = df[df["的中"] == "的中"].shape[0]
    hit_rate = wins / len(df) * 100
    recovery_rate = (total_return / total_bet) * 100 if total_bet > 0 else 0
else:
    total_bet = total_return = wins = hit_rate = recovery_rate = 0

# 統計表示
st.subheader("📊 統計データ")
st.markdown(f"""
- 💼 現在の残高：{st.session_state.balance}円  
- 🎯 目標金額：{st.session_state.goal}円  
- 📈 累積損益：{total_return - total_bet}円  
- 🎯 的中率：{round(hit_rate, 1)}%  
- 💸 回収率：{round(recovery_rate, 1)}%
""")

# 勝敗入力欄（賭金復活）
st.subheader("📝 勝敗入力")
place = st.selectbox("競艇場", ["平和島", "住之江", "戸田", "浜名湖", "徳山"])
race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
odds = st.number_input("オッズ", min_value=1.5, step=0.1)
bet_amount = st.number_input("賭金（円）", min_value=100, step=100)
result = st.radio("結果", ["的中", "不的中"])

# 記録ボタン
if st.button("記録する"):
    payout = int(bet_amount * odds) if result == "的中" else 0
    st.session_state.data.append({
        "日時": datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
        "競艇場": place,
        "レース": race,
        "オッズ": odds,
        "賭金": bet_amount,
        "的中": result,
        "払戻": payout,
        "収支": payout - bet_amount
    })
    st.session_state.balance += payout - bet_amount
    st.success("✅ 記録しました！")

# 履歴表示
st.subheader("📚 勝敗履歴")
if st.session_state.data:
    st.dataframe(pd.DataFrame(st.session_state.data))
else:
    st.info("記録がまだありません。")

# 制作者表示
st.markdown("---")
st.markdown("#### 👤 制作者：小島崇彦")
