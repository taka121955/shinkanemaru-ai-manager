# pages/page5_today_schedule.py

import streamlit as st
from datetime import datetime

st.title("📅 本日の出走表")

# 今日の日付を自動表示
today = datetime.now().strftime("%Y年%m月%d日（%a）")
st.markdown(f"### 📆 {today}")

# 仮の開催競艇場リスト（今後自動取得化可）
today_boat_places = [
    "蒲郡競艇場",
    "住之江競艇場",
    "戸田競艇場",
    "丸亀競艇場",
    "芦屋競艇場",
    "宮島競艇場"
]

# 出走表を表示
for place in today_boat_places:
    st.markdown(f"#### 🏟️ {place}")
    st.markdown("　- 第1R ～ 第12R")
    st.markdown("---")
