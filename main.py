import streamlit as st
from datetime import datetime
from pages.page1_ai_prediction import show_ai_prediction  # ← AI予想の表示関数をインポート

# ページ設定
st.set_page_config(
    page_title="新金丸法 × AI資金マネージャー",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ページ初期化
if "page" not in st.session_state:
    st.session_state.page = 0  # 初期は何も表示しない

# ヘッダー：現在時刻と資金状況
jst = datetime.utcnow().astimezone()
st.markdown(f"<h3 style='text-align: center;'>🕒 現在時刻（日本時間）：{jst.strftime('%Y/%m/%d %H:%M:%S')}</h3>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; font-size: 18px;'>
🎯 目標金額：10000円　💰 初期資金：5000円　📊 累積立資金：7200円
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# ボタン（横並び・整形済み）
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("①AI予想"):
        st.session_state.page = 1
with col2:
    if st.button("②勝敗入力"):
        st.session_state.page = 2
with col3:
    if st.button("③統計データ"):
        st.session_state.page = 3

col4, col5, col6 = st.columns(3)
with col4:
    if st.button("④結果履歴"):
        st.session_state.page = 4
with col5:
    if st.button("⑤競艇結果"):
        st.session_state.page = 5
with col6:
    if st.button("⑥設定"):
        st.session_state.page = 6

# ページ内容表示（①のみ有効）
if st.session_state.page == 1:
    show_ai_prediction()

# フッター
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
