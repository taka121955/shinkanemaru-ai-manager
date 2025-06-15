import streamlit as st
from datetime import datetime, timedelta

# ページ読み込み
from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_boat_results import show_page as show_page5

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# 🌏 日本時間を中央に表示
jst_now = datetime.utcnow() + timedelta(hours=9)
st.markdown(
    f"<div style='text-align:center; font-size:24px;'>🕰️ 現在の時刻（日本時間）<br>{jst_now.strftime('%Y/%m/%d %H:%M:%S')}</div>",
    unsafe_allow_html=True
)

# 💴 初期資金・目標金額（セッション保存）
if "initial_fund" not in st.session_state:
    st.session_state.initial_fund = 10000
if "target_fund" not in st.session_state:
    st.session_state.target_fund = 10000

st.markdown("---")
cols_fund = st.columns(2)
with cols_fund[0]:
    st.markdown(f"**💰 初期資金：{st.session_state.initial_fund}円**")
with cols_fund[1]:
    st.markdown(f"**🎯 目標金額：{st.session_state.target_fund}円**")

st.markdown("---")
st.markdown("<div style='text-align:center; font-size:20px;'>📘 <strong>メニュー</strong></div>", unsafe_allow_html=True)
st.markdown("")

# 📋 ページ切り替えのセッション
if "page" not in st.session_state:
    st.session_state.page = "①AI予想"

# 📌 ボタン配置（①②／③④／⑤）
col1, col2 = st.columns(2)
with col1:
    if st.button("①AI予想"):
        st.session_state.page = "①AI予想"
with col2:
    if st.button("②勝敗入力"):
        st.session_state.page = "②勝敗入力"

col3, col4 = st.columns(2)
with col3:
    if st.button("③統計データ"):
        st.session_state.page = "③統計データ"
with col4:
    if st.button("④結果履歴"):
        st.session_state.page = "④結果履歴"

# 🛥️ ⑤競艇結果（中央1列配置）
st.markdown("")
center_col = st.columns(3)
with center_col[1]:  # 中央の列
    if st.button("⑤競艇結果"):
        st.session_state.page = "⑤競艇結果"

st.markdown("---")

# ✅ 表示ページ
if st.session_state.page == "①AI予想":
    show_page1()
elif st.session_state.page == "②勝敗入力":
    show_page2()
elif st.session_state.page == "③統計データ":
    show_page3()
elif st.session_state.page == "④結果履歴":
    show_page4()
elif st.session_state.page == "⑤競艇結果":
    show_page5()

# 📎 フッター
st.markdown("---")
st.markdown("<div style='text-align:center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
