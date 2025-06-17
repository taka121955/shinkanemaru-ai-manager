import streamlit as st
import pandas as pd
import os

RESULTS_FILE = "results.csv"

def show_page():
    st.markdown("## ④ 結果履歴 📜")

    if not os.path.exists(RESULTS_FILE):
        st.info("記録ファイルが見つかりません。")
        return

    df = pd.read_csv(RESULTS_FILE)

    if df.empty:
        st.info("まだ結果が記録されていません。")
        return

    # 最新順に表示
    df_sorted = df.sort_values(by="日時", ascending=False)

    st.markdown("### 📊 全記録一覧（最新順）")
    st.dataframe(df_sorted, use_container_width=True)

    # ダウンロードボタン（CSV）
    csv = df_sorted.to_csv(index=False).encode('utf-8-sig')
    st.download_button(
        label="📥 CSV形式でダウンロード",
        data=csv,
        file_name="results_export.csv",
        mime="text/csv"
    )
