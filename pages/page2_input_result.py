import streamlit as st
import pandas as pd
import sys
import os

# ← Streamlit Cloud用にutilsパスを明示追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ⬇️ utilsフォルダの関数を使う
from utils.calc_ecp import calculate_ecp_amounts

def show_page():
    st.set_page_config(page_title="② 勝敗入力", layout="centered")
    st.title("② 勝敗入力")

    # 入力フォーム
    st.markdown("#### AI予想結果を入力してください")
    race_num = st.number_input("対象レース番号", min_value=1, max_value=12, value=1)
    result = st.selectbox("勝敗結果", ["的中", "不的中"])
    
    # 金額はECP計算結果
    amount = calculate_ecp_amounts(wave=1, step=1)[0]  # 仮：wave=1, step=1

    if st.button("✅ 登録"):
        st.success(f"✅ レース{race_num}の結果 [{result}] を登録しました（金額: ¥{amount:,}）")

# 実行
show_page()
