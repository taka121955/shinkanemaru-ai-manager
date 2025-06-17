# pages/page5_today_schedule.py

import streamlit as st
from datetime import datetime

# ✅ ページ名設定（サイドバー表示名に反映）
st.set_page_config(page_title="⑤ 出走表", layout="centered")

def show_page():
    st.title("📅 本日の出走表")

    # 📆 今日の日付を表示（例：2025年06月17日（火））
    today = datetime.now().strftime("%Y年%m月%d日（%a）")
    st.markdown(f"### 📆 {today}")

    # 仮の本日開催予定の競艇場リスト（将来はAPI対応可）
    boat_places_today = [
        "蒲郡競艇場",
        "住之江競艇場",
        "戸田競艇場",
        "丸亀競艇場",
        "芦屋競艇場",
        "宮島競艇場"
    ]

    # 各競艇場ごとに「1R〜12R」の表示
    for place in boat_places_today:
        st.markdown(f"#### 🏟️ {place}")
        st.markdown("　・第1R ～ 第12R")
        st.markdown("---")
