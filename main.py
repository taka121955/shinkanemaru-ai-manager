import streamlit as st
from datetime import datetime
import pytz

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide")

# ===== 🕒 日本時間の現在時刻 =====
japan_time = datetime.now(pytz.timezone("Asia/Tokyo"))
formatted_time = japan_time.strftime("%Y年%m月%d日（%a） %H:%M")
st.markdown(f"<h2 style='text-align: center;'>{formatted_time}</h2>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ===== 📊 ステータス中央表示 =====
st.markdown("""
<div style='text-align: center; font-size: 22px;'>
    <h2>📊 今日のステータス</h2>
    <p>🎯 <b>的中率：</b> 85%</p>
    <p>📈 <b>勝敗：</b> 3勝2敗</p>
    <p>💰 <b>積立金：</b> +4,800円</p>
    <p>🏆 <b>勝率：</b> 70%</p>
    <p>💹 <b>回収率：</b> 125%</p>
    <p>🎒 <b>軍資金：</b> 10,000円</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ===== 📁 メニュー一覧：ボタン風レイアウト =====
st.markdown("<h2 style='text-align: center;'>📁 メニュー一覧</h2>", unsafe_allow_html=True)

menu_labels = [
    "① AI予想 🧠", "② 勝敗入力 ✍️", "③ 統計データ 📊",
    "④ 結果履歴 📁", "⑤ 開催結果 🏁", "⑥ 設定 ⚙️",
    "⑦ 場別予想 🏟️", "⑧ 総合評価 📊", "⑨ 特別分析 💡"
]

def button_html(label):
    return f"""
    <div style='
        display: inline-block;
        background-color: #f1f3f6;
        border: 2px solid #ccc;
        border-radius: 10px;
        padding: 12px 18px;
        margin: 6px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        width: 180px;
    '>{label}</div>
    """

menu_html = "".join([button_html(label) for label in menu_labels])
st.markdown(f"<div style='text-align: center'>{menu_html}</div>", unsafe_allow_html=True)

# 制作者表記
st.markdown("<br><div style='text-align: center; font-size: 14px;'>制作：小島崇彦</div>", unsafe_allow_html=True)
