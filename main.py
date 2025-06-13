import streamlit as st
import datetime
import pandas as pd
import os

# 各ページをインポート
from pages import (
    page1_ai_prediction,
    page2_input_result,
    page3_statistics,
    page4_record_result,
    page5_boat_results,
)

# ページ選択状態の保持
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "①AI予想"

# 📅 日本時間で現在時刻を表示
japan_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
st.markdown(f"<h3 style='text-align: center;'>🕓 現在時刻（日本時間）</h3>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center;'>{japan_time.strftime('%Y/%m/%d %H:%M:%S')}</h1>", unsafe_allow_html=True)

# 💰 目標金額・初期資金・累積損益の表示
target_amount = 10000
initial_fund = 10000
csv_file = "results.csv"

if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    df["収支"] = df["払戻"] - df["賭金"]
    total_profit = df["収支"].sum()
else:
    total_profit = 0

st.markdown("## 🎯目標金額：{}円".format(target_amount))
st.markdown("## 💰初期資金：{}円".format(initial_fund))
st.markdown("## 📊累積資金額：{}円".format(total_profit))

# 🔘 ページ選択ボタン
col1, col2 = st.columns(2)
with col1:
    if st.button("①AI予想"):
        st.session_state.selected_page = "①AI予想"
    if st.button("②勝敗入力"):
        st.session_state.selected_page = "②勝敗入力"
with col2:
    if st.button("③統計データ"):
        st.session_state.selected_page = "③統計データ"
    if st.button("④結果履歴"):
        st.session_state.selected_page = "④結果履歴"
    if st.button("⑤競艇結果"):
        st.session_state.selected_page = "⑤競艇結果"

# 🧭 選択中ページの表示
st.write("---")
if st.session_state.selected_page == "①AI予想":
    page1_ai_prediction.show()
elif st.session_state.selected_page == "②勝敗入力":
    page2_input_result.show()
elif st.session_state.selected_page == "③統計データ":
    page3_statistics.show()
elif st.session_state.selected_page == "④結果履歴":
    page4_record_result.show()
elif st.session_state.selected_page == "⑤競艇結果":
    page5_boat_results.show()

# 👤 制作者名
st.markdown("---")
st.markdown("👤 制作者：小島崇彦")
