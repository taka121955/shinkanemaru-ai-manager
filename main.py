import streamlit as st
from datetime import datetime
import pandas as pd
import os

# ページ切り替え管理
if "page" not in st.session_state:
    st.session_state.page = "① AI予想"

# タイトル非表示（デフォルトヘッダー消し）
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide")

# =============================
# 🔵 ページ上部：現在時刻・資金情報表示
# =============================

# 現在時刻（日本時間）
jst_now = datetime.utcnow().astimezone().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"<h2 style='text-align:center;'>{jst_now}（日本時間）</h2>", unsafe_allow_html=True)

# 目標金額・初期資金入力（固定欄）
col1, col2, col3 = st.columns(3)
with col1:
    target = st.number_input("🎯 目標金額", min_value=0, value=10000, step=100)
with col2:
    initial = st.number_input("💰 初期資金", min_value=0, value=10000, step=100)

# 結果ファイルから累積費用取得
csv_path = "shinkanemaru_ai_manager/results.csv"
if os.path.exists(csv_path):
    try:
        df = pd.read_csv(csv_path)
        total_bet = df["賭金"].sum()
    except Exception:
        total_bet = 0
else:
    total_bet = 0

with col3:
    st.metric("📊 累積費用", f"{int(total_bet)} 円")

# =============================
# 🟢 ページ切り替えボタン群
# =============================

st.markdown("---")

col_a, col_b, col_c = st.columns([1, 4, 1])
with col_b:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("① AI予想"):
            st.session_state.page = "① AI予想"
        if st.button("② 勝敗入力"):
            st.session_state.page = "② 勝敗入力"
        if st.button("③ 統計データ"):
            st.session_state.page = "③ 統計データ"
    with col2:
        if st.button("④ 結果履歴"):
            st.session_state.page = "④ 結果履歴"
        if st.button("⑤ 競艇結果"):
            st.session_state.page = "⑤ 競艇結果"

st.markdown("---")

# =============================
# 🔴 ページごとのコンテンツ読み込み
# =============================

if st.session_state.page == "① AI予想":
    import shinkanemaru_ai_manager.pages.page1_ai_prediction as page
    page.show()
elif st.session_state.page == "② 勝敗入力":
    import shinkanemaru_ai_manager.pages.page2_input_result as page
    page.show()
elif st.session_state.page == "③ 統計データ":
    import shinkanemaru_ai_manager.pages.page3_statistics as page
    page.show()
elif st.session_state.page == "④ 結果履歴":
    import shinkanemaru_ai_manager.pages.page4_record_result as page
    page.show()
elif st.session_state.page == "⑤ 競艇結果":
    import shinkanemaru_ai_manager.pages.page5_boat_results as page
    page.show()

# =============================
# 🔻 フッター制作者表示
# =============================

st.markdown("---")
st.markdown("<div style='text-align:right;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
