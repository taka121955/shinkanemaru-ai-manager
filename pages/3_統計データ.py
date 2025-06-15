# pages/page3_statistics.py

import streamlit as st
import pandas as pd

st.markdown("## 📊 統計データ")

csv_path = "results.csv"

# データ読み込み
try:
    df = pd.read_csv(csv_path)
    total_games = len(df)
    wins = df["的中"].sum()
    total_bet = df["賭け金"].sum()
    total_return = (df["的中"] * df["オッズ"] * df["賭け金"]).sum()

    # 勝率・回収率・的中率
    win_rate = wins / total_games * 100 if total_games > 0 else 0
    hit_rate = wins / total_games * 100 if total_games > 0 else 0
    recovery_rate = total_return / total_bet * 100 if total_bet > 0 else 0

    st.metric("🏆 勝率", f"{win_rate:.1f}%")
    st.metric("💸 回収率", f"{recovery_rate:.1f}%")
    st.metric("🎯 的中率", f"{hit_rate:.1f}%")

except Exception as e:
    st.warning("データが読み込めませんでした。まだ記録が存在しない可能性があります。")
    st.text(str(e))
