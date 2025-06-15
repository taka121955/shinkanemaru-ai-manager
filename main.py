import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="新金丸法 × AI資金マネージャー",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ✅ サイドバー強制非表示
st.markdown("""
<style>
.css-1lcbmhc.e1fqkh3o3, .css-164nlkn.e1fqkh3o3 {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# ✅ 上部（時刻・資金情報）をスッキリ構成
jst = datetime.utcnow().astimezone()
st.markdown(f"""
<div style='text-align: center; margin-top: 5px; margin-bottom: 3px;'>
  <span style='font-size: 13px;'>🕒 現在時刻（日本時間）：</span><br>
  <span style='font-size: 20px; font-weight: bold;'>{jst.strftime('%Y/%m/%d %H:%M:%S')}</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; font-size: 13px; margin-bottom: 10px;'>
🎯 目標金額：<b>10000円</b>　💰 初期資金：<b>5000円</b>　📊 累積資金：<b>7200円</b>
</div>
<hr style='margin: 8px 0;'>
""", unsafe_allow_html=True)

# ✅ コンパクトナビボタン（3列2段・中央揃え）
st.markdown("""
<style>
.button-grid {
    display: grid;
    grid-template-columns: repeat(3, 130px);
    gap: 10px;
    justify-content: center;
    margin: 10px 0 20px;
}
.button-grid a {
    display: block;
    padding: 7px 0;
    font-size: 13px;
    font-weight: bold;
    text-align: center;
    background-color: #f2f8ff;
    color: #003366;
    border: 1px solid #4a90e2;
    border-radius: 6px;
    text-decoration: none;
    transition: 0.1s ease-in-out;
}
.button-grid a:hover {
    background-color: #e1efff;
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

# ✅ フッター（軽めに）
st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-size: 12px;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
