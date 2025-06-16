import streamlit as st
from datetime import datetime
import pytz

# ページタイトルとレイアウト
st.set_page_config(page_title="資金マネージャー", layout="wide")

# 日本時間の現在時刻を表示（中央・太字・やや大きめ）
japan_time = datetime.now(pytz.timezone("Asia/Tokyo"))
st.markdown(
    f"<h3 style='text-align: center; font-weight: bold;'>現在時刻：{japan_time.strftime('%Y年%m月%d日 %H:%M:%S')}</h3>",
    unsafe_allow_html=True
)

# === 📊 2列 × 3行のエクセル風配置（見た目だけ） ===
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🎯 目標金額")
    st.markdown("#### 10000円")
with col2:
    st.markdown("### 🏆 勝率")
    st.markdown("#### 50%")

col3, col4 = st.columns(2)
with col3:
    st.markdown("### 💰 準備資金")
    st.markdown("#### 10000円")
with col4:
    st.markdown("### 🎯 的中率")
    st.markdown("#### 85%")

col5, col6 = st.columns(2)
with col5:
    st.markdown("### 📊 積立資金")
    st.markdown("#### 0円")
with col6:
    st.markdown("### 💹 回収率")
    st.markdown("#### 125%")

# === 🔘 メニューボタン（①〜⑥）を 2列×3行のグリッド配置 ===
menu_col1, menu_col2 = st.columns(2)

with menu_col1:
    if st.button("① AI予想"):
        st.session_state.page = "① AI予想"
    if st.button("③ 統計データ"):
        st.session_state.page = "③ 統計データ"
    if st.button("⑤ 開催結果"):
        st.session_state.page = "⑤ 開催結果"

with menu_col2:
    if st.button("② 勝敗入力"):
        st.session_state.page = "② 勝敗入力"
    if st.button("④ 結果履歴"):
        st.session_state.page = "④ 結果履歴"
    if st.button("⑥ 設定"):
        st.session_state.page = "⑥ 設定"

# === ページ遷移処理 ===
if "page" not in st.session_state:
    st.session_state.page = "① AI予想"

if st.session_state.page == "① AI予想":
    from pages import page1_ai_prediction
    page1_ai_prediction.app()
elif st.session_state.page == "② 勝敗入力":
    from pages import page2_input_result
    page2_input_result.app()
elif st.session_state.page == "③ 統計データ":
    from pages import page3_statistics
    page3_statistics.app()
elif st.session_state.page == "④ 結果履歴":
    from pages import page4_record_result
    page4_record_result.app()
elif st.session_state.page == "⑤ 開催結果":
    from pages import page5_boat_results
    page5_boat_results.app()
elif st.session_state.page == "⑥ 設定":
    from pages import page6_settings
    page6_settings.app()

# 制作者名
st.markdown("---")
st.markdown("<p style='text-align: center;'>制作者：小島崇彦</p>", unsafe_allow_html=True)
