# pages/page1_ai_prediction.py

import streamlit as st
import pandas as pd
from datetime import datetime

st.markdown("### ① AI予想")
st.markdown("🎯 本日のAIによる予想（上位5件）")

# 仮のAI予想データ
data = {
    "競艇場": ["芦屋", "戸田", "丸亀", "福岡", "鳴門"],
    "レース": ["5R", "2R", "3R", "5R", "1R"],
    "式別": ["2連単", "単勝", "2連単", "3連単", "単勝"],
    "予想": ["5-3-4", "1-2-3", "2-1-3", "2-6-6", "1-1-3"],
    "オッズ": [12.62, 12.69, 9.77, 16.25, 15.57]
}

# DataFrame作成
df = pd.DataFrame(data)

# オッズが1.5以上のものにフィルタ
df = df[df["オッズ"] >= 1.5]

# 上位5件のみ表示
st.dataframe(df.head(5), use_container_width=True)

# 現在時刻の表示
now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"🕒 現在時刻： **{now}**")

# 🔽 各ページへのボタン（ナビゲーション）
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.page_link("pages/page1_ai_prediction.py", label="① AI予想", icon="1️⃣")
with col2:
    st.page_link("pages/page2_input_result.py", label="② 勝敗入力", icon="2️⃣")
with col3:
    st.page_link("pages/page3_statistics.py", label="③ 統計データ", icon="3️⃣")
with col4:
    st.page_link("pages/page4_record_result.py", label="④ 結果履歴", icon="4️⃣")
