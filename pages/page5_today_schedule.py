# pages/page5_today_schedule.py

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="⑤ 出走表", layout="centered")

def show_page():
    st.title("📅 本日の出走表")

    today = datetime.now().strftime("%Y年%m月%d日（%a）")
    st.markdown(f"### 📆 {today}")

    boat_places_today = [
        "蒲郡競艇場", "住之江競艇場", "戸田競艇場",
        "丸亀競艇場", "芦屋競艇場", "宮島競艇場"
    ]

    for place in boat_places_today:
        st.markdown(f"#### 🏟️ {place}")
        st.markdown("　・第1R ～ 第12R")
        st.markdown("---")
