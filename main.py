import streamlit as st
from datetime import datetime, timedelta

from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ✅ 日本時間取得（UTC +9）
now = datetime.utcnow() + timedelta(hours=9)
jst_time = now.strftime('%Y/%m/%d %H:%M:%S')

# ✅ 現在時刻（中央寄せ）
st.markdown(f"<h3 style='text-align:center;'>🕰️ 現在の時刻（日本時間）：{jst_time}</h3>", unsafe_allow_html=True)

# ✅ セッション初期化
if "page" not in st.session_state:
    st.session_state.page = "①AI予想"

# ✅ ページ切替ボタン：縦並び・中央寄せスタイル
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)

if st.button("①AI予想"):
    st.session_state.page = "①AI予想"
if st.button("②勝敗入力"):
    st.session_state.page = "②勝敗入力"
if st.button("③統計データ"):
    st.session_state.page = "③統計データ"
if st.button("④結果履歴"):
    st.session_state.page = "④結果履歴"

st.markdown("</div>", unsafe_allow_html=True)

# ✅ ページ表示
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
