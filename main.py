import streamlit as st
from datetime import datetime
import pytz

# ページ設定
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ===== 🕒 日本時間の現在時刻を中央表示 =====
japan_time = datetime.now(pytz.timezone("Asia/Tokyo"))
formatted_time = japan_time.strftime("%Y年%m月%d日（%a） %H:%M")
st.markdown(f"<h2 style='text-align: center; font-size: 24px;'>{formatted_time}</h2>", unsafe_allow_html=True)
st.markdown("---")

# ===== 📊 ステータス表示 =====
st.markdown("### 📊 今日のステータス", unsafe_allow_html=True)
status_html = """
<div style='display: flex; justify-content: center;'>
  <table style='font-size:18px; border-spacing: 16px;'>
    <tr><td>🎯 的中率：</td><td>85%</td></tr>
    <tr><td>📉 勝敗：</td><td>3勝2敗</td></tr>
    <tr><td>💰 積立金：</td><td>+4,800円</td></tr>
    <tr><td>🏆 勝率：</td><td>70%</td></tr>
    <tr><td>✅ 回収率：</td><td>125%</td></tr>
    <tr><td>🎒 軍資金：</td><td>10,000円</td></tr>
  </table>
</div>
"""
st.markdown(status_html, unsafe_allow_html=True)
st.markdown("---")

# ===== 🧭 メニュー一覧はあくまで main.py 内だけに見せる表現（他ページへは遷移しない） =====
st.markdown("### 📁 メニュー一覧", unsafe_allow_html=True)

menu_list = [
    "① 🔮 AI予想", "② ✍️ 勝敗入力", "③ 📊 統計データ",
    "④ 📁 結果履歴", "⑤ 🗓️ 開催結果", "⑥ ⚙️ 設定",
    "⑦ 🏟️ 場別予想", "⑧ 📌 総合評価", "⑨ 💡 特別分析"
]

button_style = """
display: inline-block;
background-color: #f8f9fa;
border: 1px solid #ccc;
border-radius: 10px;
padding: 12px 0;
margin: 6px;
font-size: 16px;
font-weight: bold;
text-align: center;
width: 180px;
box-shadow: 1px 1px 2px rgba(0,0,0,0.1);
"""

for i in range(0, 9, 3):
    cols = st.columns(3)
    for j in range(3):
        idx = i + j
        with cols[j]:
            st.markdown(f"<div style='{button_style}'>{menu_list[idx]}</div>", unsafe_allow_html=True)

# ===== 👤 制作者表記 =====
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-size: 14px;'>制作：小島崇彦</div>", unsafe_allow_html=True)
