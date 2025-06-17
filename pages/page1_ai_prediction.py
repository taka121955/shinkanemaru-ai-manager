import streamlit as st

# ✅ ページ設定（必ず一番上に配置）
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ✅ 各ページの読み込み（関数名で読み込み）
from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_today_schedule import show_page as show_page5
from pages.page6_settings import show_page as show_page6
from pages.page7_per_boatplace_prediction import show_page as show_page7
from pages.page8_summary_today import show_page as show_page8

# ✅ サイドバー（メニュー）
selected_page = st.sidebar.radio("📑 メニュー選択", [
    "① AI予想",
    "② 勝敗入力",
    "③ 統計データ",
    "④ 結果履歴",
    "⑤ 出走表",
    "⑥ 設定",
    "⑦ 出走場別12R予想",
    "⑧ 今日の結果まとめ"
])

# ✅ ページ切り替え
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
