# pages/page7_daily_predictions.py

import streamlit as st
import pandas as pd

st.set_page_config(page_title="⑦ 本日のAI予想", layout="centered")

def show_page():
    st.title("🎯 本日のAI予想一覧")
    st.markdown("#### 📍 出走場を選んで12Rの予想を確認")

    race_sites = ["蒲郡", "住之江", "戸田", "丸亀", "芦屋", "宮島"]
    selected_site = st.selectbox("🏟️ 出走場を選択", race_sites)

    st.markdown(f"### 📌 {selected_site} のAI予想（12R分）")

    data = {
        "R": [f"{i}R" for i in range(1, 13)],
        "式別": ["3連単"] * 12,
        "予想": ["1-2-3", "2-1-4", "3-2-1", "1-3-5", "4-1-2", "1-5-6",
                 "2-3-4", "3-1-2", "1-4-6", "2-1-5", "1-2-5", "3-2-6"],
        "自信度": ["◎", "○", "◎", "▲", "◎", "○", "▲", "○", "◎", "▲", "◎", "○"],
        "的中確率": ["75%", "72%", "78%", "68%", "80%", "74%", "65%", "70%", "77%", "67%", "76%", "71%"],
        "推奨金額": ["300円"] * 12
    }

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    st.info("※ AI予想は仮データです。実装後はAIモデル・データ自動更新に対応予定です。")
