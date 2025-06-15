import streamlit as st
from datetime import datetime

# ✅ ページ設定（サイドバー非表示）
st.set_page_config(
    page_title="新金丸法 × AI資金マネージャー",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ✅ 現在時刻表示
jst = datetime.utcnow().astimezone()
st.markdown(f"<h3 style='text-align: center;'>🕒 現在時刻（日本時間）：{jst.strftime('%Y/%m/%d %H:%M:%S')}</h3>", unsafe_allow_html=True)

# ✅ 金額表示
st.markdown("""
<div style='text-align: center; font-size: 18px;'>
🎯 目標金額：10000円　💰 初期資金：5000円　📊 累積立資金：7200円
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ✅ 横並び固定ボタン（HTML使用・スマホ対応）
st.markdown("""
<style>
.button-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    margin-top: 10px;
}
.button-container form {
    margin: 0;
}
.button-container button {
    padding: 10px 20px;
    font-size: 16px;
    border: none;
    background-color: #f0f0f0;
    border-radius: 6px;
    cursor: pointer;
}
.button-container button:hover {
    background-color: #d0e0ff;
}
</style>

<div class="button-container">
    <form><button disabled>①AI予想</button></form>
    <form><button disabled>②勝敗入力</button></form>
    <form><button disabled>③統計データ</button></form>
    <form><button disabled>④結果履歴</button></form>
    <form><button disabled>⑤競艇結果</button></form>
    <form><button disabled>⑥設定</button></form>
</div>
""", unsafe_allow_html=True)

# ✅ ページ表示なし（非表示）
# ✅ フッター
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
