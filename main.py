import streamlit as st
from datetime import datetime
import pytz

# 各ページをインポート
from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_boat_results import show_page as show_page5

# ページ設定
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ===== 🕒 日本時間の現在時刻を中央表示 =====
japan_time = datetime.now(pytz.timezone("Asia/Tokyo"))
formatted_time = japan_time.strftime("%Y年%m月%d日（%a） %H:%M")

st.markdown(f"<h2 style='text-align: center;'>{formatted_time}</h2>", unsafe_allow_html=True)
st.markdown("---")

# ===== 📁 サイドバーでページ切り替え =====
selected_page = st.sidebar.radio("📁 ページ選択", [
    "① AI予想", "② 勝敗入力", "③ 統計データ", "④ 結果履歴", "⑤ 開催結果"
])

# ===== ✅ ページ表示処理 =====
if selected_page == "① AI予想":
    show_page1()
elif selected_page == "② 勝敗入力":
    show_page2()
elif selected_page == "③ 統計データ":
    show_page3()
elif selected_page == "④ 結果履歴":
    show_page4()
elif selected_page == "⑤ 開催結果":
    show_page5()
