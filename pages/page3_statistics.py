# pages/page3_statistics.py

import streamlit as st
import pandas as pd
from datetime import datetime

st.markdown("### 📊 統計データ")
st.write("過去の勝敗結果から統計を算出します。")

# データの読み込み
try:
    df = pd.read_csv("results.csv")
    if df.empty:
        st.warning("まだ結果が記録されていません。")
    else:
        df["的中"] = df["的中"].astype(str)
        total_bets = len(df)
        total_wins = len(df[df["的中"] == "1"])
        total_losses = len(df[df["的中"] == "0"])
        win_rate = (total_wins / total_bets * 100) if total_bets else 0

        investment = df["賭け金"].sum()
        payout = df["払戻金"].sum()
        recovery_rate = (payout / investment * 100) if investment > 0 else 0

        net_profit = payout - investment

        st.metric("🎯 勝率", f"{win_rate:.2f}%")
        st.metric("💰 回収率", f"{recovery_rate:.2f}%")
        st.metric("📈 総投資", f"{investment:.0f}円")
        st.metric("📥 払戻合計", f"{payout:.0f}円")
        st.metric("📊 収支", f"{net_profit:.0f}円")
except FileNotFoundError:
    st.warning("記録ファイルが見つかりません。")
