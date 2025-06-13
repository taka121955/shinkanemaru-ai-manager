import streamlit as st
from datetime import datetime
import pytz

# ページ構成の選択肢
pages = {
    "🧠 AI予想": "ai_prediction",
    "🏠 メイン": "main",
    "✍️ 勝敗入力": "result_input"
}

# サイドバーのメニュー
selection = st.sidebar.radio("ページを選択してください", list(pages.keys()))

# ページごとの処理
def show_main_page():
    st.title("🏠 メインページ")
    now = datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y-%m-%d %H:%M:%S")
    st.markdown(f"### 🕒 現在時刻：**{now}**")
    st.markdown("### 🎯 目標金額：**¥10,000**")
    st.markdown("### 💰 初期費用：**¥10,000**")
    st.markdown("### 📊 累積費用：**（自動反映）**")
    st.markdown("---")
    st.markdown("#### 👤 制作者：小島崇彦")

def show_ai_prediction():
    st.title("🧠 AI予想")
    st.markdown("※ここにAIによる予想を表示します（開発中）")

def show_result_input():
    st.title("✍️ 勝敗入力")
    st.markdown("※ここに勝敗結果の入力フォームを設置します（開発中）")

# 選択されたページの表示
if pages[selection] == "main":
    show_main_page()
elif pages[selection] == "ai_prediction":
    show_ai_prediction()
elif pages[selection] == "result_input":
    show_result_input()
