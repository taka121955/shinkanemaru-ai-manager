import streamlit as st
from datetime import datetime

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# 現在時刻
now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"<h2 style='text-align:center; font-size:28px;'>🕒 現在時刻：{now}</h2>", unsafe_allow_html=True)

# タイトル
st.markdown("<h1 style='text-align:center; font-size:36px;'>💼 新金丸法 × AI資金マネージャー</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:20px;'>以下のページを選択してください</p>", unsafe_allow_html=True)

# メニューボタン風表示（非機能）
menu_html = """
<div style='text-align: center; margin-top: 30px;'>
    <span style='display:inline-block; background-color:#f0f0f0; padding:12px 25px; margin:5px; font-size:20px; border-radius:8px;'>① AI予想</span>
    <span style='display:inline-block; background-color:#f0f0f0; padding:12px 25px; margin:5px; font-size:20px; border-radius:8px;'>② 勝敗入力</span>
    <span style='display:inline-block; background-color:#f0f0f0; padding:12px 25px; margin:5px; font-size:20px; border-radius:8px;'>③ 統計データ</span><br>
    <span style='display:inline-block; background-color:#f0f0f0; padding:12px 25px; margin:5px; font-size:20px; border-radius:8px;'>④ 結果履歴</span>
    <span style='display:inline-block; background-color:#f0f0f0; padding:12px 25px; margin:5px; font-size:20px; border-radius:8px;'>⑤ 競艇結果</span>
    <span style='display:inline-block; background-color:#f0f0f0; padding:12px 25px; margin:5px; font-size:20px; border-radius:8px;'>⑥ 資金設定</span>
</div>
"""
st.markdown(menu_html, unsafe_allow_html=True)

# 資金ステータス表示
fund_html = """
<div style='text-align:center; margin-top: 40px; font-size:24px;'>
    🎯 <b>目標金額</b>：<span style='color:blue;'>50,000円</span><br>
    💰 <b>準備金額</b>：<span style='color:green;'>10,000円</span><br>
    📦 <b>積立金額</b>：<span style='color:orange;'>3,000円</span>
</div>
"""
st.markdown(fund_html, unsafe_allow_html=True)

# クレジット
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>制作：小島崇彦</p>", unsafe_allow_html=True)
