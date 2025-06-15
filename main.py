import streamlit as st
from datetime import datetime

# ✅ サイドバー完全無効（レイアウト指定）
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide", initial_sidebar_state="collapsed")

# --- 現在時刻（中央表示） ---
jst = datetime.utcnow().astimezone()
st.markdown(f"<h3 style='text-align: center;'>🕒 現在時刻（日本時間）：{jst.strftime('%Y/%m/%d %H:%M:%S')}</h3>", unsafe_allow_html=True)

# --- タイトルと案内 ---
st.markdown("""
<div style='text-align: center; font-size: 22px; font-weight: bold;'>💼 新金丸法 × AI資金マネージャー</div>
<div style='text-align: center; font-size: 16px; margin-bottom: 20px;'>
　以下のボタンから各機能ページに移動できます。
</div>
""", unsafe_allow_html=True)

# --- ページ移動ボタン（横並び2列×3段） ---
st.markdown("""
<style>
.button-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 16px;
    margin-bottom: 30px;
}
.button-grid a {
    display: inline-block;
    width: 160px;
    height: 60px;
    font-size: 18px;
    font-weight: bold;
    text-align: center;
    line-height: 60px;
    text-decoration: none;
    background-color: #e6f0ff;
    color: #003366;
    border: 2px solid #4a90e2;
    border-radius: 8px;
    transition: 0.2s;
}
.button-grid a:hover {
    background-color: #d0e4ff;
    transform: scale(1.05);
}
</style>

<div class="button-grid">
    <a href="/?page=1_📈_AI予想">①AI予想</a>
    <a href="/?page=2_✍️_勝敗入力">②勝敗入力</a>
    <a href="/?page=3_📊_統計データ">③統計データ</a>
    <a href="/?page=4_📋_結果履歴">④結果履歴</a>
    <a href="/?page=5_🚤_競艇結果">⑤競艇結果</a>
    <a href="/?page=6_⚙️_設定">⑥設定</a>
</div>
""", unsafe_allow_html=True)

# --- フッター ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
