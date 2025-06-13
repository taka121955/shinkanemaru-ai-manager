import streamlit as st
from datetime import datetime
import pytz
import pandas as pd

# ページ設定
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide")

# 現在時刻（日本時間）
japan_time = datetime.now(pytz.timezone('Asia/Tokyo')).strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f"<h2 style='text-align:center;'>{japan_time}</h2>", unsafe_allow_html=True)

# 資金情報の入力
col1, col2, col3 = st.columns(3)
with col1:
    goal_amount = st.number_input("🎯 目標金額", value=10000, step=100)
with col2:
    initial_amount = st.number_input("💰 初期資金", value=10000, step=100)
with col3:
    try:
        df = pd.read_csv("results.csv")
        total_stake = df["賭金"].sum()
        total_return = df["払戻"].sum()
        cumulative_amount = initial_amount - total_stake + total_return
    except:
        cumulative_amount = initial_amount
    st.metric("📊 累積資金", f"{int(cumulative_amount)} 円")

# ボタンで各ページに遷移
st.markdown("---")
colA, colB, colC = st.columns([1,1,1])
with colA:
    if st.button("① AI予想", use_container_width=True):
        st.switch_page("pages/page1_ai_prediction.py")
with colB:
    if st.button("② 勝敗入力", use_container_width=True):
        st.switch_page("pages/page2_input_result.py")
with colC:
    if st.button("③ 統計データ", use_container_width=True):
        st.switch_page("pages/page3_statistics.py")

colD, colE, _ = st.columns([1,1,1])
with colD:
    if st.button("④ 結果履歴", use_container_width=True):
        st.switch_page("pages/page4_record_result.py")
with colE:
    if st.button("⑤ 競艇結果", use_container_width=True):
        st.switch_page("pages/page5_boat_results.py")

# 制作者名
st.markdown("---")
st.markdown("<div style='text-align:center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
