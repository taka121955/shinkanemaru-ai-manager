import streamlit as st
from datetime import datetime
import pytz

# ページ状態をセッションに保存
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# ページ切り替え用ボタン
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🏠 メイン"):
        st.session_state.page = 'main'
with col2:
    if st.button("🧠 AI予想"):
        st.session_state.page = 'ai'
with col3:
    if st.button("✍️ 勝敗入力"):
        st.session_state.page = 'result'

st.markdown("---")

# ページ表示関数
def show_main_page():
    st.title("🏠 メインページ")
    now = datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y-%m-%d %H:%M:%S")
    st.markdown(f"### 🕒 現在時刻：**{now}**")
    st.markdown("### 🎯 目標金額：**¥10,000**")
    st.markdown("### 💰 初期費用：**¥10,000**")
    st.markdown("### 📊 累積費用：**（自動反映）**")
    st.markdown("---")
    st.markdown("#### 👤 制作者：小島崇彦")

def show_ai_prediction_page():
    st.title("🧠 AI予想ページ")
    st.markdown("※ ここにAIによる予想結果が表示されます（開発中）")

def show_result_input_page():
    st.title("✍️ 勝敗入力ページ")
    st.markdown("※ ここに勝敗入力フォームを配置予定（開発中）")

# ページ表示
if st.session_state.page == 'main':
    show_main_page()
elif st.session_state.page == 'ai':
    show_ai_prediction_page()
elif st.session_state.page == 'result':
    show_result_input_page()
