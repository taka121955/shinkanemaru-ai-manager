import streamlit as st
from datetime import datetime

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ✅ 現在時刻表示
now = datetime.now()
st.markdown(f"### 🕐 現在時刻：{now.strftime('%Y/%m/%d %H:%M:%S')}")

# ✅ 2列×3行の表形式で整列
left_col1, right_col1 = st.columns(2)
with left_col1:
    st.markdown("### 🎯 目標金額\n　: 10000円")
with right_col1:
    st.markdown("### 🏆 勝率\n　: 70%")

left_col2, right_col2 = st.columns(2)
with left_col2:
    st.markdown("### 💰 準備資金\n　: 5000円")
with right_col2:
    st.markdown("### 🎯 的中率\n　: 65%")

left_col3, right_col3 = st.columns(2)
with left_col3:
    st.markdown("### 📊 積立資金\n　: 2300円")
with right_col3:
    st.markdown("### 💹 回収率\n　: 115%")

# ✅ メニュー
st.markdown("---")
selected_page = st.radio("📁 メニュー選択", ["① AI予想", "② 勝敗入力", "③ 統計データ", "④ 結果履歴", "⑤ 競艇結果"], horizontal=True)

# ✅ 制作者表記
st.markdown("---")
st.markdown("#### 制作者：小島崇彦")
