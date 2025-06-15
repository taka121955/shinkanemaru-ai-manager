# pages/page4_record_result.py

import streamlit as st
import pandas as pd
import os

def show_page():
    st.header("④結果履歴")

    csv_path = "results.csv"

    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)

        if df.empty:
            st.info("📭 現在、記録されている結果はありません。")
        else:
            st.dataframe(df, use_container_width=True)

            # 並べ替えオプション
            sort_column = st.selectbox("🔽 並び替え列を選択", df.columns)
            sort_order = st.radio("順序", ["昇順", "降順"], horizontal=True)
            sorted_df = df.sort_values(by=sort_column, ascending=(sort_order == "昇順"))
            st.dataframe(sorted_df, use_container_width=True)

            # CSVダウンロード
            csv = sorted_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 CSVとしてダウンロード",
                data=csv,
                file_name='結果履歴.csv',
                mime='text/csv'
            )

    else:
        st.warning("⚠️ 結果ファイル（results.csv）がまだ存在していません。")
