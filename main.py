import streamlit as st
from datetime import datetime
import pandas as pd
import os

# CSVファイルパス（Streamlit Cloud対応）
CSV_PATH = os.path.join(os.getcwd(), "results.csv")

# ページマッピング
PAGES = {
    "①AI予想": "pages.page1_ai_prediction",
    "②勝敗入力": "pages.page2_input_result",
    "③統計データ": "pages.page3_statistics",
    "④結果履歴": "pages.page4_record_result",
    "⑤競艇結果": "pages.page5_boat_results"
}

# 時刻と数値情報
def show_header():
    st.markdown("## 🕒 現在時刻（日本時間）")
    now_jst = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    st.markdown(f"<h3 style='text-align: center;'>{now_jst}</h3>", unsafe_allow_html=True)

    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("🎯 **目標金額：** 10000円")
    with col2:
        st.markdown("💰 **初期資金：** 10000円")
    with col3:
        if os.path.exists(CSV_PATH):
            df = pd.read_csv(CSV_PATH)
            df["収支"] = df["払戻金"] - df["賭金"]
            total_profit = df["収支"].sum()
        else:
            total_profit = 0
        st.markdown(f"📊 **累積金額：** {total_profit}円")

    st.markdown("---")

# ボタンでページ切り替え
def show_navigation():
    cols = st.columns([1,1])
    with cols[0]:
        if st.button("①AI予想"):
            st.session_state.page = "①AI予想"
        if st.button("②勝敗入力"):
            st.session_state.page = "②勝敗入力"
        if st.button("③統計データ"):
            st.session_state.page = "③統計データ"
    with cols[1]:
        if st.button("④結果履歴"):
            st.session_state.page = "④結果履歴"
        if st.button("⑤競艇結果"):
            st.session_state.page = "⑤競艇結果"
        if st.button("🏠メインに戻る"):
            st.session_state.page = "メイン"

# 初期ページ設定
if "page" not in st.session_state:
    st.session_state.page = "メイン"

# 画面構成
show_header()
show_navigation()

# ページ表示
if st.session_state.page == "メイン":
    st.markdown("📗 **メインページです**")
elif st.session_state.page in PAGES:
    module = __import__(PAGES[st.session_state.page], fromlist=[""])
    module.app()

# フッター
st.markdown("---")
st.markdown("👤 制作者：小島崇彦")
