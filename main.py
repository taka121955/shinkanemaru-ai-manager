import streamlit as st
from datetime import datetime

# ページ背景をライトイエローに変更
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #fffce6;
    }
    .menu-button {
        background-color: #f0f0f0;
        border-radius: 10px;
        padding: 8px 24px;
        margin: 6px;
        font-weight: bold;
        border: 1px solid #ccc;
        color: #333;
        display: inline-block;
    }
    .menu-section {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# タイトルと説明
st.markdown("## 👜 新金丸法 × AI資金マネージャー")
st.markdown("##### 以下のページを選択してください")

# メニューボタン（表示専用）
st.markdown("<div class='menu-section'>", unsafe_allow_html=True)
menu_labels = [
    "① AI予想", "② 勝敗入力", "③ 統計データ",
    "④ 結果履歴", "⑤ 競艇結果", "⑥ 資金設定"
]
for label in menu_labels:
    st.markdown(f"<div class='menu-button'>{label}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# スペース
st.markdown("---")

# 現在の資金状況
target_amount = 50000
reserve_amount = 10000
saving_amount = 3000

st.markdown("### 💰 現在の資金状況")
st.markdown(f"🎯 <b>目標金額：</b> <span style='color:blue;'>{target_amount:,}円</span>", unsafe_allow_html=True)
st.markdown(f"💼 <b>準備金額：</b> <span style='color:green;'>{reserve_amount:,}円</span>", unsafe_allow_html=True)
st.markdown(f"📦 <b>積立金額：</b> <span style='color:orange;'>{saving_amount:,}円</span>", unsafe_allow_html=True)

# 制作クレジット
st.markdown("---")
st.markdown("#### 制作：小島崇彦")
