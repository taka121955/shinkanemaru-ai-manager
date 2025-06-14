import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.title("① AI予想入力")

CSV_PATH = "ai_predictions.csv"

# 初期化：ファイルが存在しない場合は作成（オッズ列あり）
if not os.path.exists(CSV_PATH):
    df_init = pd.DataFrame(columns=["日付", "競艇場", "レース", "オッズ", "賭金", "的中"])
    df_init.to_csv(CSV_PATH, index=False, encoding="utf-8")

# 読み込み：エラー回避（空のとき）
try:
    df = pd.read_csv(CSV_PATH)
except pd.errors.EmptyDataError:
    df = pd.DataFrame(columns=["日付", "競艇場", "レース", "オッズ", "賭金", "的中"])
    df.to_csv(CSV_PATH, index=False, encoding="utf-8")

# 入力フォーム
with st.form("ai_form"):
    col1, col2 = st.columns(2)
    with col1:
        date = st.date_input("日付", value=datetime.today())
        stadium = st.text_input("競艇場（例：住之江）")
        race = st.text_input("レース番号（例：1R）")
    with col2:
        odds = st.number_input("オッズ（倍率）", min_value=1.0, step=0.1)
        bet = st.number_input("賭金（円）", min_value=0, step=100)
        result = st.selectbox("的中状況", ["的中", "不的中"])

    submitted = st.form_submit_button("記録する")

    if submitted:
        new_row = pd.DataFrame([{
            "日付": date.strftime('%Y/%m/%d'),
            "競艇場": stadium,
            "レース": race,
            "オッズ": odds,
            "賭金": bet,
            "的中": result
        }])

        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(CSV_PATH, index=False, encoding="utf-8")
        st.success("✅ AI予想を記録しました！")
