import streamlit as st
from datetime import datetime, timedelta

# ページ表示用モジュール読み込み
from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_boat_results import show_page as show_page5

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ✅ 現在の日本時間を表示（中央）
now = datetime.utcnow() + timedelta(hours=9)
jst = now.strftime('%Y/%m/%d %H:%M:%S')
st.markdown(f"<div style='text-align:center; font-size:24px;'>🕰️ 現在の時刻（日本時間）<br>{jst}</div><hr>", unsafe_allow_html=True)

# ✅ ページ選択セッション
if "page" not in st.session_state:
    st.session_state.page = "AI予想"

# ✅ メニュー形式のボタン（スマホ縦でも横でも見やすく）
col1, col2 = st.columns(2)
with col1:
    if st.button("① AI予想"):
        st.session_state.page = "AI予想"
with col2:
    if st.button("② 勝敗入力"):
        st.session_state.page = "勝敗入力"

col3, col4 = st.columns(2)
with col3:
    if st.button("③ 統計データ"):
        st.session_state.page = "統計データ"
with col4:
    if st.button("④ 結果履歴"):
        st.session_state.page = "結果履歴"

col5, col6, _ = st.columns([1, 1, 1])
with col5:
    if st.button("⑤ 競艇結果"):
        st.session_state.page = "競艇結果"

# ✅ ページ切替表示
if st.session_state.page == "AI予想":
    show_page1()
elif st.session_state.page == "勝敗入力":
    show_page2()
elif st.session_state.page == "統計データ":
    show_page3()
elif st.session_state.page == "結果履歴":
    show_page4()
elif st.session_state.page == "競艇結果":
    show_page5()

# ✅ フッター
st.markdown("<hr><div style='text-align:center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
