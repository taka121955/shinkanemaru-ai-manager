# pages/page8_summary_today.py

import streamlit as st
import pandas as pd
from datetime import datetime

st.title("📊 今日の結果まとめ")

# 読み込み（results.csv を使っている前提）
try:
    df = pd.read_csv("results.csv")
    today = datetime.now().strftime("%Y-%m-%d")
    df_today = df[df["日付"] == today]

    if df_today.empty:
        st.warning("本日の記録がまだありません。")
    else:
        total = len(df_today)
        wins = len(df_today[df_today["的中"] == "○"])
        losses = total - wins

        投資額 = df_today["金額"].sum()
        回収額 = df_today["回収"].sum()
        的中率 = (wins / total) * 100 if total > 0 else 0
        回収率 = (回収額 / 投資額) * 100 if 投資額 > 0 else 0
        収支 = 回収額 - 投資額

        col1, col2, col3 = st.columns(3)
        col1.metric("✅ 勝ち数", f"{wins} 勝")
        col2.metric("❌ 負け数", f"{losses} 敗")
        col3.metric("🎯 的中率", f"{的中率:.1f}%")

        col4, col5, col6 = st.columns(3)
        col4.metric("💰 投資額", f"{int(投資額):,} 円")
        col5.metric("💵 回収額", f"{int(回収額):,} 円")
        col6.metric("📈 回収率", f"{回収率:.1f}%")

        st.subheader("🏁 的中レース一覧")
        st.dataframe(df_today[df_today["的中"] == "○"], use_container_width=True)

except FileNotFoundError:
    st.error("results.csv が見つかりません。先にベット結果を記録してください。")
