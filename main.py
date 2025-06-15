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
    f"<h3 style='text-align:center;'>🕰️ 現在の時刻（日本時間）<br>{jst}</h3><hr>",
    unsafe_allow_html=True
)

# ✅ セッションでページを記録
if "page" not in st.session_state:
    st.session_state.page = "①AI予想"

# ✅ ボタンを 2列×2段で中央揃えに配置（styleも含めて綺麗に）
st.markdown("<div style='display: flex; justify-content: center; flex-wrap: wrap; gap: 15px;'>", unsafe_allow_html=True)

if st.button("①AI予想", key="b1"):
    st.session_state.page = "①AI予想"
if st.button("②勝敗入力", key="b2"):
    st.session_state.page = "②勝敗入力"
if st.button("③統計データ", key="b3"):
    st.session_state.page = "③統計データ"
if st.button("④結果履歴", key="b4"):
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
