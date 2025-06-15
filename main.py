import streamlit as st
from datetime import datetime

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# 日本時間の現在時刻
now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"<h2 style='text-align: center;'>🕒 現在時刻：{now}</h2>", unsafe_allow_html=True)

# タイトルと説明
st.markdown("<h1 style='text-align: center;'>💼 新金丸法 × AI資金マネージャー</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>以下のページを選択してください</p>", unsafe_allow_html=True)

# ページ選択ボタン（装飾のみ）
page_buttons = """
<div style='text-align: center; margin-top: 30px;'>
    <button disabled style='padding:10px 25px; margin:5px; font-size:18px;'>① AI予想</button>
    <button disabled style='padding:10px 25px; margin:5px; font-size:18px;'>② 勝敗入力</button>
    <button disabled style='padding:10px 25px; margin:5px; font-size:18px;'>③ 統計データ</button><br>
    <button disabled style='padding:10px 25px; margin:5px; font-size:18px;'>④ 結果履歴</button>
    <button disabled style='padding:10px 25px; margin:5px; font-size:18px;'>⑤ 競艇結果</button>
    <button disabled style='padding:10px 25px; margin:5px; font-size:18px;'>⑥ 資金設定</button>
</div>
"""
st.markdown(page_buttons, unsafe_allow_html=True)

# 資金情報（中央・大きめ）
fund_info = """
<div style='text-align: center; margin-top: 40px; font-size: 22px;'>
    🎯 <strong>目標金額</strong>：<span style='color:blue;'>50,000円</span><br>
    💰 <strong>準備金額</strong>：<span style='color:green;'>10,000円</span><br>
    📦 <strong>積立金額</strong>：<span style='color:orange;'>3,000円</span>
</div>
"""
st.markdown(fund_info, unsafe_allow_html=True)

# 制作者クレジット
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>制作：小島崇彦</p>", unsafe_allow_html=True)
