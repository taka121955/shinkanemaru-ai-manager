import streamlit as st
from datetime import datetime
import pytz

# ページ構成設定
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide")

# ===== 🕒 日本時間の現在時刻を中央表示 =====
japan_time = datetime.now(pytz.timezone("Asia/Tokyo"))
formatted_time = japan_time.strftime("%Y年%m月%d日（%a） %H:%M")
st.markdown(f"<h2 style='text-align: center; font-size: 24px;'>{formatted_time}</h2>", unsafe_allow_html=True)
st.markdown("---")

# ===== 📊 ステータス表示 =====
st.markdown("<h3 style='text-align: center;'>📊 今日のステータス</h3>", unsafe_allow_html=True)
status_html = """
<div style='display: flex; justify-content: center;'>
  <table style='font-size:18px; border-spacing: 16px;'>
    <tr><td>🎯 <b>的中率：</b></td><td>85%</td></tr>
    <tr><td>📈 <b>勝敗：</b></td><td>3勝2敗</td></tr>
    <tr><td>💰 <b>積立金：</b></td><td>+4,800円</td></tr>
    <tr><td>🏆 <b>勝率：</b></td><td>70%</td></tr>
    <tr><td>✅ <b>回収率：</b></td><td>125%</td></tr>
    <tr><td>🎒 <b>軍資金：</b></td><td>10,000円</td></tr>
  </table>
</div>
"""
st.markdown(status_html, unsafe_allow_html=True)
st.markdown("---")

# ===== 📁 サイドバー日本語・カラフル対応 =====
st.sidebar.markdown("## 📋 ページメニュー")

menu = st.sidebar.radio("ページを選択してください", [
    "🏠 メインページ",
    "① 🔮 AI予想",
    "② ✍️ 勝敗入力",
    "③ 📊 統計データ",
    "④ 📁 結果履歴",
    "⑤ 🗓️ 開催結果",
    "⑥ ⚙️ 設定",
    "⑦ 🏟️ 場別予想",
    "⑧ 📌 総合評価",
    "⑨ 💡 特別分析"
], label_visibility="collapsed")

# ===== 🔁 ページ遷移処理（ここでは一部のみ仮に記述）=====
if menu == "🏠 メインページ":
    st.info("左のメニューからページを選んでください。")
elif menu == "① 🔮 AI予想":
    from pages.page1_ai_prediction import show_page
    show_page()
elif menu == "② ✍️ 勝敗入力":
    from pages.page2_input_result import show_page
    show_page()
elif menu == "③ 📊 統計データ":
    from pages.page3_statistics import show_page
    show_page()
elif menu == "④ 📁 結果履歴":
    from pages.page4_record_result import show_page
    show_page()
elif menu == "⑤ 🗓️ 開催結果":
    from pages.page5_today_schedule import show_page
    show_page()
elif menu == "⑥ ⚙️ 設定":
    from pages.page6_settings import show_page
    show_page()
elif menu == "⑦ 🏟️ 場別予想":
    from pages.page7_per_boatplace_prediction import show_page
    show_page()
elif menu == "⑧ 📌 総合評価":
    from pages.page8_summary_today import show_page
    show_page()
elif menu == "⑨ 💡 特別分析":
    from pages.page9_reflection import show_page
    show_page()

# ===== 👤 制作者表記 =====
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-size: 14px;'>制作：小島崇彦</div>", unsafe_allow_html=True)
