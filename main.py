import streamlit as st
from datetime import datetime, timedelta

from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_boat_results import show_page as show_page5

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# 日本時間を表示
now = datetime.utcnow() + timedelta(hours=9)
jst = now.strftime('%Y/%m/%d %H:%M:%S')
st.markdown(
    f"<div style='text-align:center; font-size:24px;'>🕰️ 現在の時刻（日本時間）<br>{jst}</div><hr>",
    unsafe_allow_html=True
)

# ページセッション初期化
if "page" not in st.session_state:
    st.session_state.page = "①"

# ボタン＋ラベル表示（中央配置）
options = [
    ("①", "AI予想"),
    ("②", "勝敗入力"),
    ("③", "統計データ"),
    ("④", "結果履歴"),
    ("⑤", "競艇結果")
]

for num, label in options:
    cols = st.columns([1, 5])
    with cols[0]:
        if st.button(num):
            st.session_state.page = num
    with cols[1]:
        st.markdown(f"<div style='padding-top: 6px;'>{label}</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ページ切替
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
