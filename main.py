import streamlit as st
from datetime import datetime
import pytz

# 各ページインポート
from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_today_schedule import show_page as show_page5
from pages.page6_settings import show_page as show_page6
from pages.page7_per_boatplace_prediction import show_page as show_page7
from pages.page8_summary_today import show_page as show_page8
from pages.page9_reflection import show_page as show_page9

# ページ設定
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ===== 🕒 日本時間の現在時刻を中央表示 =====
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

# ===== 📁 メニュー一覧（装飾のみ） =====
st.markdown("### 📁 メニュー一覧")

menu_labels = [
    "① AI予想 🧠", "② 勝敗入力 ✍️", "③ 統計データ 📊",
    "④ 結果履歴 📁", "⑤ 開催結果 🏁", "⑥ 設定 ⚙️",
    "⑦ 場別予想 🏟️", "⑧ 総合評価 📊", "⑨ 特別分析 💡"
]

for i in range(0, 9, 3):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div style='text-align: center; font-size:20px;'>{menu_labels[i]}</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div style='text-align: center; font-size:20px;'>{menu_labels[i+1]}</div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div style='text-align: center; font-size:20px;'>{menu_labels[i+2]}</div>", unsafe_allow_html=True)
