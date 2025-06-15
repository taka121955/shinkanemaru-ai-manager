# main.py

import streamlit as st
from datetime import datetime

# ✅ ページ設定：サイドバー非表示・横長・高速化
st.set_page_config(
    page_title="新金丸法 × AI資金マネージャー",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ✅ 現在時刻（JST）
jst = datetime.utcnow().astimezone()
st.markdown(f"<h3 style='text-align: center;'>🕒 現在時刻（日本時間）：{jst.strftime('%Y/%m/%d %H:%M:%S')}</h3>", unsafe_allow_html=True)

# ✅ 資金表示
st.markdown("""
<div style='text-align: center; font-size: 18px;'>
🎯 目標金額：10000円　💰 初期資金：5000円　📊 累積資金：7200円
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ✅ ページナビゲーションボタン（2段 × 3列、軽量化済み）
st.markdown("""
<style>
.button-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 12px;
    margin-bottom: 30px;
}
.button-container a {
    display: inline-block;
    padding: 14px 28px;
    font-size: 16px;
    font-weight: bold;
    color: #003366;
    background-color: #e6f0ff;
    border: 2px solid #4a90e2;
    border-radius: 8px;
    text-decoration: none;
    transition: all 0.2s;
}
.button-container a:hover {
    background-color: #d0e4ff;
    transform: scale(1.05);
}
</style>

<div class="button-container">
    <a href="/?page=1_📈_AI予想">① AI予想</a>
    <a href="/?page=2_✍️_勝敗入力">② 勝敗入力</a>
    <a href="/?page=3_📊_統計データ">③ 統計データ</a>
    <a href="/?page=4_📋_結果履歴">④ 結果履歴</a>
    <a href="/?page=5_🚤_競艇結果">⑤ 競艇結果</a>
    <a href="/?page=6_⚙️_設定">⑥ 設定</a>
</div>
""", unsafe_allow_html=True)

# ✅ フッター
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
