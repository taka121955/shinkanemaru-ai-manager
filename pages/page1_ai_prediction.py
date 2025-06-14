import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.title("① AI予想")
st.write("🎯 本日のAIによる予想（上位5件）")

# 仮のAI予想データ（後ほどAI連携可能）
sample_data = []
racenames = ["1R", "2R", "3R", "4R", "5R", "6R", "7R", "8R", "9R", "10R", "11R", "12R"]
boats = ["住之江", "丸亀", "鳴門", "福岡", "戸田", "芦屋"]

for _ in range(5):
    boat = random.choice(boats)
    race = random.choice(racenames)
    bet_type = random.choice(["3連単", "2連単", "単勝"])
    prediction = f"{random.randint(1,6)}-{random.randint(1,6)}-{random.randint(1,6)}"
    odds = round(random.uniform(3.0, 25.0), 2)
    sample_data.append([boat, race, bet_type, prediction, odds])

df = pd.DataFrame(sample_data, columns=["競艇場", "レース", "式別", "予想", "オッズ"])

# 表示
st.dataframe(df, use_container_width=True)

# 現在時刻（日本時間）
now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"🕒 現在時刻：**{now}**")

# --------------------
# 🔽 ナビゲーション（ページ下部ボタン）
# --------------------
st.markdown("---")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("① AI予想"):
        st.switch_page("pages/page1_ai_prediction.py")

with col2:
    if st.button("② 勝敗入力"):
        st.switch_page("pages/page2_input_result.py")

with col3:
    if st.button("③ 統計データ"):
        st.switch_page("pages/page3_statistics.py")

with col4:
    if st.button("④ 結果履歴"):
        st.switch_page("pages/page4_record_result.py")

with col5:
    if st.button("⑤ レース結果"):
        st.switch_page("pages/page5_boat_results.py")

# 最下部に制作者表記
st.markdown("<p style='text-align: center;'>制作者：小島崇彦</p>", unsafe_allow_html=True)
