import streamlit as st
import pandas as pd
from datetime import datetime

st.markdown("### ① AI予想")
st.markdown("🎯 本日のAIによる予想（上位5件）")

# 本物形式に準拠した仮データ（式別ごとに予想の書式も統一）
data = {
    "競艇場": ["戸田", "住之江", "丸亀", "福岡", "芦屋"],
    "レース": ["1R", "2R", "3R", "4R", "5R"],
    "式別": ["3連単", "3連複", "2連単", "2連複", "単勝"],
    "予想": ["1-2-3", "1=2=3", "1-2", "1=2", "1"],
    "オッズ": [18.6, 12.5, 7.8, 4.2, 1.7]
}

df = pd.DataFrame(data)

# オッズ1.5以上でフィルター（ご要望通り）
df = df[df["オッズ"] >= 1.5].head(5)

# 表示
st.dataframe(df, use_container_width=True)

# 現在時刻
now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"🕒 現在時刻： **{now}**")

# ——ページ下部にナビゲーション（サイドバー非表示構成）
cols = st.columns(4)
buttons = [
    ("① AI予想", "page1_ai_prediction", "1️⃣"),
    ("② 勝敗入力", "page2_input_result", "2️⃣"),
    ("③ 統計データ", "page3_statistics", "3️⃣"),
    ("④ 結果履歴", "page4_record_result", "4️⃣")
]
for col, (label, path, icon) in zip(cols, buttons):
    with col:
        st.button(f"{icon} {label}", on_click=lambda p=path: st.experimental_set_query_params(page=p))
