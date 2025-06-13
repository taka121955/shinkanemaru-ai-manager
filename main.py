import streamlit as st
from datetime import datetime
import pandas as pd
import pytz
import os

# ファイル定義
csv_file = "results.csv"

# ページ切替ステート
if "page" not in st.session_state:
    st.session_state.page = "main"

# ⏰ 現在時刻（日本時間）
japan = pytz.timezone("Asia/Tokyo")
now = datetime.now(japan)
st.markdown(f"<h3 style='text-align: center;'>🕒 現在時刻（日本時間）</h3>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center;'>{now.strftime('%Y/%m/%d %H:%M:%S')}</h1>", unsafe_allow_html=True)

# 💰 初期資金と累積金額（仮データまたはファイル読み取り）
initial_amount = 10000
target_amount = 10000
accumulated_amount = 0

if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    if "収支" in df.columns:
        accumulated_amount = df["収支"].sum()

# 🎯 統計情報
st.markdown(f"🎯 目標金額：{target_amount}円")
st.markdown(f"💰 初期資金：{initial_amount}円")
st.markdown(f"📊 累積資金額：{accumulated_amount}円")

# 🔘 ページ切り替えボタン群（中央整列）
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("①AI予想"):
        st.session_state.page = "ai"
with col2:
    if st.button("②勝敗入力"):
        st.session_state.page = "input"
with col3:
    if st.button("③統計データ"):
        st.session_state.page = "stats"
with col4:
    if st.button("④結果履歴"):
        st.session_state.page = "history"
with col5:
    if st.button("⑤競艇結果"):
        st.session_state.page = "results"

# 📄 各ページ内容の表示
if st.session_state.page == "ai":
    st.markdown("🧠 **AI予想ページ（ここにAI予想の内容を表示）**")
elif st.session_state.page == "input":
    st.markdown("🎮 **勝敗入力ページ（勝敗記録フォーム）**")
elif st.session_state.page == "stats":
    st.markdown("📊 **統計データページ（勝率や回収率などを表示）**")
elif st.session_state.page == "history":
    st.markdown("📖 **結果履歴ページ（記録一覧）**")
elif st.session_state.page == "results":
    st.markdown("🏁 **競艇結果ページ（外部結果連携など）**")
else:
    st.markdown("🔰 **メインページです**")

# 👤 制作者名
st.markdown("---")
st.markdown("👤 制作者：小島崇彦")
