import streamlit as st
import pandas as pd

def show_page():
    st.set_page_config(page_title="① AI予想", layout="centered")
    st.title("① AI予想")

    # ✅ スプレッドシートCSV URL（シート1）
    csv_url = "https://docs.google.com/spreadsheets/d/1yfzSSgqA-1x2z-MF7xKnCMbFBJvb-7Kq4c84XSmRROg/export?format=csv&gid=0"

    try:
        df = pd.read_csv(csv_url)
        st.markdown("### 📋 本日のAI予想一覧（自動更新）")
        st.dataframe(df)
    except Exception as e:
        st.error("❌ データの読み込みに失敗しました。")
        st.code(str(e))

show_page()
