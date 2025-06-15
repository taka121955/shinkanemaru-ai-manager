import streamlit as st
from datetime import datetime

# ページ設定
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ページ全体の背景色（HTMLで黄色）
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fff9db;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 時刻表示
now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"⏰ <span style='font-size:20px;'>現在時刻：{now}</span>", unsafe_allow_html=True)

# タイトル
st.markdown("## 🧠 <strong>新金丸法 × AI資金マネージャー</strong>", unsafe_allow_html=True)
st.markdown("#### 🗂️ メニュー（表示専用）")

# メニュー：表示用ボタン風（横並び × 2列）
cols1 = st.columns(3)
cols1[0].markdown("#### <button style='width:100%;'>①AI予想</button>", unsafe_allow_html=True)
cols1[1].markdown("#### <button style='width:100%;'>②勝敗入力</button>", unsafe_allow_html=True)
cols1[2].markdown("#### <button style='width:100%;'>③統計データ</button>", unsafe_allow_html=True)

cols2 = st.columns(3)
cols2[0].markdown("#### <button style='width:100%;'>④結果履歴</button>", unsafe_allow_html=True)
cols2[1].markdown("#### <button style='width:100%;'>⑤競艇結果</button>", unsafe_allow_html=True)
cols2[2].markdown("#### <button style='width:100%;'>⑥資金設定</button>", unsafe_allow_html=True)

# 現在の資金状況（ページ⑥から取得されたと仮定）
target = 50000
reserve = 10000
stack = 3000

st.markdown("---")
st.markdown("### 💰 <strong>現在の資金状況</strong>", unsafe_allow_html=True)

st.markdown(f"🎯 <strong>目標金額：</strong> <span style='color:blue;'>{target:,}円</span>", unsafe_allow_html=True)
st.markdown(f"💼 <strong>準備金額：</strong> <span style='color:green;'>{reserve:,}円</span>", unsafe_allow_html=True)
st.markdown(f"📦 <strong>積立金額：</strong> <span style='color:orange;'>{stack:,}円</span>", unsafe_allow_html=True)

# 制作者名
st.markdown("---")
st.markdown("#### 制作：小島崇彦")
