import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

def show_page():
    st.markdown("## ① AI予想")

    # 日本時間の現在時刻を表示
    jst = pytz.timezone("Asia/Tokyo")
    now = datetime.now(jst).strftime("%Y/%m/%d %H:%M:%S")
    st.markdown(f"🕒 現在時刻（日本時間）：**{now}**")

    # 仮のAI予想データ（※後で本物と差し替え予定）
    predictions = [
        {"競艇場": "住之江", "レース": "12R", "式別": "3連単", "予想": "1-2-3", "金額": "1,000円", "確率": "83%"},
        {"競艇場": "戸田", "レース": "10R", "式別": "2連複", "予想": "2-4", "金額": "500円", "確率": "74%"},
        {"競艇場": "芦屋", "レース": "11R", "式別": "単勝", "予想": "3", "金額": "300円", "確率": "68%"},
        {"競艇場": "丸亀", "レース": "9R", "式別": "3連複", "予想": "1-4-6", "金額": "400円", "確率": "72%"},
        {"競艇場": "蒲郡", "レース": "7R", "式別": "2連単", "予想": "5-1", "金額": "800円", "確率": "79%"}
    ]

    df = pd.DataFrame(predictions)
    st.table(df)
