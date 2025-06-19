# pages/main.py

import streamlit as st
from datetime import datetime
import pytz

# ページ設定
st.set_page_config(page_title="新金丸法", layout="wide")

# 現在時刻
now = datetime.now(pytz.timezone("Asia/Tokyo"))
st.markdown(f"<h2 style='text-align: center;'>{now.strftime('%Y/%m/%d (%a) %H:%M')}</h2>", unsafe_allow_html=True)
st.markdown("---")

# サイドバー（日本語）
menu = st.sidebar.radio("📋 ページ選択", [
    "🏠 メインページ", "① AI予想", "② 勝敗入力", "③ 統計データ",
    "④ 結果履歴", "⑤ 開催結果", "⑥ 設定", "⑦ 場別予想", "⑧ 総合評価", "⑨ 特別分析"
], label_visibility="collapsed")

# 各ページの読み込み
if menu == "🏠 メインページ":
    st.write("ここにステータスや概要を表示")

elif menu == "① AI予想":
    from page1_ai_prediction import show_page; show_page()

elif menu == "② 勝敗入力":
    from page2_input_result import show_page; show_page()

elif menu == "③ 統計データ":
    from page3_statistics import show_page; show_page()

# 以下、page4〜page9も同様に追加してOK
