import streamlit as st
import pandas as pd
from datetime import datetime

st.title("① AI予想")

# 仮のAI予想データ（上位5件）
ai_predictions = [
    {"日付": datetime.today().strftime('%Y/%m/%d'), "競艇場": "住之江", "レース": "1R", "式別": "3連単", "買い目": "1-2-3", "オッズ": 5.2},
    {"日付": datetime.today().strftime('%Y/%m/%d'), "競艇場": "戸田",   "レース": "2R", "式別": "2連単", "買い目": "2-4",   "オッズ": 4.8},
    {"日付": datetime.today().strftime('%Y/%m/%d'), "競艇場": "平和島", "レース": "3R", "式別": "3連単", "買い目": "3-1-2", "オッズ": 4.4},
    {"日付": datetime.today().strftime('%Y/%m/%d'), "競艇場": "大村",   "レース": "4R", "式別": "2連単", "買い目": "1-3",   "オッズ": 4.0},
    {"日付": datetime.today().strftime('%Y/%m/%d'), "競艇場": "芦屋",   "レース": "5R", "式別": "3連単", "買い目": "2-3-1", "オッズ": 3.9},
]

df = pd.DataFrame(ai_predictions)
st.dataframe(df, use_container_width=True)
