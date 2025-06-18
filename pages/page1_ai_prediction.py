import streamlit as st
import pandas as pd

def show_page():
    st.set_page_config(page_title="① AI予想", layout="centered")
    st.title("① AI予想")

    # ✅ ヘッダー＆フッダー非表示CSS
    st.markdown("""
        <style>
        /* ヘッダー（ハンバーガー＆Shareボタン等）非表示 */
        header {visibility: hidden;}
        /* フッダー（Streamlitロゴ）非表示 */
        footer {visibility: hidden;}
        /* bodyスクロール防止（画面固定） */
        body {
            overflow: hidden;
        }
        </style>
    """, unsafe_allow_html=True)

    # ✅ スプレッドシートCSV URL
    csv_url = "https://docs.google.com/spreadsheets/d/1yfzSSgqA-1x2z-MF7xKnCMbFBJvb-7Kq4c84XSmRROg/export?format=csv&gid=0"

    try:
        df = pd.read_csv(csv_url)
        st.markdown("### 📋 本日のAI予想一覧（自動更新）")
        st.dataframe(df)
    except Exception as e:
        st.error("❌ データの読み込みに失敗しました。")
        st.code(str(e))

show_page()
