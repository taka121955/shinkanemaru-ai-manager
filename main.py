import streamlit as st
from datetime import datetime

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide", initial_sidebar_state="collapsed")

# 現在時刻
jst = datetime.utcnow().astimezone()
st.markdown(f"<h2 style='text-align: center;'>🕒 現在時刻：{jst.strftime('%Y/%m/%d %H:%M:%S')}</h2>", unsafe_allow_html=True)

# タイトルと案内
st.markdown("""
<div style='text-align: center; font-size: 24px; font-weight: bold;'>💼 新金丸法 × AI資金マネージャー</div>
<div style='text-align: center; font-size: 16px;'>以下のページを選択してください</div>
""", unsafe_allow_html=True)

# ボタン形式のナビゲーション
st.markdown("""
<style>
.button-grid {
    display: grid;
    grid-template-columns: repeat(2, 180px);
    gap: 16px;
    justify-content: center;
    margin: 30px 0;
}
.button-grid a {
    display: inline-block;
    text-align: center;
    padding: 14px;
    font-size: 18px;
    font-weight: bold;
    color: #003366;
    background-color: #e6f0ff;
    border: 2px solid #4a90e2;
    border-radius: 8px;
    text-decoration: none;
    transition: all 0.2s;
}
.button-grid a:hover {
    background-color: #d0e4ff;
    transform: scale(1.05);
}
</style>

<div class="button-grid">
    <a href="/?page=1_📈_AI予想">① AI予想</a>
    <a href="/?page=2_✍️_勝敗入力">② 勝敗入力</a>
</div>
""", unsafe_allow_html=True)

# フッター
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
