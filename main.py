import streamlit as st
from datetime import datetime, timedelta
from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_boat_results import show_page as show_page5

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# 日本時間
now = datetime.utcnow() + timedelta(hours=9)
jst = now.strftime('%Y/%m/%d %H:%M:%S')

# セッション管理
if "page" not in st.session_state:
    st.session_state.page = "メイン"
if "initial_funds" not in st.session_state:
    st.session_state.initial_funds = 0
if "target_funds" not in st.session_state:
    st.session_state.target_funds = 0
if "total_funds" not in st.session_state:
    st.session_state.total_funds = 0

# ✅ 現在時刻と資金情報を中央表示
st.markdown(f"<div style='text-align:center; font-size:24px;'>🕰️ 現在の時刻（日本時間）<br>{jst}</div><hr>", unsafe_allow_html=True)

col0, col1 = st.columns(2)
with col0:
    st.session_state.initial_funds = st.number_input("💰初期資金（円）", value=st.session_state.initial_funds, step=100)
with col1:
    st.session_state.target_funds = st.number_input("🎯目標金額（円）", value=st.session_state.target_funds, step=100)

st.session_state.total_funds = st.session_state.initial_funds  # 後で勝敗データから更新可能
st.markdown(f"<div style='text-align:center;'>📊 累積資金：{st.session_state.total_funds} 円</div><br>", unsafe_allow_html=True)

# ✅ ページ切り替えボタン（縦と横両対応）
st.markdown("<hr><div style='text-align:center;'>", unsafe_allow_html=True)

# ボタン表示：スマホでも2列を維持
col1, col2 = st.columns(2)
with col1:
    if st.button("①AI予想"):
        st.session_state.page = "①AI予想"
with col2:
    if st.button("②勝敗入力"):
        st.session_state.page = "②勝敗入力"

col3, col4 = st.columns(2)
with col3:
    if st.button("③統計データ"):
        st.session_state.page = "③統計データ"
with col4:
    if st.button("④結果履歴"):
        st.session_state.page = "④結果履歴"

col5, _ = st.columns([1, 1])
with col5:
    if st.button("⑤競艇結果"):
        st.session_state.page = "⑤競艇結果"

st.markdown("</div><br>", unsafe_allow_html=True)

# ✅ ページ切り替え
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
