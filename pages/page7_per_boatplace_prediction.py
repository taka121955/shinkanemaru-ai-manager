# pages/page7_daily_predictions.py

import streamlit as st
import pandas as pd

st.set_page_config(page_title="⑦ 本日のAI予想", layout="centered")

def show_page():
    st.title("🎯 本日のAI予想一覧")

    st.markdown("#### 📍 出走場を選んで12Rの予想を確認")

    # ✅ 出走場の仮データ（今後自動反映可）
    race_sites = ["蒲郡", "住之江", "戸田", "丸亀", "芦屋", "宮島"]
    selected_site = st.selectbox("🏟️ 出走場を選択", race_sites)

    st.markdown(f"### 📌 {selected_site} のAI予想（12R分）")

    # ✅ 仮のAI予想データ（本番はAIモデル or CSV連携）
    data = {
        "R": [f"{i}R" for i in range(1, 13)],
        "式別": ["3連単"] * 12,
        "予想": ["1-2-3", "2-1-4", "3-2-1", "1-3-5", "4-1-2", "1-5-6",
                 "2-3-4", "3-1-2", "1-4-6", "2-1-5", "1-2-5", "3-2-6"],
        "買い目点数": [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        "自信度": ["◎", "○", "◎", "▲", "◎", "○", "▲", "○", "◎", "▲", "◎", "○"],
        "的中確率": ["75%", "72%", "78%", "68%", "80%", "74%", "65%", "70%", "77%", "67%", "76%", "71%"],
        "推奨金額": ["300円"] * 12
    }

    df = pd.DataFrame(data)

    # ✅ 表を固定風に表示（横スクロールなし）
    st.dataframe(df, use_container_width=True)

    st.markdown("---")
    st.info("※ AI予想は仮データです。実装後は自動更新またはモデル連携に切り替わります。")
