# main.py

import streamlit as st
from datetime import datetime
import pytz
import sys
import os
import pandas as pd  # メインページ用の表に使用

# ===== pages フォルダを読み込む設定 =====
pages_dir = os.path.join(os.path.dirname(__file__), "pages")
if pages_dir not in sys.path:
    sys.path.append(pages_dir)

# ===== ページ設定 =====
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide")

# ===== 現在時刻（中央表示） =====
now = datetime.now(pytz.timezone("Asia/Tokyo"))
st.markdown(f"<h2 style='text-align: center;'>{now.strftime('%Y年%m月%d日（%a） %H:%M')}</h2>", unsafe_allow_html=True)
st.markdown("---")

# ===== サイドバー（日本語メニュー） =====
menu = st.sidebar.radio("📋 ページ選択", [
    "🏠 メインページ", "① AI予想", "② 勝敗入力", "③ 統計データ",
    "④ 結果履歴", "⑤ 開催結果", "⑥ 設定", "⑦ 場別予想", "⑧ 総合評価", "⑨ 特別分析"
], label_visibility="collapsed")

# ===== ページ切替処理 =====
if menu == "🏠 メインページ":
    st.markdown("## 🎯 現在の資金ステータス")
    st.write("以下は現在の資金状況と統計情報の概要です。")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🎯 目標金額", "100,000円")
    with col2:
        st.metric("💰 初期資金", "30,000円")
    with col3:
        st.metric("📊 累積収支", "12,000円")

    st.markdown("---")
    st.markdown("### 📁 ページ一覧")

    st.table(pd.DataFrame({
        "メニュー番号": ["①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨"],
        "ページ名": [
            "AI予想", "勝敗入力", "統計データ", "結果履歴", "開催結果",
            "設定", "場別予想", "総合評価", "特別分析"
        ]
    }))

elif menu == "① AI予想":
    from page1_ai_prediction import show_page; show_page()

elif menu == "② 勝敗入力":
    from page2_input_result import show_page; show_page()

elif menu == "③ 統計データ":
    from page3_statistics import show_page; show_page()

elif menu == "④ 結果履歴":
    from page4_record_result import show_page; show_page()

elif menu == "⑤ 開催結果":
    from page5_today_schedule import show_page; show_page()

elif menu == "⑥ 設定":
    from page6_settings import show_page; show_page()

elif menu == "⑦ 場別予想":
    from page7_per_boatplace_prediction import show_page; show_page()

elif menu == "⑧ 総合評価":
    from page8_summary_today import show_page; show_page()

elif menu == "⑨ 特別分析":
    from page9_reflection import show_page; show_page()

# ===== 制作者表示 =====
st.markdown("---")
st.markdown("<div style='text-align: center;'>制作：小島崇彦</div>", unsafe_allow_html=True)
