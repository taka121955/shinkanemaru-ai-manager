# pages/page3_statistics.py

import streamlit as st
st.set_page_config(page_title="③ 統計データ", layout="centered")  # ✅ 最上段に固定！

import pandas as pd

def show_page():
    st.title("📊 統計データの表示")

    try:
        df = pd.read_csv("results.csv")

        if df.empty:
            st.warning("⚠️ データがまだ登録されていません。")
            return

        total_bets = len(df)
        total_hits = (df["的中"] == "的中").sum()
        hit_rate = round(total_hits / total_bets * 100, 1) if total_bets else 0

        total_amount = df["金額"].sum()
        avg_amount = round(total_amount / total_bets, 1) if total_bets else 0

        st.metric("ベット回数", f"{total_bets} 回")
        st.metric("的中回数", f"{total_hits} 回")
        st.metric("的中率", f"{hit_rate} %")
        st.metric("合計ベット額", f"{total_amount} 円")
        st.metric("平均ベット額", f"{avg_amount} 円")

        st.markdown("### 🔎 レース別統計")
        st.dataframe(df.groupby("競艇場")["的中"].value_counts().unstack().fillna(0))

    except FileNotFoundError:
        st.warning("❌ 'results.csv' が存在しません。データを登録してください。")
