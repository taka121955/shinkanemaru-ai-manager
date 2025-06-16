# pages/page7_per_boatplace_prediction.py

import streamlit as st
import pandas as pd
from datetime import datetime

st.title("📍 出走場別 全12R AI予想")

# 仮の出走場リスト（後で自動化可）
boat_places = ["蒲郡", "住之江", "戸田", "丸亀", "唐津", "芦屋"]

selected_place = st.selectbox("🏟️ 今日の出走場を選択してください", boat_places)

# 仮データ作成（1R〜12R × 最も的中率の高い予想）
def generate_mock_predictions(place):
    today = datetime.now().strftime("%Y-%m-%d")
    data = []
    for r in range(1, 13):
        data.append({
            "日付": today,
            "競艇場": place,
            "レース": f"{r}R",
            "式別": "3連単",
            "予想": f"{r % 6 + 1}-{(r + 1) % 6 + 1}-{(r + 2) % 6 + 1}",
            "金額": "100円",
            "的中率": f"{60 + r % 5:.1f}%",
        })
    return pd.DataFrame(data)

df = generate_mock_predictions(selected_place)

st.write(f"🔽 {selected_place} の全12R AI予想（最も的中率の高い予想のみ表示）")
st.dataframe(df, use_container_width=True)
