# pages/page4_record_result.py

import streamlit as st
import pandas as pd

st.set_page_config(page_title="④ 結果履歴", layout="centered")

def show_page():
    st.title("📖 結果履歴")

    try:
        df = pd.read_csv("results.csv")
    except FileNotFoundError:
        st.warning("⚠️ データがまだありません。勝敗入力してください。")
        return

    if df.empty:
        st.warning("⚠️ データがまだ登録されていません。")
        return

    st.markdown("### 📋 登録されたすべての結果")

    # 日付順に並び替え（新しい順）
    df_sorted = df.sort_values(by="日付", ascending=False)

    st.dataframe(df_sorted, use_container_width=True)
