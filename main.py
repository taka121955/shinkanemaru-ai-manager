import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="新金丸法 × AI資金マネージャー",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ✅ サイドバー完全非表示
st.markdown("""
<style>
.css-1lcbmhc.e1fqkh3o3, .css-164nlkn.e1fqkh3o3 {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# ✅ 上部：現在時刻・資金（見やすく強調）
jst = datetime.utcnow().astimezone()
st.markdown(f"""
<div style='text-align: center; margin-top: 10px; margin-bottom: 10px;'>
  <div style='font-size:16px;'>🕒 現在時刻（日本時間）</div>
  <div style='font-size:24px; font-weight:bold;'>{jst.strftime('%Y/%m/%d %H:%M:%S')}</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; font-size: 16px; line-height: 2em; margin-bottom: 10px;'>
🎯 <b>目標金額：10000円</b>　💰 <b>初期資金：5000円</b>　📊 <b>累積資金：7200円</b>
</div>
<hr style='margin: 12px 0;'>
""", unsafe_allow_html=True)

# ✅ ナビボタン：大きめ＆中央整列
st.markdown("""
<style>
.button-grid {
    display: grid;
    grid-template-columns: repeat(3, 150px);
    gap: 12px;
    justify-content: center;
    margin-bottom: 25px;
}
.button-grid a {
    display: block;
    padding: 10px 0;
    font-size: 15px;
    font-weight: bold;
    font-family: "ヒラギノ角ゴ ProN", "游ゴシック", sans-serif;
    text-align: center;
    background-color: #f0f7ff;
    color: #003366;
    border: 2px solid #4a90e2;
    border-radius: 6px;
    text-decoration: none;
    transition: 0.15s ease-in-out;
}
.button-grid a:hover {
    background-color: #e2efff;
    transform: scale(1.03);
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
st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-size: 14px;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
