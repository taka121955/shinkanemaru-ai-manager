import streamlit as st
import pandas as pd

# 仮データ（後にCSV or DBに切り替え可）
data = [
    {"日付": "2025/06/13", "競艇場": "住之江", "レース": "1R", "賭金": 1000, "オッズ": 2.5, "的中": "的中"},
    {"日付": "2025/06/13", "競艇場": "住之江", "レース": "2R", "賭金": 1000, "オッズ": 1.8, "的中": "不的中"},
    {"日付": "2025/06/14", "競艇場": "戸田", "レース": "1R", "賭金": 500, "オッズ": 3.0, "的中": "的中"},
    {"日付": "2025/06/14", "競艇場": "戸田", "レース": "2R", "賭金": 1000, "オッズ": 2.0, "的中": "不的中"},
]

df = pd.DataFrame(data)

# 統計計算
total_bets = len(df)
total_money = df["賭金"].sum()
total_hits = df[df["的中"] == "的中"].shape[0]
hit_rate = total_hits / total_bets * 100 if total_bets else 0
recovery = (df[df["的中"] == "的中"]["オッズ"] * df[df["的中"] == "的中"]["賭金"]).sum()
recovery_rate = recovery / total_money * 100 if total_money else 0
win_rate = total_hits / total_bets * 100 if total_bets else 0

# 表示
st.markdown("### 📊 統計データ")
st.metric("総レース数", f"{total_bets} 回")
st.metric("総賭金", f"{total_money} 円")
st.metric("的中数", f"{total_hits} 回")
st.metric("的中率", f"{hit_rate:.1f} %")
st.metric("回収率", f"{recovery_rate:.1f} %")
st.metric("勝率", f"{win_rate:.1f} %")

# 記録表示
st.markdown("---")
st.markdown("### 📋 過去の記録")
st.dataframe(df)
