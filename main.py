import streamlit as st
from datetime import datetime, timedelta

from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_boat_results import show_page as show_page5  # ← ⑤ページがある場合

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide")

# ✅ 現在の日本時間
now = datetime.utcnow() + timedelta(hours=9)
jst = now.strftime('%Y/%m/%d %H:%M:%S')
st.markdown(
    f"<h3 style='text-align:center;'>🕰️ 現在の時刻（日本時間）<br>{jst}</h3><hr>",
    unsafe_allow_html=True
)

# ✅ セッションでページ管理
if "page" not in st.session_state:
    st.session_state.page = "①AI予想"

# ✅ レスポンシブなボタン配置（縦横対応）
cols = st.columns(3)
with cols[0]:
    if st.button("①AI予想"):
        st.session_state.page = "①AI予想"
    if st.button("③統計データ"):
        st.session_state.page = "③統計データ"
with cols[1]:
    if st.button("②勝敗入力"):
        st.session_state.page = "②勝敗入力"
    if st.button("④結果履歴"):
        st.session_state.page = "④結果履歴"
with cols[2]:
    if st.button("⑤競艇結果"):
        st.session_state.page = "⑤競艇結果"

# ✅ ページ表示切替
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

# ✅ フッター（中央）
st.markdown("---")
st.markdown("<div style='text-align:center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
