# pages/page5_today_schedule.py

import streamlit as st
from datetime import datetime

# ✅ サイドバー表示名＆レイアウト指定
st.set_page_config(page_title="⑤ 出走表", layout="centered")

def show_page():
    st.title("📅 本日の出走表")

    # 本日日付
    today = datetime.now().strftime("%Y年%m月%d日（%a）")
    st.markdown(f"### 📆 {today}")

    # 仮の出走場（後に自動取得可）
    boat_places_today = [
        "蒲郡競艇場",
        "住之江競艇場",
        "戸田競艇場",
        "丸亀競艇場",
        "芦屋競艇場",
        "宮島競艇場"
    ]

    # 出走表表示（12R固定）
    for place in boat_places_today:
        st.markdown(f"#### 🏟️ {place}")
        st.markdown("　・第1R ～ 第12R")
        st.markdown("---")
