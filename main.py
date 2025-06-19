import streamlit as st
from datetime import datetime
import pytz

# ✅ 追加：⑥設定ページのインポート
from pages.page6_settings import show_page as show_page6

# ページ設定
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ===== 🕒 日本時間の現在時刻を中央表示 =====
japan_time = datetime.now(pytz.timezone("Asia/Tokyo"))
formatted_time = japan_time.strftime("%Y年%m月%d日（%a） %H:%M")
st.markdown(f"<h2 style='text-align: center; font-size: 24px;'>{formatted_time}</h2>", unsafe_allow_html=True)
st.markdown("---")

# ===== 📊 ステータス（中央表示） =====
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

# ===== 📁 メニュー一覧（同サイズボタン） =====
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
        with cols[j]:
            st.markdown(
                f"<div style='{button_style}'>{menu_list[i+j]}</div>",
                unsafe_allow_html=True
            )

# ✅ 追加：URLパラメータによるページ選択処理（簡易）
query_params = st.experimental_get_query_params()
selected_menu = query_params.get("page", [None])[0]

if selected_menu == "6":
    show_page6()

# ===== 👤 制作者表記 =====
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-size: 14px;'>制作：小島崇彦</div>", unsafe_allow_html=True)
