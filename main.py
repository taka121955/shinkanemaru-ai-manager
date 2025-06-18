import streamlit as st
from datetime import datetime
import pytz

# ページ設定
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ===== 🕒 日本時間の現在時刻を中央表示 =====
japan_time = datetime.now(pytz.timezone("Asia/Tokyo"))
formatted_time = japan_time.strftime("%Y年%m月%d日（%a） %H:%M")
st.markdown(f"<h1 style='text-align:center; font-size:28px;'>{formatted_time}</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ===== 📊 今日のステータス 表示（強調＋絵文字つき） =====
st.markdown("<h2 style='font-size:26px;'>📊 今日のステータス</h2>", unsafe_allow_html=True)

st.markdown("""
<div style='font-size:22px; line-height:1.8;'>
🎯 <b>的中率：</b> 85%　<br>
📈 <b>勝敗：</b> 3勝2敗　<br>
💰 <b>積立金：</b> +4,800円　<br>
🏆 <b>勝率：</b> 70%　<br>
📈 <b>回収率：</b> 125%　<br>
🎒 <b>軍資金：</b> 10,000円　
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ===== 📁 メニュー一覧（中央寄せ + 大きめ） =====
st.markdown("<h2 style='font-size:26px;'>📁 メニュー一覧</h2>", unsafe_allow_html=True)

menu_labels = [
    "① AI予想 🧠", "② 勝敗入力 ✍️", "③ 統計データ 📊",
    "④ 結果履歴 📁", "⑤ 開催結果 🏁", "⑥ 設定 ⚙️",
    "⑦ 場別予想 🏟️", "⑧ 総合評価 📊", "⑨ 特別分析 💡"
]

for i in range(0, 9, 3):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div style='text-align:center; font-size:22px;'>{menu_labels[i]}</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div style='text-align:center; font-size:22px;'>{menu_labels[i+1]}</div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div style='text-align:center; font-size:22px;'>{menu_labels[i+2]}</div>", unsafe_allow_html=True)

# フッター
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; color:gray;'>制作：小島崇彦</div>", unsafe_allow_html=True)
