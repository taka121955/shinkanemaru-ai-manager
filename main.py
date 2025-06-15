import streamlit as st
from datetime import datetime, timedelta

from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_boat_results import show_page as show_page5

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# 現在の日本時間を取得
now = datetime.utcnow() + timedelta(hours=9)
jst = now.strftime('%Y/%m/%d %H:%M:%S')

# 上部情報表示
st.markdown(f"<div style='text-align:center; font-size:24px;'>🕰️ 現在の時刻（日本時間）<br>{jst}</div>", unsafe_allow_html=True)
st.markdown("----")
st.markdown("💰 初期資金：10000円")
st.markdown("🎯 目標金額：10000円")
st.markdown("----")

# メニュー表示（番号と名前をテキストで表示）
st.markdown("<div style='text-align:center; font-size:22px;'>📘 メニュー</div><br>", unsafe_allow_html=True)
menu_items = [
    "① AI予想",
    "② 勝敗入力",
    "③ 統計データ",
    "④ 結果履歴",
    "⑤ 競艇結果"
]
for item in menu_items:
    st.markdown(f"<div style='text-align:center;'>{item}</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ページ管理（セッションステート）
if "page" not in st.session_state:
    st.session_state.page = "①"

# 下部のボタンを横並びで中央配置（数字のみ）
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("①"):
        st.session_state.page = "①"
with col2:
    if st.button("②"):
        st.session_state.page = "②"
with col3:
    if st.button("③"):
        st.session_state.page = "③"
with col4:
    if st.button("④"):
        st.session_state.page = "④"
with col5:
    if st.button("⑤"):
        st.session_state.page = "⑤"

# ページ遷移
if st.session_state.page == "①":
    show_page1()
elif st.session_state.page == "②":
    show_page2()
elif st.session_state.page == "③":
    show_page3()
elif st.session_state.page == "④":
    show_page4()
elif st.session_state.page == "⑤":
    show_page5()

# フッター
st.markdown("---")
st.markdown("<div style='text-align:center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
