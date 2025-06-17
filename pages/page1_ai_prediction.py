import streamlit as st
import pandas as pd
from datetime import datetime

# ✅ 必ず最初にこの行を書く（重要）
st.set_page_config(page_title="① AI予想", layout="centered")

def show_page():
    st.markdown("## ① AI予想")

    # 現在時刻の表示（日本時間）
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    st.markdown(f"🕒 現在時刻（日本時間） ：**{now}**")

    # データ読み込み（ファイルがあれば読み込む）
    try:
        df = pd.read_csv("ai_predictions.csv")
        st.table(df)
    except FileNotFoundError:
        st.warning("予想データ（ai_predictions.csv）が見つかりません。")
