import streamlit as st
from datetime import datetime, timedelta

from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ✅ 現在の日本時間を中央に表示
now = datetime.utcnow() + timedelta(hours=9)
jst = now.strftime('%Y/%m/%d %H:%M:%S')
st.markdown(
    f"<div style='text-align:center; font-size:24px;'>🕰️ 現在の時刻（日本時間）：<br>{jst}</div><br>",
    unsafe_allow_html=True
)

# ✅ セッションでページを記録
if "page" not in st.session_state:
    st.session_state.page = "①AI予想"

# ✅ ボタンを2列 × 2段で中央配置
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="medium")
with col1:
    if st.button("①AI予想"):
        st.session_state.page = "①AI予想"
with col2:
    if st.button("②勝敗入力"):
        st.session_state.page = "②勝敗入力"

col3, col4 = st.columns([1, 1], gap="medium")
with col3:
    if st.button("③統計データ"):
        st.session_state.page = "③統計データ"
with col4:
    if st.button("④結果履歴"):
        st.session_state.page = "④結果履歴"

st.markdown("</div><br>", unsafe_allow_html=True)

# ✅ ページ切替処理
if st.session_state.page == "①AI予想":
    show_page1()
elif st.session_state.page == "②勝敗入力":
    show_page2()
elif st.session_state.page == "③統計データ":
    show_page3()
elif st.session_state.page == "④結果履歴":
    show_page4()

# ✅ フッター（中央寄せ）
st.markdown("---")
st.markdown("<div style='text-align:center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
