import streamlit as st
from datetime import datetime

st.set_page_config(page_title="① AI予想", layout="wide", initial_sidebar_state="collapsed")

# 現在時刻
jst = datetime.utcnow().astimezone()
st.markdown(f"<h3 style='text-align: center;'>🕒 現在時刻：{jst.strftime('%Y/%m/%d %H:%M:%S')}</h3>", unsafe_allow_html=True)

# タイトル
st.markdown("<h2 style='text-align: center;'>📈 AI予想</h2>", unsafe_allow_html=True)

# ボタンナビ（ページ遷移）
st.markdown("""
<style>
.nav-grid {
    display: grid;
    grid-template-columns: repeat(3, 160px);
    gap: 12px;
    justify-content: center;
    margin-bottom: 30px;
}
.nav-grid a {
    text-decoration: none;
    text-align: center;
    display: block;
    padding: 12px;
    font-weight: bold;
    background: #e6f0ff;
    border: 2px solid #4a90e2;
    border-radius: 8px;
    color: #003366;
    transition: all 0.2s;
}
.nav-grid a:hover {
    background: #d0e4ff;
    transform: scale(1.03);
}
</style>

<div class="nav-grid">
    <a href="/?page=1_📈_AI予想">① AI予想</a>
    <a href="/?page=2_✍️_勝敗入力">② 勝敗入力</a>
    <a href="/?page=3_📊_統計データ">③ 統計データ</a>
    <a href="/?page=4_📋_結果履歴">④ 結果履歴</a>
    <a href="/?page=5_🚤_競艇結果">⑤ 競艇結果</a>
    <a href="/?page=6_⚙️_設定">⑥ 設定</a>
</div>
""", unsafe_allow_html=True)

# ↓↓↓ AI予想の中身をここに追加
st.markdown("🔮 本番AI予想（近日更新）")
