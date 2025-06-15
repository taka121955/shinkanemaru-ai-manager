import streamlit as st
from datetime import datetime, timedelta

from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_boat_results import show_page as show_page5

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ✅ 日本時間の現在時刻を表示（中央寄せ）
now = datetime.utcnow() + timedelta(hours=9)
jst = now.strftime('%Y/%m/%d %H:%M:%S')
st.markdown(
    f"<h3 style='text-align: center;'>🕰️ 現在の時刻（日本時間）<br>{jst}</h3><hr>",
    unsafe_allow_html=True
)

# ✅ ページ初期設定
if "page" not in st.session_state:
    st.session_state.page = "①AI予想"

# ✅ 横一列ボタン（スマホでも横並び維持）
button_labels = ["①AI予想", "②勝敗入力", "③統計データ", "④結果履歴", "⑤競艇結果"]
cols = st.columns(5)
for i, col in enumerate(cols):
    with col:
        if st.button(button_labels[i]):
            st.session_state.page = button_labels[i]

st.markdown("<br>", unsafe_allow_html=True)

# ✅ ページ切替処理
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

# ✅ フッター
st.markdown("---")
st.markdown("<div style='text-align:center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
