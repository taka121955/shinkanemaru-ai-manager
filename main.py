import streamlit as st
from datetime import datetime
from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# 現在時刻の表示
now = datetime.now()
st.markdown(f"## 🕰️ 現在時刻（日本時間）：{now.strftime('%Y/%m/%d %H:%M:%S')}")

# セッションステートでページ管理
if "page" not in st.session_state:
    st.session_state.page = "①AI予想"

# ページ切り替えボタン
cols = st.columns(4)
with cols[0]:
    if st.button("①AI予想"):
        st.session_state.page = "①AI予想"
with cols[1]:
    if st.button("②勝敗入力"):
        st.session_state.page = "②勝敗入力"
with cols[2]:
    if st.button("③統計データ"):
        st.session_state.page = "③統計データ"
with cols[3]:
    if st.button("④結果履歴"):
        st.session_state.page = "④結果履歴"

# ページの表示
if st.session_state.page == "①AI予想":
    show_page1()
elif st.session_state.page == "②勝敗入力":
    show_page2()
elif st.session_state.page == "③統計データ":
    show_page3()
elif st.session_state.page == "④結果履歴":
    show_page4()

# フッター
st.markdown("---")
st.markdown("制作者：小島崇彦")
