import streamlit as st
from datetime import datetime
import pytz

# ✅ 各ページ読み込み
from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_boat_results import show_page as show_page5
from pages.page6_settings import show_page as show_page6

# ===== 📌 ページ設定 =====
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ===== 🕒 現在時刻（日本時間） =====
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

# ===== 📁 メニュー一覧（見た目のみボタン風） =====
st.markdown("<h3 style='text-align: center;'>📁 メニュー一覧</h3>", unsafe_allow_html=True)

menu_list = [
    "① AI予想 🧠", "② 勝敗入力 ✍️", "③ 統計データ 📊",
    "④ 結果履歴 📁", "⑤ 開催結果 🏁", "⑥ 設定 ⚙️",
    "⑦ 場別予想 🏟️", "⑧ 総合評価 📊", "⑨ 特別分析 💡"
]

button_style = """
display: inline-block;
background-color: #f1f3f6;
border: 2px solid #ccc;
border-radius: 10px;
padding: 18px 0;
margin: 10px;
font-size: 18px;
font-weight: bold;
text-align: center;
width: 180px;
height: 60px;
"""

for i in range(0, 9, 3):
    cols = st.columns(3)
    for j in range(3):
        idx = i + j
        with cols[j]:
            st.markdown(
                f"<div style='{button_style}'>{menu_list[idx]}</div>",
                unsafe_allow_html=True
            )

st.markdown("---")

# ===== ✅ サイドバーでページ切替 =====
page = st.sidebar.radio("📑 ページ選択", [
    "① AI予想", "② 勝敗入力", "③ 統計データ",
    "④ 結果履歴", "⑤ 開催結果", "⑥ 設定"
])

if page == "① AI予想":
    show_page1()
elif page == "② 勝敗入力":
    show_page2()
elif page == "③ 統計データ":
    show_page3()
elif page == "④ 結果履歴":
    show_page4()
elif page == "⑤ 開催結果":
    show_page5()
elif page == "⑥ 設定":
    show_page6()

# ===== 👤 制作者クレジット =====
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-size: 14px;'>制作：小島崇彦</div>", unsafe_allow_html=True)
