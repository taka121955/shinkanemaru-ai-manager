# page1_ai_prediction.py

import streamlit as st
import pandas as pd

def show_page():
    st.markdown("## 🎯 本日のAI予想（的中率トップ10）")

    data = [
        [1, "唐津", "1R", "2連単", "5-2", "89.0%"],
        [2, "住之江", "3R", "3連単", "6-3-3", "82.0%"],
        [3, "若松", "2R", "2連単", "1-6", "70.0%"],
    ]

    columns = ["順位", "競艇場", "レース番号", "式別", "投票内訳", "的中率"]
    df = pd.DataFrame(data, columns=columns)

    st.dataframe(df, use_container_width=True)
