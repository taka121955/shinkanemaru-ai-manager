import streamlit as st
from datetime import datetime

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ✅ 現在時刻
now = datetime.now()
st.markdown(f"### 🕐 現在時刻：{now.strftime('%Y/%m/%d %H:%M:%S')}")

# ✅ 一列表示（縦並びで左：資金系 → 右：勝率系の順）
st.markdown("### 🎯 目標金額　　　　: 10000円")
st.markdown("### 🏆 勝率　　　　　　: 70%")
st.markdown("### 💰 準備資金　　　　: 5000円")
st.markdown("### 🎯 的中率　　　　　: 65%")
st.markdown("### 📊 積立資金　　　　: 2300円")
st.markdown("### 💹 回収率　　　　　: 115%")

# ✅ メニュー（ボタン風）
st.markdown("---")
selected_page = st.radio("📁 メニュー選択", ["① AI予想", "② 勝敗入力", "③ 統計データ", "④ 結果履歴", "⑤ 競艇結果"], horizontal=True)

# ✅ 制作者
st.markdown("---")
st.markdown("#### 制作者：小島崇彦")
