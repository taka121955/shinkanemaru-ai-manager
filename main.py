import streamlit as st
from datetime import datetime
import pytz

# 日本時間取得
japan_time = datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y/%m/%d %H:%M:%S")

# 初期設定
initial_funds = 10000
target_funds = 10000
cumulative_profit = 5000

# ページ切替用のセッション状態
if "page" not in st.session_state:
    st.session_state.page = "main"

# ページ切り替え関数
def switch_page(name):
    st.session_state.page = name

# ---------- メインページ ----------
if st.session_state.page == "main":
    st.markdown(f"### 🕓 現在時刻（日本時間）\n#### {japan_time}")
    st.markdown(f"### 🎯 目標金額：{target_funds}円")
    st.markdown(f"### 💰 初期資金：{initial_funds}円")
    st.markdown(f"### 📊 累積金額：{cumulative_profit}円")

    st.markdown("---")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("①AI予想"):
            switch_page("ai")
    with col2:
        if st.button("②勝敗入力"):
            switch_page("input")
    with col3:
        if st.button("③統計データ"):
            switch_page("stats")
    with col4:
        if st.button("④勝敗履歴"):
            switch_page("history")
    with col5:
        if st.button("⑤競艇結果"):
            switch_page("results")
    st.markdown("---")
    st.markdown("👤 **制作者：小島崇彦**")

# ---------- 各ページ ----------
elif st.session_state.page == "ai":
    st.markdown("## 🧠 AI予想ページ（ここにAI予想の内容を表示）")
    if st.button("← メインへ戻る"):
        switch_page("main")

elif st.session_state.page == "input":
    st.markdown("## ✍️ 勝敗入力ページ（ここに入力フォームを表示）")
    if st.button("← メインへ戻る"):
        switch_page("main")

elif st.session_state.page == "stats":
    st.markdown("## 📈 統計データページ（ここに統計情報を表示）")
    if st.button("← メインへ戻る"):
        switch_page("main")

elif st.session_state.page == "history":
    st.markdown("## 📖 勝敗履歴ページ（ここに履歴を表示）")
    if st.button("← メインへ戻る"):
        switch_page("main")

elif st.session_state.page == "results":
    st.markdown("## 🏁 競艇結果ページ（ここに各レースの結果を表示）")
    if st.button("← メインへ戻る"):
        switch_page("main")
