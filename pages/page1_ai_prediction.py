import streamlit as st
st.set_page_config(page_title="① AI予想", layout="centered")

from datetime import datetime

def show_page():
    st.title("🧠 AI予想")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.markdown(f"#### ⏰ 現在時刻：{now}")
    st.markdown("---")

    predictions = [
        {"競艇場": "蒲郡", "レース": "1R", "式別": "3連単", "予想": "1-2-3", "確率": "76%"},
        {"競艇場": "住之江", "レース": "5R", "式別": "2連単", "予想": "2-4", "確率": "68%"},
        {"競艇場": "戸田", "レース": "12R", "式別": "単勝", "予想": "6", "確率": "64%"},
    ]

    for p in predictions:
        st.markdown(
            f"🏟️ **{p['競艇場']}**｜{p['レース']}｜{p['式別']}｜🎯 予想：**{p['予想']}**｜的中確率：**{p['確率']}**"
        )
