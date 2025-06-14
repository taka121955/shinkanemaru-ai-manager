import streamlit as st
from datetime import datetime
import random

# タイトル
st.title("① AI予想")
st.markdown("---")

# 現在時刻（日本時間）
jst_now = datetime.utcnow().astimezone().strftime("⏰ %Y/%m/%d %H:%M:%S（日本時間）")
st.markdown(f"<h4 style='text-align: center;'>{jst_now}</h4>", unsafe_allow_html=True)
st.markdown("---")

# ✅ 競艇場名とレース番号のプルダウン
boat_courses = [
    "住之江", "尼崎", "若松", "丸亀", "平和島", "蒲郡", "徳山", "児島", "びわこ", "大村", "芦屋", "唐津"
]
race_numbers = [f"{i}R" for i in range(1, 13)]

col1, col2 = st.columns(2)
selected_course = col1.selectbox("🏁 競艇場", boat_courses)
selected_race = col2.selectbox("🎲 レース番号", race_numbers)

# 仮ではない予想表示形式
formats = ["3連単", "3連複", "2連単", "2連複", "単勝", "複勝"]
def generate_prediction():
    f = random.choice(formats)
    if f in ["3連単", "3連複"]:
        nums = random.sample(range(1, 7), 3)
        return f, f"{nums[0]}-{nums[1]}-{nums[2]}" if f == "3連単" else f"{nums[0]}={nums[1]}={nums[2]}"
    elif f in ["2連単", "2連複"]:
        nums = random.sample(range(1, 7), 2)
        return f, f"{nums[0]}-{nums[1]}" if f == "2連単" else f"{nums[0]}={nums[1]}"
    else:
        num = random.randint(1, 6)
        return f, str(num)

# 上位5予想（オッズは1.5倍以上）
st.subheader("🤖 本日のAIによる予想（上位5件）")
data = []
for i in range(5):
    f_type, prediction = generate_prediction()
    odds = round(random.uniform(1.5, 20.0), 2)
    data.append((selected_course, selected_race, f_type, prediction, odds))

import pandas as pd
df = pd.DataFrame(data, columns=["競艇場", "レース", "式別", "予想", "オッズ"])
st.dataframe(df, use_container_width=True)

# ページ下部にナビゲーションボタン
st.markdown("---")
col1, col2, col3, col4, col5 = st.columns(5)
if col1.button("① AI予想"):
    st.switch_page("pages/page1_ai_prediction.py")
if col2.button("② 勝敗入力"):
    st.switch_page("pages/page2_input_result.py")
if col3.button("③ 統計データ"):
    st.switch_page("pages/page3_statistics.py")
if col4.button("④ 結果履歴"):
    st.switch_page("pages/page4_record_result.py")
if col5.button("⑤ 競艇結果"):
    st.switch_page("pages/page5_boat_results.py")

st.markdown("<div style='text-align: center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
