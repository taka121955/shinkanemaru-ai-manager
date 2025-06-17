# pages/5_出走表.py

import streamlit as st
from datetime import datetime

# ✅ サイドバーに表示されるページ名とレイアウトを明示
st.set_page_config(page_title="⑤ 出走表", layout="centered")

def show_page():
    st.title("📅 本日の出走表")

    # 今日の日付を表示（例：2025年6月17日（火））
    today = datetime.now().strftime("%Y年%m月%d日（%a）")
    st.markdown(f"### 📆 {today}")

    # 仮の本日開催競艇場（将来API化OK）
    boat_places_today = [
        "蒲郡競艇場",
        "住之江競艇場",
        "戸田競艇場",
        "丸亀競艇場",
        "芦屋競艇場",
        "宮島競艇場"
    ]

    # 出走表の表示（1場ごとに1R〜12Rと見出し付き）
    for place in boat_places_today:
        st.markdown(f"#### 🏟️ {place}")
        st.markdown("　・第1R ～ 第12R")
        st.markdown("---")
