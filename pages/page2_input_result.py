import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.title("② 勝敗入力")

CSV_PATH = "results.csv"

# CSVが存在しない場合は作成
if not os.path.exists(CSV_PATH):
    df_init = pd.DataFrame(columns=["日付", "競艇場", "レース", "賭金", "払戻金"])
    df_init.to_csv(CSV_PATH, index=False, encoding="utf-8")

# 🔽 選択肢（必要に応じて増やせます）
stadium_options = [
    "住之江", "丸亀", "大村", "戸田", "多摩川", "若松", "芦屋", "蒲郡", "唐津", "宮島"
]
race_options = [f"{i}R" for i in range(1, 13)]

# 入力フォーム
with st.form("bet_form"):
    col1, col2 = st.columns(2)
    with col1:
        date = st.date_input("日付", value=datetime.today())
        stadium = st.selectbox("競艇場名を選択", stadium_options)
        race = st.selectbox("レース番号を選択", race_options)
    with col2:
        bet = st.number_input("賭金（円）", min_value=0, step=100)
        payout = st.number_input("払戻金（円）", min_value=0, step=100)

    submitted = st.form_submit_button("記録する")

    if submitted:
        new_data = pd.DataFrame([{
            "日付": date.strftime('%Y/%m/%d'),
            "競艇場": stadium,
            "レース": race,
            "賭金": bet,
            "払戻金": payout
        }])

        df = pd.read_csv(CSV_PATH)
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(CSV_PATH, index=False, encoding="utf-8")

        st.success("✅ 記録しました！")
