import streamlit as st
from datetime import datetime

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# 初期値の設定（セッション）
st.session_state.setdefault("目標金額", 0)
st.session_state.setdefault("準備金額", 0)
st.session_state.setdefault("積立金額", 0)

# スタイル調整（見やすくする）
st.markdown(
    """
    <style>
    .big-font {
        font-size:24px !important;
        font-weight:bold;
    }
    .button-row button {
        width: 100%;
        margin: 2px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 現在時刻（中央表示）
st.markdown(f"<div style='text-align:center;' class='big-font'>⏰ 現在時刻：{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}</div>", unsafe_allow_html=True)

# タイトル
st.markdown("<h2 style='text-align:center;'>🧠 新金丸法 × AI資金マネージャー</h2>", unsafe_allow_html=True)
st.markdown("---")

# メニューボタン（見た目のみ／6ボタン水平整列）
st.markdown("### 📄 メニュー（表示専用）")
cols1 = st.columns(3)
cols2 = st.columns(3)
menu_labels = ["① AI予想", "② 勝敗入力", "③ 統計データ", "④ 結果履歴", "⑤ 競艇結果", "⑥ 資金設定"]

for i, col in enumerate(cols1 + cols2):
    with col:
        st.button(menu_labels[i], disabled=True)

st.markdown("---")

# 資金情報表示（強調表示）
st.markdown("### 💹 現在の資金情報")

st.markdown(f"""
- 🎯 <span class='big-font' style='color:blue;'>目標金額：{st.session_state['目標金額']:,}円</span><br>
- 💰 <span class='big-font' style='color:green;'>準備金額：{st.session_state['準備金額']:,}円</span><br>
- 📦 <span class='big-font' style='color:orange;'>積立金額：{st.session_state['積立金額']:,}円</span>
""", unsafe_allow_html=True)

st.markdown("---")

# フッター
st.markdown("##### 制作者：小島崇彦", unsafe_allow_html=True)
