import streamlit as st
from datetime import datetime, timedelta

from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_boat_results import show_page as show_page5

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# 現在の日本時間を中央に表示
now = datetime.utcnow() + timedelta(hours=9)
jst = now.strftime('%Y/%m/%d %H:%M:%S')
st.markdown(f"<div style='text-align:center; font-size:24px;'>🕰️ 現在の時刻（日本時間）<br>{jst}</div><hr>", unsafe_allow_html=True)

# セッションでページ管理
if "page" not in st.session_state:
    st.session_state.page = "①"

# メニュー表示（文字ラベル）
st.markdown("#### メニュー：")

# ✅ ①と②を横並び
col1, col2 = st.columns(2)
with col1:
    if st.button("①"):
        st.session_state.page = "①"
        st.toast("AI予想を選択")
with col2:
    if st.button("②"):
        st.session_state.page = "②"
        st.toast("勝敗入力を選択")

# ✅ ③は中央に表示
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
if st.button("③"):
    st.session_state.page = "③"
    st.toast("統計データを選択")
st.markdown("</div>", unsafe_allow_html=True)

# ✅ ④と⑤を横並び
col3, col4 = st.columns(2)
with col3:
    if st.button("④"):
        st.session_state.page = "④"
        st.toast("結果履歴を選択")
with col4:
    if st.button("⑤"):
        st.session_state.page = "⑤"
        st.toast("競艇結果を選択")

# ページの切替表示
if st.session_state.page == "①":
    st.markdown("### ① AI予想")
    show_page1()
elif st.session_state.page == "②":
    st.markdown("### ② 勝敗入力")
    show_page2()
elif st.session_state.page == "③":
    st.markdown("### ③ 統計データ")
    show_page3()
elif st.session_state.page == "④":
    st.markdown("### ④ 結果履歴")
    show_page4()
elif st.session_state.page == "⑤":
    st.markdown("### ⑤ 競艇結果")
    show_page5()

# フッター
st.markdown("---")
st.markdown("<div style='text-align:center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
