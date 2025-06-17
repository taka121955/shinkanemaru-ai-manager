# pages/page5_today_schedule.py

import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="⑤ 本日の出走表", layout="centered")

def show_page():
    st.title("🚤 本日の出走表")

    st.markdown("#### 📅 本日開催される競艇場・レース一覧")

    # 仮の出走データ（あとでAPIやCSV連携可）
    data = {
        "競艇場": ["蒲郡", "住之江", "戸田", "丸亀", "芦屋", "宮島"],
        "開催グレード": ["G1", "一般", "一般", "G3", "G1", "一般"],
        "第1R 発走": ["10:30", "10:50", "11:05", "10:40", "10:25", "10:45"],
        "最終12R 発走": ["16:45", "17:00", "17:15", "17:05", "16:55", "17:10"]
    }

    df = pd.DataFrame(data)

    # 日付表示
    today = date.today().strftime("%Y年%m月%d日（%a）")
    st.markdown(f"🗓️ **{today} 現在のスケジュール**")

    # 出走表を表示
    st.dataframe(df, use_container_width=True)

    st.markdown("---")
    st.markdown("※ データは仮です。将来的にBOATRACE APIや日替わりCSVから取得可能です。")
