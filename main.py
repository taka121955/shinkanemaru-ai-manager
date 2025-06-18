# main.py

import streamlit as st
from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_today_schedule import show_page as show_page5  # ← 正式名に修正
from pages.page6_settings import show_page as show_page6
from pages.page7_per_boatplace_prediction import show_page as show_page7
from pages.page8_summary_today import show_page as show_page8

st.markdown("## 🎮 メニュー選択")

menu = st.radio("選択してください", [
    "① AI予想", "② 勝敗入力", "③ 統計データ", "④ 結果履歴",
    "⑤ 出走表", "⑥ 設定", "⑦ 競艇場別予想", "⑧ 本日のまとめ"
])

if menu == "① AI予想":
    show_page1()
elif menu == "② 勝敗入力":
    show_page2()
elif menu == "③ 統計データ":
    show_page3()
elif menu == "④ 結果履歴":
    show_page4()
elif menu == "⑤ 出走表":
    show_page5()  # ← ここも一致
elif menu == "⑥ 設定":
    show_page6()
elif menu == "⑦ 競艇場別予想":
    show_page7()
elif menu == "⑧ 本日のまとめ":
    show_page8()
