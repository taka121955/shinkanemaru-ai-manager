import streamlit as st
from datetime import datetime
import pytz

# ページ設定
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ===== 🕒 日本時間の現在時刻を中央表示 =====
japan_time = datetime.now(pytz.timezone("Asia/Tokyo"))
formatted_time = japan_time.strftime("%Y年%m月%d日（%a） %H:%M")

st.markdown(f"<h2 style='text-align: center;'>{formatted_time}</h2>", unsafe_allow_html=True)
st.markdown("---")

# ===== 📊 ステータスをエクセル風に中央表示 =====
st.markdown("<h3 style='text-align: center;'>📊 今日のステータス</h3>", unsafe_allow_html=True)

status_table = """
<div style='display: flex; justify-content: center;'>
<table style='border-collapse: collapse; font-size: 18px;'>
  <tr><td>🎯 <b>的中率</b></td><td>85%</td></tr>
  <tr><td>📉 <b>勝敗</b></td><td>3勝2敗</td></tr>
  <tr><td>💰 <b>積立金</b></td><td>+4,800円</td></tr>
  <tr><td>🏆 <b>勝率</b></td><td>70%</td></tr>
  <tr><td>✅ <b>回収率</b></td><td>125%</td></tr>
  <tr><td>🎒 <b>軍資金</b></td><td>10,000円</td></tr>
</table>
</div>
"""
st.markdown(status_table, unsafe_allow_html=True)
st.markdown("---")

# ===== 📁 メニュー一覧（ボタン風デザインで3列表示） =====
st.markdown("<h3 style='text-align: center;'>📁 メニュー一覧</h3>", unsafe_allow_html=True)

menu_items = [
    "① AI予想 🧠", "② 勝敗入力 ✍️", "③ 統計データ 📊",
    "④ 結果履歴 📁", "⑤ 開催結果 🏁", "⑥ 設定 ⚙️",
    "⑦ 場別予想 🏟️", "⑧ 総合評価 📊", "⑨ 特別分析 💡"
]

menu_html = "<div style='display: flex; flex-wrap: wrap; justify-content: center;'>"

for item in menu_items:
    menu_html += f"""
    <div style='
        display: inline-block;
        background-color: #f1f3f6;
        border: 2px solid #ccc;
        border-radius: 10px;
        padding: 12px 18px;
        margin: 10px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        width: 180px;
    '>{item}</div>
    """

menu_html += "</div>"
st.markdown(menu_html, unsafe_allow_html=True)

# 制作者名
st.markdown("<div style='text-align: center; margin-top: 30px;'>制作：小島崇彦</div>", unsafe_allow_html=True)
