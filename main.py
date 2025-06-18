import streamlit as st
from datetime import datetime
import pytz

# ===== 各ページの読み込み =====
from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_boat_results import show_page as show_page5
from pages.page6_settings import show_page as show_page6
from pages.page7_venue_prediction import show_page as show_page7
from pages.page8_total_evaluation import show_page as show_page8
from pages.page9_special_analysis import show_page as show_page9

# ===== ページ基本設定 =====
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ===== 🕒 現在時刻（日本時間） =====
japan_time = datetime.now(pytz.timezone("Asia/Tokyo"))
formatted_time = japan_time.strftime("%Y年%m月%d日（%a） %H:%M")
st.markdown(f"<h2 style='text-align: center;'>{formatted_time}</h2>", unsafe_allow_html=True)
st.markdown("---")

# ===== 📊 今日のステータス 表示 =====
st.markdown("### 📊 今日のステータス")
col1, col2 = st.columns(2)
with col1:
    st.markdown("🎯 的中率：85%")
    st.markdown("📈 勝敗：3勝2敗")
    st.markdown("💰 積立金：+4,800円")
with col2:
    st.markdown("🏆 勝率：70%")
    st.markdown("💹 回収率：125%")
    st.markdown("🎒 軍資金：10,000円")
st.markdown("---")

# ===== 📁 メニュー一覧（ページ選択） =====
st.markdown("### 📁 メニュー一覧")
menu_options = [
    "① AI予想 🧠", "② 勝敗入力 ✍️", "③ 統計データ 📊",
    "④ 結果履歴 📁", "⑤ 開催結果 🏁", "⑥ 設定 ⚙️",
    "⑦ 場別予想 🏟️", "⑧ 総合評価 📊", "⑨ 特別分析 💡"
]

selected_page = st.sidebar.radio("📌 ページ選択", menu_options)

# ===== 📄 ページ分岐処理 =====
if selected_page == "① AI予想 🧠":
    show_page1()
elif selected_page == "② 勝敗入力 ✍️":
    show_page2()
elif selected_page == "③ 統計データ 📊":
    show_page3()
elif selected_page == "④ 結果履歴 📁":
    show_page4()
elif selected_page == "⑤ 開催結果 🏁":
    show_page5()
elif selected_page == "⑥ 設定 ⚙️":
    show_page6()
elif selected_page == "⑦ 場別予想 🏟️":
    show_page7()
elif selected_page == "⑧ 総合評価 📊":
    show_page8()
elif selected_page == "⑨ 特別分析 💡":
    show_page9()

# ===== フッター =====
st.markdown("---")
st.markdown("<div style='text-align:center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
