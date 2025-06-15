import streamlit as st
from datetime import datetime

# ページ設定
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# セッション変数の初期化
st.session_state.setdefault("目標金額", 50000)
st.session_state.setdefault("準備金額", 10000)
st.session_state.setdefault("積立金額", 3000)

# 背景色とスタイルの設定
st.markdown(
    """
    <style>
    body {
        background-color: #fff8dc;
    }
    .big-title {
        font-size: 28px;
        font-weight: bold;
        text-align: center;
    }
    .sub-title {
        font-size: 20px;
        text-align: center;
    }
    .menu-btn {
        width: 100%;
        font-size: 16px;
        margin: 4px 0;
    }
    .funds {
        font-size: 18px;
        font-weight: bold;
        padding-left: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 現在時刻の表示
st.markdown(f"<div class='sub-title'>⏰ 現在時刻：{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}</div>", unsafe_allow_html=True)

# タイトル
st.markdown("<div class='big-title'>🧠 新金丸法 × AI資金マネージャー</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# メニュー表示（ボタン風）
st.markdown("#### 📋 メニュー（表示専用）")
menu_labels = [
    "① AI予想", "② 勝敗入力", "③ 統計データ",
    "④ 結果履歴", "⑤ 競艇結果", "⑥ 資金設定"
]
cols = st.columns(2)
for i, label in enumerate(menu_labels):
    with cols[i % 2]:
        st.button(label, disabled=True)

st.markdown("---")

# 資金表示（見やすくカラー強調）
st.markdown("#### 💰 現在の資金状況")
st.markdown(f"<div class='funds'>🎯 目標金額：<span style='color:blue;'>{st.session_state['目標金額']:,}円</span></div>", unsafe_allow_html=True)
st.markdown(f"<div class='funds'>💼 準備金額：<span style='color:green;'>{st.session_state['準備金額']:,}円</span></div>", unsafe_allow_html=True)
st.markdown(f"<div class='funds'>📦 積立金額：<span style='color:orange;'>{st.session_state['積立金額']:,}円</span></div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align:center;'>制作者：小島崇彦</p>", unsafe_allow_html=True)
