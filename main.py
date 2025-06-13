import streamlit as st
from datetime import datetime
import pandas as pd
import pytz
import os

# CSVファイル
csv_file = "results.csv"

# ページ状態
if "page" not in st.session_state:
    st.session_state.page = "main"

# ⏰ 日本時間で現在時刻を表示
japan = pytz.timezone("Asia/Tokyo")
now = datetime.now(japan)
st.markdown(f"<h3 style='text-align: center;'>🕒 現在時刻（日本時間）</h3>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center;'>{now.strftime('%Y/%m/%d %H:%M:%S')}</h1>", unsafe_allow_html=True)

# 💰 初期資金・累積金額の表示
initial_amount = 10000
target_amount = 10000
accumulated_amount = 0

if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    if "収支" in df.columns:
        accumulated_amount = df["収支"].sum()

st.markdown(f"🎯 目標金額：{target_amount}円")
st.markdown(f"💰 初期資金：{initial_amount}円")
st.markdown(f"📊 累積資金額：{accumulated_amount}円")

# 🔘 ページ切替ボタン（中央揃え2列）
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("①AI予想"):
        st.session_state.page = "ai"
with col3:
    if st.button("②勝敗入力"):
        st.session_state.page = "input"

col4, col5, col6 = st.columns([1, 1, 1])
with col4:
    if st.button("③統計データ"):
        st.session_state.page = "stats"
with col6:
    if st.button("④結果履歴"):
        st.session_state.page = "history"

col7, col8, col9 = st.columns([1, 1, 1])
with col5:
    if st.button("⑤競艇結果"):
        st.session_state.page = "results"

# ページ表示内容
if st.session_state.page == "ai":
    st.markdown("🧠 **AI予想ページ（ここにAI予想を表示）**")
elif st.session_state.page == "input":
    st.markdown("🎮 **勝敗入力ページ（記録用）**")
elif st.session_state.page == "stats":
    st.markdown("📊 **統計データページ（勝率・回収率など）**")
elif st.session_state.page == "history":
    st.markdown("📖 **結果履歴ページ（一覧表など）**")
elif st.session_state.page == "results":
    st.markdown("🏁 **競艇結果ページ（外部リンク・情報）**")
else:
    st.markdown("🟢 **メインページです**")

# 制作者名
st.markdown("---")
st.markdown("👤 制作者：小島崇彦")
