import streamlit as st
from datetime import datetime

# ページ設定
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# セッション初期化（連動用）
st.session_state.setdefault("目標金額", 50000)
st.session_state.setdefault("準備金額", 10000)
st.session_state.setdefault("積立金額", 3000)

# カスタムCSSで背景＆見た目調整
st.markdown("""
    <style>
        body {
            background-color: #fff9dc;
        }
        .title {
            font-size: 30px;
            text-align: center;
            font-weight: bold;
        }
        .menu-box {
            text-align: center;
            margin-top: 20px;
            margin-bottom: 30px;
        }
        .menu-button {
            display: inline-block;
            padding: 10px 20px;
            margin: 6px;
            border-radius: 12px;
            background-color: #f0f0f0;
            border: 1px solid #999;
            font-size: 18px;
            font-weight: bold;
        }
        .fund-status {
            font-size: 20px;
            margin-top: 20px;
            line-height: 1.8;
        }
    </style>
""", unsafe_allow_html=True)

# 🕒 現在時刻表示
now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
st.markdown(f"<div style='text-align:center; font-size:20px;'>⏰ 現在時刻：{now}</div>", unsafe_allow_html=True)

# タイトル
st.markdown("<div class='title'>🧠 新金丸法 × AI資金マネージャー</div>", unsafe_allow_html=True)

# メニュー（表示専用）
st.markdown("<div class='menu-box'><p style='font-size:22px;'>📋 メニュー（表示専用）</p>", unsafe_allow_html=True)

# メニューボタン風表示（3列 × 2行）
menu_items = ["①AI予想", "②勝敗入力", "③統計データ", "④結果履歴", "⑤競艇結果", "⑥資金設定"]
for i in range(0, len(menu_items), 3):
    row = menu_items[i:i+3]
    st.markdown(
        "<div>" + "".join([f"<span class='menu-button'>{item}</span>" for item in row]) + "</div>",
        unsafe_allow_html=True
    )
st.markdown("</div>", unsafe_allow_html=True)

# 💰 資金状況
目標 = f"{st.session_state['目標金額']:,}円"
準備 = f"{st.session_state['準備金額']:,}円"
積立 = f"{st.session_state['積立金額']:,}円"

st.markdown(f"""
<div class='fund-status'>
💰 <b>現在の資金状況</b><br>
🎯 目標金額：<span style='color:blue'>{目標}</span><br>
💼 準備金額：<span style='color:green'>{準備}</span><br>
📦 積立金額：<span style='color:orange'>{積立}</span>
</div>
""", unsafe_allow_html=True)

# 制作表記
st.markdown("<hr><p style='text-align:center;'>制作：小島崇彦</p>", unsafe_allow_html=True)
