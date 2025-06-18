import streamlit as st
from datetime import datetime
import pytz

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide")

# ===== 🕒 日本時間の現在時刻を中央表示 =====
japan_time = datetime.now(pytz.timezone("Asia/Tokyo"))
formatted_time = japan_time.strftime("%Y年%m月%d日（%a） %H:%M")

st.markdown(f"<h2 style='text-align: center; font-size:30px;'>{formatted_time}</h2>", unsafe_allow_html=True)
st.markdown("---")

# ===== 📊 今日のステータス（表風レイアウト・中央寄せ） =====
st.markdown("<h3 style='text-align: center;'>📊 今日のステータス</h3>", unsafe_allow_html=True)

status_data = [
    ["🎯 的中率", "85%"],
    ["📈 勝敗", "3勝2敗"],
    ["💰 積立金", "+4,800円"],
    ["🏆 勝率", "70%"],
    ["✅ 回収率", "125%"],
    ["🎒 軍資金", "10,000円"]
]

status_html = """
<table style='margin-left:auto; margin-right:auto; font-size:20px;'>
"""
for row in status_data:
    status_html += f"<tr><td style='padding: 10px 30px;'>{row[0]}</td><td>{row[1]}</td></tr>"
status_html += "</table>"

st.markdown(status_html, unsafe_allow_html=True)
st.markdown("---")

# ===== 📁 メニュー一覧（ボタン風装飾で中央表示） =====
st.markdown("<h3 style='text-align: center;'>📁 メニュー一覧</h3>", unsafe_allow_html=True)

menu_labels = [
    "① AI予想 🧠", "② 勝敗入力 ✍️", "③ 統計データ 📊",
    "④ 結果履歴 📁", "⑤ 開催結果 🏁", "⑥ 設定 ⚙️",
    "⑦ 場別予想 🏟️", "⑧ 総合評価 📊", "⑨ 特別分析 💡"
]

menu_html = "<div style='display: flex; flex-wrap: wrap; justify-content: center;'>"
for label in menu_labels:
    menu_html += f"""
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
menu_html += "</div>"

st.markdown(menu_html, unsafe_allow_html=True)

# ===== 👤 フッター（制作者名） =====
st.markdown("<div style='text-align: center; margin-top: 40px;'>制作：小島崇彦</div>", unsafe_allow_html=True)
