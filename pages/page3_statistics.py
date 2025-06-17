# pages/page3_statistics.py

import streamlit as st
st.set_page_config(page_title="③ 統計データ", layout="centered")  # ✅ 最上部に配置

import pandas as pd

def show_page():
    st.title("📊 統計データ")

    try:
        df = pd.read_csv("results.csv")
    except FileNotFoundError:
        st.warning("⚠️ データがまだありません。勝敗入力をしてください。")
        return

    if df.empty:
        st.warning("⚠️ データがまだありません。")
        return

    st.markdown("### 🔎 集計結果")

    total_bets = len(df)
    hits = len(df[df["的中"] == "的中"])
    total_amount = df["金額"].sum()
    avg_bet = df["金額"].mean()

    hit_rate = round((hits / total_bets) * 100, 2)

    df["回収額"] = df.apply(lambda row: row["金額"] * 3 if row["予想"] == row["結果"] else 0, axis=1)
    total_return = df["回収額"].sum()
    return_rate = round((total_return / total_amount) * 100, 2) if total_amount > 0 else 0

    st.write(f"🎯 的中率：**{hit_rate}%**")
    st.write(f"💹 回収率：**{return_rate}%**")
    st.write(f"📊 総ベット回数：{total_bets} 回")
    st.write(f"💰 総ベット金額：{total_amount} 円")
    st.write(f"📈 平均ベット金額：{avg_bet:.1f} 円")

    st.markdown("---")
    st.markdown("### 📄 最近の10件")
    st.dataframe(df.tail(10), use_container_width=True)
