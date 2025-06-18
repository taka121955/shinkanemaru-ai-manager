import streamlit as st
from datetime import datetime
import pytz

# ページ設定
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ===== 🕒 日本時間の現在時刻を中央表示 =====
japan_time = datetime.now(pytz.timezone("Asia/Tokyo"))
formatted_time = japan_time.strftime("%Y年%m月%d日（%a） %H:%M")

st.markdown(f"<h1 style='text-align: center; font-size: 28px;'>{formatted_time}</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ===== 📊 今日のステータス 表示（中央 × Excel風）=====
st.markdown("### 📊 今日のステータス", unsafe_allow_html=True)

status_data = [
    ["🎯 的中率", "85%"],
    ["📈 勝敗", "3勝2敗"],
    ["💰 積立金", "+4,800円"],
    ["🏆 勝率", "70%"],
    ["✅ 回収率", "125%"],
    ["🎒 軍資金", "10,000円"]
]

status_html = "<div style='text-align:center;'>"
for label, value in status_data:
    status_html += f"<div style='font-size: 20px; margin: 4px;'><b>{label}：</b> {value}</div>"
status_html += "</div>"

st.markdown(status_html, unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ===== 📁 メニュー一覧（ボタン風3列×3行） =====
st.markdown("### 📁 メニュー一覧", unsafe_allow_html=True)

menu_labels = [
    "① AI予想 🧠", "② 勝敗入力 ✍️", "③ 統計データ 📊",
    "④ 結果履歴 📁", "⑤ 開催結果 🏁", "⑥ 設定 ⚙️",
    "⑦ 場別予想 🏟️", "⑧ 総合評価 📈", "⑨ 特別分析 💡"
]

def menu_button(label):
    return f"""
    <div style='
        display: inline-block;
        background-color: #f1f3f6;
        border: 2px solid #ccc;
        border-radius: 10px;
        padding: 12px 18px;
        margin: 8px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        width: 160px;
    '>{label}</div>
    """

menu_html = "<div style='text-align: center;'>"
for i in range(0, len(menu_labels), 3):
    menu_html += "<div style='margin-bottom: 10px;'>"
    for label in menu_labels[i:i+3]:
        menu_html += menu_button(label)
    menu_html += "</div>"
menu_html += "</div>"

st.markdown(menu_html, unsafe_allow_html=True)

# ===== 制作者名 =====
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-size: 14px;'>制作：小島崇彦</div>", unsafe_allow_html=True)
