import streamlit as st
from datetime import datetime

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide", initial_sidebar_state="collapsed")

# 現在時刻
jst = datetime.utcnow().astimezone()
st.markdown(f"<h3 style='text-align: center;'>🕒 現在時刻（日本時間）：{jst.strftime('%Y/%m/%d %H:%M:%S')}</h3>", unsafe_allow_html=True)

# タイトルと案内
st.markdown("""
<div style='text-align: center; font-size: 24px; font-weight: bold;'>💼 新金丸法 × AI資金マネージャー</div>
<div style='text-align: center; font-size: 16px;'>各機能ページへは以下のナビゲーションからどうぞ</div>
""", unsafe_allow_html=True)

# ナビゲーションボタン（上部配置・ページ遷移）
st.markdown("""
<style>
.nav-container {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 16px;
    margin-top: 30px;
    margin-bottom: 30px;
}
.nav-container a {
    display: inline-block;
    padding: 14px 22px;
    font-size: 16px;
    font-weight: bold;
    text-decoration: none;
    border: 2px solid #4a90e2;
    background-color: #e6f0ff;
    color: #003366;
    border-radius: 8px;
    transition: all 0.2s;
}
.nav-container a:hover {
    background-color: #d0e4ff;
    transform: scale(1.05);
}
</style>

<div class="nav-container">
    <a href="/?page=1_AI予想">① AI予想</a>
    <a href="/?page=2_勝敗入力">② 勝敗入力</a>
    <a href="/?page=3_統計データ">③ 統計データ</a>
    <a href="/?page=4_結果履歴">④ 結果履歴</a>
    <a href="/?page=5_競艇結果">⑤ 競艇結果</a>
    <a href="/?page=6_設定">⑥ 設定</a>
</div>
""", unsafe_allow_html=True)

# トップページの内容（必要に応じて増やせます）
st.markdown("---")
st.markdown("### 🔰 このアプリの使い方")
st.markdown("""
- 上部のナビゲーションボタンから各ページへジャンプできます
- ページごとに別々の目的で設計されています
""")

# フッター
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
