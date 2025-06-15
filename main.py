import streamlit as st
from datetime import datetime, timedelta

from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_boat_results import show_page as show_page5

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ✅ 日本時間の現在時刻（中央表示）
now = datetime.utcnow() + timedelta(hours=9)
jst_time = now.strftime('%Y/%m/%d %H:%M:%S')
st.markdown(
    f"<h4 style='text-align:center;'>🕰️ 現在の時刻（日本時間）<br>{jst_time}</h4><hr>",
    unsafe_allow_html=True
)

# ✅ メニュー表示（中央寄せ）
st.markdown("""
<div style='text-align: center; font-size: 20px;'>
📘<b>メニュー</b><br><br>
①AI予想<br>
②勝敗入力<br>
③統計データ<br>
④結果履歴<br>
⑤競艇結果
</div><br>
""", unsafe_allow_html=True)

# ✅ ページ状態の初期化
if "page" not in st.session_state:
    st.session_state.page = "①AI予想"

# ✅ 横並びボタン（2列 × 3段）
col1, col2 = st.columns(2)
with col1:
    if st.button("①"):
        st.session_state.page = "①AI予想"
with col2:
    if st.button("②"):
        st.session_state.page = "②勝敗入力"

col3, col4 = st.columns(2)
with col3:
    if st.button("③"):
        st.session_state.page = "③統計データ"
with col4:
    if st.button("④"):
        st.session_state.page = "④結果履歴"

col5, col6 = st.columns(2)
with col5:
    if st.button("⑤"):
        st.session_state.page = "⑤競艇結果"

st.markdown("<br>", unsafe_allow_html=True)

# ✅ ページ切り替え
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

# ✅ フッター（中央寄せ）
st.markdown("---")
st.markdown("<div style='text-align:center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
