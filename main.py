import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="新金丸法 × AI資金マネージャー",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ⏰ 現在時刻（日本時間）
jst = datetime.utcnow().astimezone()
st.markdown(f"""
    <div style='text-align: center; font-size: 26px; font-weight: bold; color: #333; margin-top: 10px;'>
        🕒 現在時刻（日本時間）：{jst.strftime('%Y/%m/%d %H:%M:%S')}
    </div>
""", unsafe_allow_html=True)

# 💼 タイトル + 説明
st.markdown("""
    <div style='text-align: center; font-size: 28px; font-weight: bold; margin-top: 20px;'>
        💼 新金丸法 × AI資金マネージャー
    </div>
    <div style='text-align: center; font-size: 16px; color: #555; margin-bottom: 25px;'>
        ページを選択してください
    </div>
""", unsafe_allow_html=True)

# 🔘 ボタン式ページリンク
st.markdown("""
<style>
.grid-buttons {
    display: grid;
    grid-template-columns: repeat(2, 180px);
    gap: 14px;
    justify-content: center;
    margin-bottom: 30px;
}
.grid-buttons a {
    display: inline-block;
    text-align: center;
    padding: 12px;
    font-size: 18px;
    font-weight: bold;
    color: #003366;
    background-color: #e6f0ff;
    border: 2px solid #4a90e2;
    border-radius: 8px;
    text-decoration: none;
    transition: all 0.2s;
}
.grid-buttons a:hover {
    background-color: #d0e4ff;
    transform: scale(1.03);
}
</style>

<div class="grid-buttons">
    <a href="/1_📈_AI予想">① AI予想</a>
    <a href="/2_✍️_勝敗入力">② 勝敗入力</a>
    <a href="/3_📊_統計データ">③ 統計データ</a>
    <a href="/4_📋_結果履歴">④ 結果履歴</a>
    <a href="/5_🚤_競艇結果">⑤ 競艇結果</a>
    <a href="/6_⚙️_設定">⑥ 設定</a>
</div>
""", unsafe_allow_html=True)

# 🖊 フッター
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
