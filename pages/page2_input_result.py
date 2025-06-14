import streamlit as st
import pandas as pd
from datetime import date
import os

CSV_PATH = "results.csv"

st.title("② 勝敗入力")

# プルダウン候補
競艇場一覧 = ["住之江", "戸田", "平和島", "大村", "芦屋", "蒲郡", "丸亀"]
レース番号 = [f"{i}R" for i in range(1, 13)]

# 入力フォーム
with st.form("result_form"):
    日付 = st.date_input("日付", value=date.today())
    競艇場 = st.selectbox("競艇場名", 競艇場一覧)
    レース = st.selectbox("レース番号", レース番号)
    賭金 = st.number_input("賭金（円）", min_value=0, step=100)
    オッズ = st.number_input("オッズ", min_value=0.0, step=0.1)

    submitted = st.form_submit_button("記録する")

    if submitted:
        new_data = pd.DataFrame([{
            "日付": 日付.strftime('%Y/%m/%d'),
            "競艇場": 競艇場,
            "レース": レース,
            "賭金": 賭金,
            "オッズ": オッズ
        }])

        if os.path.exists(CSV_PATH):
            df = pd.read_csv(CSV_PATH)
            df = pd.concat([df, new_data], ignore_index=True)
        else:
            df = new_data

        df.to_csv(CSV_PATH, index=False)
        st.success("✅ 記録しました！")
