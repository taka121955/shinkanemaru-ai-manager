# pages/page4_record_result.py

import streamlit as st
import pandas as pd

st.markdown("### 📄 結果履歴")
st.write("これまでの勝敗結果・賭け金・払戻などを一覧で確認できます。")

# CSVから読み込み
try:
    df = pd.read_csv("results.csv")

    if df.empty:
        st.info("まだ結果が記録されていません。")
    else:
        df["的中"] = df["的中"].replace({1: "◯", 0: "×"})
        df["日付"] = pd.to_datetime(df["日付"]).dt.strftime("%Y/%m/%d %H:%M")
        df = df.sort_values(by="日付", ascending=False)

        st.dataframe(df, use_container_width=True)
except FileNotFoundError:
    st.warning("記録ファイル（results.csv）が見つかりません。")
