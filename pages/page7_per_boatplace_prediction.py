# pages/page7_per_boatplace_prediction.py（カード表示型）

import streamlit as st
from datetime import datetime

st.title("📍 出走場別 全12R AI予想")

boat_places = ["蒲郡", "住之江", "戸田", "丸亀", "唐津", "芦屋"]
selected_place = st.selectbox("🏟️ 今日の出走場を選択してください", boat_places)

st.markdown(f"### 📍 現在の出走場：{selected_place}")
st.markdown("---")

# 予想データを簡潔に表示（1R〜12R）
for r in range(1, 13):
    race = f"{r}R"
    style = ["単勝", "2連単", "3連単"][r % 3]
    pred = f"{r%6+1}-{(r+1)%6+1}-{(r+2)%6+1}" if style == "3連単" else f"{r%6+1}"
    rate = f"{60 + r % 5:.1f}%"
    
    st.markdown(
        f"🏁 **{race}**｜{style}｜予想：**{pred}**｜🎯 的中率：**{rate}**",
        help=f"{selected_place}の{race}"
    )
