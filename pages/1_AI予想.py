import streamlit as st
import pandas as pd
from datetime import datetime
import random

# 現在時刻
now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

# タイトル表示
st.markdown(f"""
<div style='text-align: center; margin-bottom: 20px;'>
    <h5 style='color: gray;'>🕒 現在時刻（日本時間）</h5>
    <h3 style='margin-top: -10px;'>{now}</h3>
</div>
""", unsafe_allow_html=True)

# 本日のAI予想タイトル
st.markdown("""
<div style='text-align: center; font-size: 26px; font-weight: bold; margin-bottom: 10px;'>
🎯 本日のAI予想 <span style='font-size: 18px;'>(的中率重視)</span>
</div>
""", unsafe_allow_html=True)

# 枠付きテーブル風データ生成
def generate_predictions():
    boat_names = ['丸亀', '常滑', '福岡', '平和島', '若松']
    formulas = ['3連単', '2連単', '単勝']
    predictions = []

    for name in boat_names:
        formula = random.choice(formulas)
        if formula == '3連単':
            yoso = f"{random.randint(1,6)}-{random.randint(1,6)}-{random.randint(1,6)}"
        elif formula == '2連単':
            yoso = f"{random.randint(1,6)}-{random.randint(1,6)}"
        else:
            yoso = f"{random.randint(1,6)}"
        acc = f"{random.randint(80, 95)}%"
        predictions.append([name, formula, yoso, acc])
    
    return pd.DataFrame(predictions, columns=['競艇場', '式別', '予想', '的中率'])

df = generate_predictions()

# 表の表示（エクセル風）
st.markdown("""
<style>
th, td {
    text-align: center !important;
}
thead tr th {
    background-color: #e8f0fe;
    font-weight: bold;
    border: 1px solid #aab8c2;
}
tbody tr td {
    border: 1px solid #cbd5e0;
}
</style>
""", unsafe_allow_html=True)

st.table(df)

# フッター注記
st.caption("※仮AI予想です。正式版は後日連携予定です。")
