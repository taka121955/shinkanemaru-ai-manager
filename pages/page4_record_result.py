import streamlit as st
import pandas as pd
import os

# ファイルパス
RESULTS_FILE = "results.csv"

st.title("④ 結果履歴")

# 結果ファイルが存在するか確認
if os.path.exists(RESULTS_FILE):
    df = pd.read_csv(RESULTS_FILE)
    if df.empty:
        st.info("まだ結果が入力されていません。")
    else:
        st.dataframe(df)
        # CSVダウンロードボタン
        csv = df.to_csv(index=False).encode("utf-8-sig")
        st.download_button("CSVをダウンロード", csv, "結果履歴.csv", "text/csv")
else:
    st.warning("結果ファイルが存在しません。")
