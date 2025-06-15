# main.py

import streamlit as st
from datetime import datetime

# ✅ ページ設定（サイドバー完全非表示）
st.set_page_config(
    page_title="新金丸法 × AI資金マネージャー",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ✅ サイドバー非表示用CSS（強制的に隠す）
st.markdown("""
<style>
/* サイドバーを完全に非表示 */
.css-1lcbmhc.e1fqkh3o3, .css-164nlkn.e1fqkh3o3 {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# ✅ 現在時刻（日本時間）
jst = datetime.utcnow().astimezone()
st.markdown(f"<h3 style='text-align: center;'>🕒 現在時刻（日本時間）：{jst.strftime('%Y/%m/%d %H:%M:%S')}</h3>", unsafe_allow_html=True)

# ✅ 資金情報
st.markdown("""
<div style='text-align: center; font-size: 18px;'>
🎯 目標金額：10000円　💰 初期資金：5000円　📊 累積資金：7200円
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ✅ 美しいボタンナビゲーション（2段 × 3列）
st.markdown("""
<style>
.button-grid {
    display: grid;
    grid-template-columns: repeat(3, 180px);
    gap: 18px;
    justify-content: center;
    margin-top: 30px;
    margin-bottom: 30px;
}
.button-grid a {
    display: inline-block;
    text-align: center;
    padding: 18px 0;
    font-size: 17px;
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
    <a href="/?page=3_📊_統計データ">③ 統計データ</a>
    <a href="/?page=4_📋_結果履歴">④ 結果履歴</a>
    <a href="/?page=5_🚤_競艇結果">⑤ 競艇結果</a>
    <a href="/?page=6_⚙️_設定">⑥ 設定</a>
</div>
""", unsafe_allow_html=True)

# ✅ フッター
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
