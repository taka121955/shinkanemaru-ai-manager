# main.py
import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

# タイトル非表示、ページ設定
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide")
st.markdown("<style>footer {visibility: hidden;}</style>", unsafe_allow_html=True)

# 日本時間
jst = pytz.timezone('Asia/Tokyo')
now = datetime.now(jst).strftime('%Y/%m/%d %H:%M:%S')

# CSVファイル読み込み
try:
    df = pd.read_csv("results.csv", encoding="utf-8")
    total_bet = df["賭金"].sum()
    total_return = df["払戻金"].sum()
    net_profit = total_return - total_bet
except Exception:
    total_bet = 0
    total_return = 0
    net_profit = 0

# 表示要素
st.markdown(f"<h1 style='text-align: center; font-size: 36px;'>{now}</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("🎯 **目標金額：** 10000円")
with col2:
    st.markdown("💰 **初期資金：** 10000円")
with col3:
    st.markdown(f"📊 **累積資金：** {net_profit}円")

# ナビゲーションボタン配置
st.markdown("---")
col_a1, col_a2, col_b1, col_b2 = st.columns([1, 1, 1, 1])
with col_a1:
    if st.button("① AI予想"):
        st.switch_page("pages/page1_ai_prediction.py")
with col_a2:
    if st.button("② 勝敗入力"):
        st.switch_page("pages/page2_input_result.py")
with col_b1:
    if st.button("③ 統計データ"):
        st.switch_page("pages/page3_statistics.py")
with col_b2:
    if st.button("④ 結果履歴"):
        st.switch_page("pages/page4_record_result.py")

st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
