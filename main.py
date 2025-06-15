import streamlit as st
from datetime import datetime
import sys
import os

# ✅ calc_ecp の安全な読み込み
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
from calc_ecp import calculate_next_bet

# 🎯 プルダウン内容
boat_venues = [
    "桐生", "戸田", "江戸川", "平和島", "多摩川", "浜名湖", "蒲郡", "常滑",
    "津", "三国", "びわこ", "住之江", "尼崎", "鳴門", "丸亀", "児島",
    "宮島", "徳山", "下関", "若松", "芦屋", "福岡", "唐津", "大村"
]
bet_types = ["単勝", "複勝", "2連単", "2連複", "3連単", "3連複"]

# 📝 入力フォーム
st.markdown("### ✍️ 勝敗入力")

with st.form("result_form"):
    col1, col2 = st.columns(2)
    with col1:
        venue = st.selectbox("競艇場", boat_venues)
        bet_type = st.selectbox("式別", bet_types)
    with col2:
        bet_content = st.text_input("賭け内容", placeholder="例：1-2-3")
        win_or_lose = st.radio("結果", ["勝ち", "負け"], horizontal=True)

    total_funds = st.number_input("現在の残高（円）", min_value=0, value=7200)
    step = st.number_input("ステップ数", min_value=1, value=1)
    amount = calculate_next_bet(total_funds, step)

    st.markdown(f"💸 **推奨賭金：{amount}円**", unsafe_allow_html=True)
    submitted = st.form_submit_button("保存する")

if submitted:
    st.success(f"✅ {venue}・{bet_type}・{bet_content}｜{win_or_lose}（{amount}円）を保存しました（仮）")
