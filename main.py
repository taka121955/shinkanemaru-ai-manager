import streamlit as st
from datetime import datetime

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide", initial_sidebar_state="collapsed")

# 時刻表示
jst = datetime.utcnow().astimezone()
st.markdown(f"<h3 style='text-align: center;'>🕒 現在時刻（日本時間）：{jst.strftime('%Y/%m/%d %H:%M:%S')}</h3>", unsafe_allow_html=True)

# タイトルと案内
st.markdown("""
<div style='text-align: center; font-size: 22px; font-weight: bold;'>💼 新金丸法 × AI資金マネージャー</div>
<div style='text-align: center; font-size: 15px;'>以下のボタンから各ページへ移動してください</div>
""", unsafe_allow_html=True)

# 安定動作のボタンリンク（URL末尾に ?page=〇〇）
st.markdown("""
<style>
.button-grid {
    display: grid;
    grid-template-columns: repeat(2, 180px);
    gap: 16px;
    justify-content: center;
    margin-top: 30px;
    margin-bottom: 30px;
}
.button-grid a {
    display: inline-block;
    text-align: center;
    padding: 16px;
    font-size: 16px;
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
    <a href="/?page=1_AI予想">① AI予想</a>
    <a href="/?page=2_勝敗入力">② 勝敗入力</a>
    <a href="/?page=3_統計データ">③ 統計データ</a>
    <a href="/?page=4_結果履歴">④ 結果履歴</a>
    <a href="/?page=5_競艇結果">⑤ 競艇結果</a>
    <a href="/?page=6_設定">⑥ 設定</a>
</div>
""", unsafe_allow_html=True)

# フッター
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
