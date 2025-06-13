import streamlit as st
import pandas as pd
import os

def show():
    st.header("📖 勝敗履歴")

    csv_file = "shinkanemaru_ai_manager/results.csv"

    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        st.dataframe(df)
        st.download_button("📥 CSVダウンロード", df.to_csv(index=False), "results.csv", "text/csv")
    else:
        st.info("まだ勝敗履歴がありません。")
