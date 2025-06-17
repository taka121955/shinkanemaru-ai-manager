import streamlit as st
from datetime import datetime
import pandas as pd

def show_page():
    # ページ設定（必ず最初）
    st.set_page_config(page_title="① AI予想", layout="centered")

    st.title("① AI予想")
    st.markdown("▶️ **現在時刻（日本時間）** ： " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

    # 予想データ（10件）
    data = {
        "競艇場": ["住之江", "戸田", "芦屋", "丸亀", "蒲郡", "平和島", "唐津", "若松", "江戸川", "びわこ"],
        "レース": ["12R", "10R", "11R", "9R", "7R", "5R", "8R", "6R", "12R", "4R"],
        "式別": ["3連単", "2連複", "単勝", "3連複", "2連単", "単勝", "2連単", "3連単", "3連複", "2連複"],
        "予想": ["1-2-3", "2-4", "3", "1-4-6", "5-1", "4", "1-3", "2-3-6", "3-4-6", "1-2"],
        "金額": ["1,000円", "500円", "300円", "400円", "800円", "300円", "600円", "700円", "500円", "400円"],
        "確率": ["83%", "74%", "68%", "72%", "79%", "64%", "71%", "76%", "69%", "73%"]
    }

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
