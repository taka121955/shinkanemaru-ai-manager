import streamlit as st
from datetime import datetime

# ページ設定
st.set_page_config(page_title="資金マネージャー", layout="centered")

# 背景色
st.markdown("""
    <style>
    .stApp {
        background-color: #fff9db;
    }
    </style>
""", unsafe_allow_html=True)

# 日本時間表示（大きく）
japan_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"<h4 style='color:#333333;'>⏰ 現在時刻：<code style='font-size:18px;'>{japan_time}</code></h4>", unsafe_allow_html=True)

# メニュータイトル
st.markdown("### 🗂️ メニュー（表示専用）")

# 2列×3行のメニュー
col1, col2 = st.columns(2)
with col1:
    st.button("①AI予想", use_container_width=True)
    st.button("③統計データ", use_container_width=True)
    st.button("⑤競艇結果", use_container_width=True)
with col2:
    st.button("②勝敗入力", use_container_width=True)
    st.button("④結果履歴", use_container_width=True)
    st.button("⑥資金設定", use_container_width=True)

# ページ⑥のデータ（セッション連携）
target_amount = st.session_state.get("target_amount", 0)
reserve_amount = st.session_state.get("reserve_amount", 0)
accumulated_amount = st.session_state.get("accumulated_amount", 0)

# 資金状況表示
st.markdown("---")
st.markdown("### 💰 現在の資金状況")
st.markdown(f"🎯 **目標金額：** <span style='color:blue;'>{target_amount:,}円</span>", unsafe_allow_html=True)
st.markdown(f"💼 **準備金額：** <span style='color:green;'>{reserve_amount:,}円</span>", unsafe_allow_html=True)
st.markdown(f"📦 **積立金額：** <span style='color:orange;'>{accumulated_amount:,}円</span>", unsafe_allow_html=True)
