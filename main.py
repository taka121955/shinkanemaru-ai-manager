import streamlit as st
from datetime import datetime

from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_boat_results import show_page as show_page5
from pages.page6_settings import show_page as show_page6

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# 🎯 日本時間の現在時刻
jst = datetime.utcnow().astimezone()
st.markdown(f"<h3 style='text-align: center;'>🕒 現在時刻（日本時間）：{jst.strftime('%Y/%m/%d %H:%M:%S')}</h3>", unsafe_allow_html=True)

# 💰 目標金額・初期資金・累積資金（仮に表示）
st.markdown("""
<div style='text-align: center; font-size: 18px;'>
🎯 目標金額：10000円　　💰 初期資金：5000円　　📊 累積資金：7200円
</div>
""", unsafe_allow_html=True)

# 🔘 メインボタンナビゲーション
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("①AI予想"):
        st.session_state["page"] = 1
    if st.button("②勝敗入力"):
        st.session_state["page"] = 2
with col2:
    if st.button("③統計データ"):
        st.session_state["page"] = 3
    if st.button("④結果履歴"):
        st.session_state["page"] = 4
with col3:
    if st.button("⑤競艇結果"):
        st.session_state["page"] = 5
    if st.button("⑥設定"):
        st.session_state["page"] = 6

# 🔄 ページ切り替え処理
if "page" not in st.session_state:
    st.session_state["page"] = 1  # 初期ページ

if st.session_state["page"] == 1:
    show_page1()
elif st.session_state["page"] == 2:
    show_page2()
elif st.session_state["page"] == 3:
    show_page3()
elif st.session_state["page"] == 4:
    show_page4()
elif st.session_state["page"] == 5:
    show_page5()
elif st.session_state["page"] == 6:
    show_page6()

# 👤 フッター
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
