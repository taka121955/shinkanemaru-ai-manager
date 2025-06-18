import streamlit as st
import pandas as pd
import sys
import os

# ✅ モジュールのパスを明示的に追加（Streamlit Cloud対策）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.calc_ecp import calculate_ecp_amounts

def show_page():
    st.set_page_config(page_title="② 勝敗入力", layout="centered")
    st.title("② 勝敗入力")

    st.markdown("#### ✅ AI予想に対する結果入力")

    # レース番号
    race_number = st.number_input("🎯 レース番号", min_value=1, max_value=12, value=1)

    # 結果
    result = st.selectbox("🎲 結果", ["的中", "不的中"])

    # 波・段階を仮に固定（後で動的に変更可能）
    wave = 1
    step = 1
    amount = calculate_ecp_amounts(wave=wave, step=step)[0]

    st.write(f"💰 自動計算された金額（ECP）: ¥{amount:,}")

    if st.button("✅ 結果を登録"):
        st.success(f"✅ レース {race_number} の結果 [{result}] を登録しました（賭け金: ¥{amount:,}）")

show_page()
