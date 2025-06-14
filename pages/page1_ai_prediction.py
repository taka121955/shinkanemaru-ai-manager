import streamlit as st
from datetime import datetime
import random

# ページタイトル
st.title("① AI予想")
st.markdown("---")

# 現在の日本時間を中央に表示
jst_now = datetime.utcnow().astimezone().strftime("⏰ %Y/%m/%d %H:%M:%S（日本時間）")
st.markdown(f"<h4 style='text-align: center;'>{jst_now}</h4>", unsafe_allow_html=True)

# 🎯目標金額、💰初期資金、📊累積資金
if "goal" not in st.session_state:
    st.session_state.goal = 10000
if "initial" not in st.session_state:
    st.session_state.initial = 3000
if "current" not in st.session_state:
    st.session_state.current = st.session_state.initial

col1, col2, col3 = st.columns(3)
col1.metric("🎯目標金額", f"{st.session_state.goal:,} 円")
col2.metric("💰初期資金", f"{st.session_state.initial:,} 円")
col3.metric("📊累積資金", f"{st.session_state.current:,} 円")

st.markdown("---")

# プルダウン式で競艇場とレース番号を選択
boat_courses = [
    "住之江", "尼崎", "若松", "丸亀", "平和島", "蒲郡", "徳山", "児島", "びわこ", "大村", "芦屋", "唐津"
]
race_numbers = [f"{i}R" for i in range(1, 13)]

col1, col2 = st.columns(2)
selected_course = col1.selectbox("🏁 競艇場", boat_courses)
selected_race = col2.selectbox("🎲 レース番号", race_numbers)

# 仮ではない実際の形式で表示（式別ランダムに）
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

# 上位5予想（オッズはランダムで最低1.5以上）
st.subheader("🤖 AI予想（上位5）")

for i in range(5):
    f_type, prediction = generate_prediction()
    odds = round(random.uniform(1.5, 15.0), 2)
    st.markdown(f"**{i+1}.【{f_type}】{prediction}**　🧮想定オッズ：{odds}倍")

st.markdown("---")

# ページ下のナビゲーション
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

# フッター
st.markdown("---")
st.markdown("<div style='text-align: center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
