import streamlit as st
st.set_page_config(page_title="⑧ 今日の結果まとめ", layout="centered")

import pandas as pd

def show_page():
    st.title("📊 今日の結果まとめ")
    try:
        df = pd.read_csv("results.csv")
        today = pd.Timestamp.now().strftime("%Y-%m-%d")
        df_today = df[df["日付"] == today]
        if df_today.empty:
            st.warning("📭 今日のデータはまだありません。")
        else:
            st.dataframe(df_today, use_container_width=True)
    except:
        st.warning("❌ 'results.csv' が存在しません。")
