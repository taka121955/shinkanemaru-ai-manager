import streamlit as st
import pandas as pd
from datetime import datetime

st.title("① AI予想")

# ダミー予想（本番はAI予測に置き換える）
ai_predictions = [
    {"日付": datetime.today().strftime('%Y/%m/%d'), "競艇場": "住之江", "レース": "1R", "式別": "3連単", "買い目": "1-2-3", "オッズ": 4.2},
    {"日付": datetime.today().strftime('%Y/%m/%d'), "競艇場": "戸田", "レース": "2R", "式別": "2連単", "買い目": "2-4", "オッズ": 3.7},
]

df = pd.DataFrame(ai_predictions)
st.dataframe(df, use_container_width=True)
