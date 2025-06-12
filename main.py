import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
from utils.ecp import get_next_bet_amount
from utils.ai_predictor import get_ai_predictions

# 日本時間の表示
jst = pytz.timezone('Asia/Tokyo')
now_japan = datetime.now(jst)
st.markdown("## 🕒現在の日本時間")
st.markdown(f"### **{now_japan.strftime('%Y/%m/%d %H:%M:%S')}**")

# AI予想（本番表示：上位5件）
st.markdown("## 🧠AI予想（的中率 × 勝率重視）")
predictions = get_ai_predictions()
for pred in predictions[:5]:
    st.markdown(f"🏁 {pred['場']} 🎯{pred['レース']}R {pred['式別']}【{pred['艇番']}】🧠 スコア：{pred['score']}")

# 統計情報
st.markdown("## 📊統計情報")

df = st.session_state.get("history", pd.DataFrame())

if not df.empty:
    total_bet = df["賭金"].sum()
    total_return = df["収支"].sum()
    hit_count = (df["的中／不的中"] == "的中").sum()
    total_count = len(df)
    hit_rate = hit_count / total_count * 100 if total_count else 0
    recovery_rate = total_return / total_bet * 100 if total_bet else 0
else:
    total_return = 0
    hit_rate = 0
    recovery_rate = 0

# 次回ベット額
next_bet = 100 if total_return >= 0 else get_next_bet_amount(st.session_state.get("ecp", {}).get("loss_count", 0))

st.markdown(f"""
- 💼 現在の残高：{st.session_state.get('balance', 10000)}円  
- 🎯 的中率：{hit_rate:.1f}%  
- 💸 回収率：{recovery_rate:.1f}%  
- 🧠 次回推奨ベット額（ECP方式）：{next_bet}円
""")

# 勝敗入力
st.markdown("## ✏️勝敗入力")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    place = st.selectbox("競艇場", ["住之江", "若松", "丸亀", "芦屋", "大村"])
with col2:
    race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
with col3:
    odds = st.number_input("オッズ（1.5以上）", min_value=1.5, value=1.5, step=0.1)
with col4:
    bet_amount = st.number_input("賭金", min_value=100, step=100, value=next_bet)
with col5:
    result = st.radio("的中／不的中", ["的中", "不的中"])

if st.button("記録"):
    profit = round(bet_amount * (odds - 1)) if result == "的中" else -bet_amount
    new_record = pd.DataFrame([{
        "日付": now_japan.strftime("%Y-%m-%d %H:%M:%S"),
        "競艇場": place,
        "レース": race,
        "オッズ": odds,
        "賭金": bet_amount,
        "的中／不的中": result,
        "収支": profit
    }])
    df = pd.concat([df, new_record], ignore_index=True)
    st.session_state["history"] = df
    st.session_state["balance"] = st.session_state.get("balance", 10000) + profit
    st.success("✅ 記録を保存しました。")

# 勝敗履歴
st.markdown("## 📊勝敗履歴")
st.dataframe(df)

# 制作者名
st.markdown("---")
st.markdown("#### 制作者：小島崇彦")
