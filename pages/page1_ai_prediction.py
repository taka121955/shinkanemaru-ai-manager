import streamlit as st
from datetime import datetime
import pandas as pd

# ✅ ページ設定（必ず一番最初に置くこと）
st.set_page_config(page_title="① AI予想", layout="centered")

def show_page():
    st.markdown("## ① AI予想 🔮")
    st.markdown(f"🕒 現在時刻（日本時間）： `{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}`")

    # ✅ 表示データ（仮の10件予想）
    data = pd.DataFrame([
        ["住之江", "12R", "3連単", "1-2-3", "1,000円", "83%"],
        ["戸田",   "10R", "2連複", "2-4",   "500円",   "74%"],
        ["芦屋",   "11R", "単勝",   "3",     "300円",   "68%"],
        ["丸亀",   "9R",  "3連複", "1-4-6", "400円",   "72%"],
        ["蒲郡",   "7R",  "2連単", "5-1",   "800円",   "79%"],
        ["大村",   "6R",  "単勝",   "2",     "500円",   "70%"],
        ["若松",   "11R", "3連単", "4-1-5", "600円",   "76%"],
        ["唐津",   "10R", "2連複", "3-6",   "400円",   "73%"],
        ["徳山",   "8R",  "3連単", "1-3-6", "700円",   "80%"],
        ["児島",   "5R",  "単勝",   "6",     "200円",   "65%"],
    ], columns=["競艇場", "レース", "式別", "予想", "金額", "確率"])

    st.dataframe(data, use_container_width=True)
