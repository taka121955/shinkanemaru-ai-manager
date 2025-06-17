import streamlit as st
import pandas as pd
from datetime import datetime

def show_page():
    st.set_page_config(page_title="① AI予想", layout="centered")

    st.title("① AI予想")
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    st.markdown(f"🕒 現在時刻（日本時間）： `{now}`")

    # 仮データ10件（実際はCSV読み込み予定）
    data = {
        "競艇場": ["住之江", "戸田", "芦屋", "丸亀", "蒲郡", "常滑", "徳山", "宮島", "若松", "桐生"],
        "レース": ["12R", "10R", "11R", "9R", "7R", "8R", "6R", "5R", "4R", "3R"],
        "式別": ["3連単", "2連複", "単勝", "3連複", "2連単", "3連単", "単勝", "3連単", "2連複", "3連複"],
        "予想": ["1-2-3", "2-4", "3", "1-4-6", "2-5", "3-2-4", "6", "5-1-3", "1-3", "2-5-6"],
        "金額": ["1,000円", "500円", "300円", "400円", "800円", "500円", "300円", "400円", "700円", "500円"],
        "確率": ["83%", "74%", "68%", "72%", "79%", "65%", "70%", "60%", "75%", "67%"]
    }

    df = pd.DataFrame(data)

    st.markdown("### 🔟 本日のAI予想一覧")
    st.table(df)
