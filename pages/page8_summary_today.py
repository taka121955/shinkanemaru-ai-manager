# pages/page8_today_result_summary.py

import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="⑧ 今日の結果まとめ", layout="centered")

def show_page():
    st.title("📅 今日の結果まとめ")

    today = date.today().strftime("%Y年%m月%d日（%a）")
    st.markdown(f"### 🗓️ {today} の集計結果")

    data = {
        "競艇場": ["蒲郡", "住之江", "戸田", "丸亀"],
        "的中レース数": [5, 3, 4, 6],
        "ベット回数": [12, 12, 12, 12],
        "的中率": ["41.7%", "25.0%", "33.3%", "50.0%"],
        "総ベット金額": [3600, 3600, 3600, 3600],
        "払戻金額": [5200, 2300, 3100, 6200],
        "回収率": ["144.4%", "63.9%", "86.1%", "172.2%"]
    }

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    st.markdown("※ データは仮です。将来は入力履歴からの自動集計へ対応します。")
