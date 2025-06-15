import streamlit as st
from datetime import datetime, timedelta

from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ✅ 現在の日本時間を表示
now = datetime.utcnow() + timedelta(hours=9)
jst = now.strftime('%Y/%m/%d %H:%M:%S')
st.markdown(
    f"<div style='text-align:center; font-size:22px;'>🕰️ 現在の時刻（日本時間）<br><b>{jst}</b></div><hr>",
    unsafe_allow_html=True
)

# ✅ ページ記録
if "page" not in st.session_state:
    st.session_state.page = "①AI予想"

# ✅ 2列ボタン中央配置（スマホでも安定する幅）
st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    if st.button("①AI予想", use_container_width=True):
        st.session_state.page = "①AI予想"
    if st.button("③統計データ", use_container_width=True):
        st.session_state.page = "③統計データ"
with col2:
    if st.button("②勝敗入力", use_container_width=True):
        st.session_state.page = "②勝敗入力"
    if st.button("④結果履歴", use_container_width=True):
        st.session_state.page = "④結果履歴"

st.markdown("</div><br>", unsafe_allow_html=True)

# ✅ ページ切り替え
if st.session_state.page == "①AI予想":
    show_page1()
elif st.session_state.page == "②勝敗入力":
    show_page2()
elif st.session_state.page == "③統計データ":
    show_page3()
elif st.session_state.page == "④結果履歴":
    show_page4()

# ✅ フッター
st.markdown("---")
st.markdown("<div style='text-align:center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
