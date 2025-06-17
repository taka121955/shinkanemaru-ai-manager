# main.py

import streamlit as st
from pages.1_AI予想 import show_page as show_page1
from pages.2_勝敗入力 import show_page as show_page2
from pages.3_統計データ import show_page as show_page3
from pages.4_結果履歴 import show_page as show_page4
from pages.5_出走表 import show_page as show_page5
from pages.6_設定 import show_page as show_page6
from pages.page7_per_boatplace_prediction import show_page as show_page7
from pages.page8_summary_today import show_page as show_page8

# ✅ ページ選択（サイドバー）
selected_page = st.sidebar.radio("📑 ページ選択", [
    "① AI予想",
    "② 勝敗入力",
    "③ 統計データ",
    "④ 結果履歴",
    "⑤ 出走表",
    "⑥ 設定",
    "⑦ 出走場別12R予想",
    "⑧ 今日の結果まとめ"
])

# ✅ 各ページを表示
if selected_page == "① AI予想":
    show_page1()
elif selected_page == "② 勝敗入力":
    show_page2()
elif selected_page == "③ 統計データ":
    show_page3()
elif selected_page == "④ 結果履歴":
    show_page4()
elif selected_page == "⑤ 出走表":
    show_page5()
elif selected_page == "⑥ 設定":
    show_page6()
elif selected_page == "⑦ 出走場別12R予想":
    show_page7()
elif selected_page == "⑧ 今日の結果まとめ":
    show_page8()
