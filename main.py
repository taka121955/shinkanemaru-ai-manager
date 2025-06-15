import streamlit as st
from datetime import datetime

# ページ設定
st.set_page_config(page_title="AI資金マネージャー", layout="centered")

# 背景色（淡い黄色）
st.markdown("""
    <style>
    .stApp {
        background-color: #fff9db;
    }
    </style>
""", unsafe_allow_html=True)

# 日本時間の現在時刻を表示
now = datetime.now()
japan_time = now.strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"⏰ **現在時刻：** `{japan_time}`")

# 目標・準備・積立金をセッションから取得（なければ0）
target_amount = st.session_state.get("target_amount", 0)
reserve_amount = st.session_state.get("reserve_amount", 0)
accumulated_amount = st.session_state.get("accumulated_amount", 0)

# メニュー表示（2列構成）
st.markdown("### 🗂️ メニュー（表示専用）")

col1, col2 = st.columns(2)
with col1:
    st.button("①AI予想", use_container_width=True)
    st.button("③統計データ", use_container_width=True)
    st.button("⑤競艇結果", use_container_width=True)
with col2:
    st.button("②勝敗入力", use_container_width=True)
    st.button("④結果履歴", use_container_width=True)
    st.button("⑥資金設定", use_container_width=True)

# 資金状況の表示
st.markdown("---")
st.markdown("### 💰 現在の資金状況")
st.markdown(f"🎯 **目標金額：** <span style='color:blue;'>{target_amount:,}円</span>", unsafe_allow_html=True)
st.markdown(f"💼 **準備金額：** <span style='color:green;'>{reserve_amount:,}円</span>", unsafe_allow_html=True)
st.markdown(f"📦 **積立金額：** <span style='color:orange;'>{accumulated_amount:,}円</span>", unsafe_allow_html=True)

# 制作者表示は非表示（削除済み）
