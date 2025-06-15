import streamlit as st
from datetime import datetime, timedelta

from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_boat_results import show_page as show_page5

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ✅ 日本時間表示
now = datetime.utcnow() + timedelta(hours=9)
jst = now.strftime('%Y/%m/%d %H:%M:%S')
st.markdown(
    f"<div style='text-align:center; font-size:24px;'>🕰️ 現在の時刻（日本時間）<br>{jst}</div><hr>",
    unsafe_allow_html=True
)

# ✅ セッションでページ記憶
if "page" not in st.session_state:
    st.session_state.page = "①AI予想"

# ✅ ボタン配置（横並び2列、ラベルをボタンの下に）
button_info = [
    ("①AI予想", "①"),
    ("②勝敗入力", "②"),
    ("③統計データ", "③"),
    ("④結果履歴", "④"),
    ("⑤競艇結果", "⑤"),
]

# 2列 × 複数行
for i in range(0, len(button_info), 2):
    cols = st.columns(2)
    for j in range(2):
        if i + j < len(button_info):
            label, short = button_info[i + j]
            with cols[j]:
                if st.button(short, key=label):
                    st.session_state.page = label
                st.markdown(f"<div style='text-align:center'>{label}</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ✅ ページ切替処理
page_map = {
    "①AI予想": show_page1,
    "②勝敗入力": show_page2,
    "③統計データ": show_page3,
    "④結果履歴": show_page4,
    "⑤競艇結果": show_page5,
}

if st.session_state.page in page_map:
    page_map[st.session_state.page]()

# ✅ フッター
st.markdown("---")
st.markdown("<div style='text-align:center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
