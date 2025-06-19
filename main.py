import streamlit as st
from datetime import datetime
import pytz

# サイドバーでだけページ切替（英語出ない）
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide")

# ===== 日本時間の表示 =====
japan_time = datetime.now(pytz.timezone("Asia/Tokyo"))
formatted_time = japan_time.strftime("%Y年%m月%d日（%a） %H:%M")
st.markdown(f"<h2 style='text-align: center;'>{formatted_time}</h2>", unsafe_allow_html=True)
st.markdown("---")

# ===== 🎨 カスタムサイドバー =====
st.sidebar.markdown("## 📋 ページ選択")
menu = st.sidebar.radio("操作メニュー", [
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

# ===== ✅ ページ分岐・表示制御 =====
if menu == "🏠 メインページ":
    st.markdown("### 📊 今日のステータス")
    st.write("ここにステータスを表示")
    st.info("左のメニューで操作できます。")

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

# ===== 制作者表示 =====
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>制作：小島崇彦</div>", unsafe_allow_html=True)
