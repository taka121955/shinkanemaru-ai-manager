import streamlit as st
from datetime import datetime
from pages.page1_ai_prediction import show_ai_prediction  # ← ①をインポート

st.set_page_config(
    page_title="新金丸法 × AI資金マネージャー",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ✅ 時刻と資金表示
jst = datetime.utcnow().astimezone()
st.markdown(f"<h3 style='text-align: center;'>🕒 現在時刻（日本時間）：{jst.strftime('%Y/%m/%d %H:%M:%S')}</h3>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; font-size: 18px;'>
🎯 目標金額：10000円　💰 初期資金：5000円　📊 累積立資金：7200円
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ✅ ボタンデザイン（横並び・統一スタイル）
st.markdown("""
<style>
.button-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 14px;
    margin-top: 20px;
}
.button-container form {
    margin: 0;
}
.button-container button {
    width: 150px;
    height: 60px;
    padding: 10px;
    font-size: 17px;
    font-weight: bold;
    border: 2px solid #4a90e2;
    background-color: #e6f0ff;
    border-radius: 8px;
    color: #003366;
    cursor: pointer;
    transition: 0.3s;
}
.button-container button:hover {
    background-color: #d0e4ff;
    transform: scale(1.03);
}
</style>

<div class="button-container">
    <form action="?page=1"><button type="submit">①AI予想</button></form>
    <form><button disabled>②勝敗入力</button></form>
    <form><button disabled>③統計データ</button></form>
    <form><button disabled>④結果履歴</button></form>
    <form><button disabled>⑤競艇結果</button></form>
    <form><button disabled>⑥設定</button></form>
</div>
""", unsafe_allow_html=True)

# ✅ ①ページ内容表示（クエリで判断）
page = st.query_params.get("page", "0")
if page == "1":
    show_ai_prediction()

# ✅ フッター
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
