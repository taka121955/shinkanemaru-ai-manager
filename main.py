import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))import streamlit as st
from datetime import datetime  # ← これが必要です！

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide")

# ✅ 改善版：現在時刻と資金情報（パッと見やすく）
jst = datetime.utcnow().astimezone()

st.markdown(f"""
<div style='text-align: center; margin-top: 10px;'>
    <div style='font-size: 18px;'>🕒 <b>現在時刻（日本時間）</b></div>
    <div style='font-size: 28px; font-weight: bold; margin-top: 4px;'>
        {jst.strftime('%Y/%m/%d %H:%M:%S')}
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; font-size: 18px; line-height: 1.8em; margin-top: 12px;'>
    🎯 <b>目標金額：<span style="color:#d10000;">10000円</span></b>　
    💰 <b>初期資金：<span style="color:#007700;">5000円</span></b>　
    📊 <b>累積資金：<span style="color:#003399;">7200円</span></b>
</div>
<hr style='margin: 12px 0 20px 0;'>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.button-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    justify-items: center;
    margin-top: 10px;
    margin-bottom: 30px;
    padding: 0 10px;
}
.button-grid a {
    display: inline-block;
    width: 130px;
    height: 48px;
    line-height: 48px;
    text-align: center;
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
    transform: scale(1.03);
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
