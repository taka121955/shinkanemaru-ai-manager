import streamlit as st
from datetime import datetime

# ページ設定
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# 現在時刻（日本時間で表示）
now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"🕒 現在時刻：**{now}**")

# CSSスタイルで2列6行の表示レイアウト
st.markdown("""
<style>
.grid-container {
  display: grid;
  grid-template-columns: 160px 160px;
  grid-row-gap: 10px;
  font-size: 20px;
  margin-top: 20px;
}
.grid-container div {
  padding: 5px 10px;
}
</style>

<div class="grid-container">
  <div>🎯 目標金額</div><div>：10000円</div>
  <div>💰 準備資金</div><div>：5000円</div>
  <div>📊 積立資金</div><div>：2300円</div>
  <div>🏆 勝率</div><div>：70%</div>
  <div>🎯 的中率</div><div>：65%</div>
  <div>💹 回収率</div><div>：115%</div>
</div>
""", unsafe_allow_html=True)

# 下部に制作者名
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div style="text-align: right;">制作者：小島崇彦</div>', unsafe_allow_html=True)
