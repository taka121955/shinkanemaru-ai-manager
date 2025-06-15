import streamlit as st
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ページ背景色（ライトイエロー）
page_bg_color = """
<style>
body {
    background-color: #fff8dc;
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# 現在時刻
st.markdown(f"⏰ **現在時刻： `{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}`**")

# タイトル
st.markdown("<h1 style='text-align: center;'>🧠 新金丸法 × AI資金マネージャー</h1>", unsafe_allow_html=True)

# メニュー（6ページ）を横並びに整列
st.markdown("### 🗂 メニュー（表示専用）")
col1, col2 = st.columns(2)
with col1:
    st.button("①AI予想", key="btn1", help="AI予想ページ（非リンク）", disabled=True)
    st.button("③統計データ", key="btn3", help="統計ページ（非リンク）", disabled=True)
    st.button("⑤競艇結果", key="btn5", help="競艇結果（非リンク）", disabled=True)
with col2:
    st.button("②勝敗入力", key="btn2", help="勝敗入力ページ（非リンク）", disabled=True)
    st.button("④結果履歴", key="btn4", help="結果履歴ページ（非リンク）", disabled=True)
    st.button("⑥資金設定", key="btn6", help="資金設定ページ（非リンク）", disabled=True)

# 現在の資金状況読み込み
try:
    df = pd.read_csv("settings.csv")
    goal = int(df.loc[0, "目標金額"])
    reserve = int(df.loc[0, "準備金額"])
    savings = int(df.loc[0, "積立金額"])
except Exception:
    goal = reserve = savings = 0

# 現在の資金状況表示
st.markdown("---")
st.markdown("### 💰 現在の資金状況")
st.markdown(f"🎯 **目標金額：** <span style='color:blue;'>{goal:,}円</span>", unsafe_allow_html=True)
st.markdown(f"💼 **準備金額：** <span style='color:green;'>{reserve:,}円</span>", unsafe_allow_html=True)
st.markdown(f"📦 **積立金額：** <span style='color:orange;'>{savings:,}円</span>", unsafe_allow_html=True)

# 制作者名
st.markdown("---")
st.markdown("### 制作：小島崇彦")
