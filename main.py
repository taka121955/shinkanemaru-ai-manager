import streamlit as st
from datetime import datetime

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# 🕒 現在時刻
now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
st.markdown(f"### 🕐 現在時刻：{now}")

# 💡 2列レイアウト
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎯 目標金額\n　: 10000円")
    st.markdown("### 💰 準備資金\n　: 5000円")
    st.markdown("### 📊 積立資金\n　: 2300円")

with col2:
    st.markdown("### 🏆 勝率\n　: 70%")
    st.markdown("### 🎯 的中率\n　: 65%")
    st.markdown("### 💹 回収率\n　: 115%")

# メニュー
st.markdown("---")
st.radio("📁 メニュー選択", ["① AI予想", "② 勝敗入力", "③ 統計データ", "④ 結果履歴", "⑤ 競艇結果"], horizontal=True)

# 下部表記
st.markdown("---")
st.markdown("#### 制作者：小島崇彦")
