import streamlit as st
import pandas as pd
import os

RESULTS_FILE = "results.csv"

def show_page():
    st.markdown("## ③ 統計データ 📊")

    # 仮データ生成（初回動作確認用）
    if not os.path.exists(RESULTS_FILE):
        sample_data = pd.DataFrame({
            "日付": ["2025-06-16", "2025-06-16", "2025-06-16"],
            "競艇場": ["唐津", "若松", "住之江"],
            "レース番号": ["12R", "11R", "10R"],
            "式別": ["2連単", "3連単", "単勝"],
            "投票内容": ["1-5", "4-5-6", "3"],
            "賭け金額": [100, 100, 100],
            "結果": ["的中", "不的中", "的中"],
            "払戻": [840, 0, 810],
        })
        sample_data.to_csv(RESULTS_FILE, index=False)

    df = pd.read_csv(RESULTS_FILE)

    if df.empty:
        st.info("まだ記録がありません。")
        return

    total_bets = len(df)
    total_amount = df["賭け金額"].sum()
    total_hits = len(df[df["結果"] == "的中"])
    total_payout = df["払戻"].sum()

    accuracy = round((total_hits / total_bets) * 100, 2) if total_bets else 0
    return_rate = round((total_payout / total_amount) * 100, 2) if total_amount else 0
    win_rate = round((total_hits / total_bets) * 100, 2) if total_bets else 0

    st.markdown("### 📈 集計結果")
    col1, col2, col3 = st.columns(3)
    col1.metric("総ベット数", f"{total_bets} 回")
    col2.metric("総賭け金", f"{total_amount:,} 円")
    col3.metric("的中数", f"{total_hits} 回")

    col4, col5 = st.columns(2)
    col4.metric("回収率", f"{return_rate} %")
    col5.metric("勝率", f"{win_rate} %")

    st.markdown("### 📋 最新10件")
    st.dataframe(df.tail(10), use_container_width=True)
