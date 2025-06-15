import streamlit as st
from datetime import datetime

# ページ設定
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# セッション初期化
st.session_state.setdefault("目標金額", 50000)
st.session_state.setdefault("準備金額", 10000)
st.session_state.setdefault("積立金額", 3000)

# 🌟 CSSスタイル（背景＋フォント整形）
st.markdown("""
    <style>
        body {
            background-color: #fffdd0;
        }
        .big-title {
            font-size: 32px;
            font-weight: bold;
            text-align: center;
            padding-bottom: 10px;
        }
        .clock {
            font-size: 20px;
            text-align: center;
        }
        .menu-title {
            font-size: 24px;
            font-weight: bold;
            padding-top: 20px;
        }
        .menu-button {
            display: inline-block;
            width: 120px;
            padding: 8px;
            margin: 5px;
            font-size: 16px;
            text-align: center;
            border-radius: 8px;
            background-color: #f0f0f0;
            border: 1px solid #ccc;
        }
        .fund-display {
            font-size: 18px;
            padding-left: 10px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# 🕒 現在時刻
now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
st.markdown(f"<div class='clock'>⏰ 現在時刻： {now}</div>", unsafe_allow_html=True)

# 🧠 タイトル
st.markdown("<div class='big-title'>🧠 新金丸法 × AI資金マネージャー</div>", unsafe_allow_html=True)

# 📋 メニュー表示
st.markdown("<div class='menu-title'>📄 メニュー（表示専用）</div>", unsafe_allow_html=True)

menu_items = [
    "① AI予想", "② 勝敗入力", "③ 統計データ",
    "④ 結果履歴", "⑤ 競艇結果", "⑥ 資金設定"
]

menu_cols = st.columns(3)
for i, label in enumerate(menu_items):
    with menu_cols[i % 3]:
        st.markdown(f"<div class='menu-button'>{label}</div>", unsafe_allow_html=True)

st.markdown("---")

# 💰 現在の資金状況
st.markdown("<div class='menu-title'>💰 現在の資金状況</div>", unsafe_allow_html=True)
st.markdown(f"<div class='fund-display'>🎯 目標金額：<span style='color:blue'>{st.session_state['目標金額']:,}円</span></div>", unsafe_allow_html=True)
st.markdown(f"<div class='fund-display'>💼 準備金額：<span style='color:green'>{st.session_state['準備金額']:,}円</span></div>", unsafe_allow_html=True)
st.markdown(f"<div class='fund-display'>📦 積立金額：<span style='color:orange'>{st.session_state['積立金額']:,}円</span></div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align:center;'>制作：小島崇彦</p>", unsafe_allow_html=True)
