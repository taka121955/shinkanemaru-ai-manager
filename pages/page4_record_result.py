import streamlit as st
st.set_page_config(page_title="④ 結果履歴", layout="centered")

import pandas as pd

def show_page():
    st.title("📖 ベット結果の履歴")
    try:
        df = pd.read_csv("results.csv")
        st.dataframe(df, use_container_width=True)
    except:
        st.warning("❌ データが存在しません。")
