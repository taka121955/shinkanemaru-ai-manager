# pages/page7_per_boatplace_prediction.py（エクセル風）

import streamlit as st
import pandas as pd
from datetime import datetime

st.title("📍 出走場別 全12R AI予想")

# 出走場の選択
boat_places = ["蒲郡", "住之江", "戸田", "丸亀", "唐津", "芦屋"]
selected_place = st.selectbox("🏟️ 今日の出走場を選択してください", boat_places)

st.markdown(f"### 📌 現在の出走場：**{selected_place}**")
st.markdown("---")

# ダミーデータ生成（本番はAI予想と連携）
def generate_predictions(place):
    today = datetime.now().strftime("%Y-%m-%d")
    data = []
    for r in range(1, 13):
        style = ["単勝", "2連単", "3連単"][r % 3]
        pred = (
            f"{r%6+1}-{(r+1)%6+1}-{(r+2)%6+1}" if style == "3連単"
            else f"{r%6+1}"
        )
        data.append({
            "レース": f"{r}R",
            "式別": style,
            "予想": pred,
            "的中率": f"{60 + r % 5:.1f}%",
        })
    return pd.DataFrame(data)

df = generate_predictions(selected_place)

# ✅ エクセル風に表示（スクロールなし、スマホ対応◎）
st.table(df)
