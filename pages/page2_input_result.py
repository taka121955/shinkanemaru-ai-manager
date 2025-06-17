import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
import os

RESULTS_FILE = "results.csv"

def show_page():
    st.markdown("## ② 勝敗入力")

    # 入力フォーム
    with st.form("result_form"):
        col1, col2 = st.columns(2)
        with col1:
            date = st.date_input("📅 日付", datetime.now().date())
            race_place = st.text_input("🚩 競艇場名", "")
            race_no = st.text_input("🎯 レース番号（例: 12R）", "")
            bet_type = st.selectbox("🎲 式別", ["単勝", "複勝", "2連単", "3連単", "2連複", "3連複"])
        with col2:
            bet_content = st.text_input("📋 ベット内容（例: 1-2-3）", "")
            bet_amount = st.number_input("💸 賭け金額（円）", min_value=0, step=100)
            result = st.selectbox("✅ 結果", ["的中", "外れ"])
            payout = st.number_input("🏆 払戻金額（円）", min_value=0, step=100)

        submitted = st.form_submit_button("記録する")

    if submitted:
        jst = pytz.timezone("Asia/Tokyo")
        now = datetime.now(jst).strftime("%Y/%m/%d %H:%M:%S")
        data = {
            "記録時間": now,
            "日付": str(date),
            "競艇場": race_place,
            "レース": race_no,
            "式別": bet_type,
            "ベット": bet_content,
            "賭け金額": bet_amount,
            "結果": result,
            "払戻": payout
        }

        if os.path.exists(RESULTS_FILE):
            df = pd.read_csv(RESULTS_FILE)
        else:
            df = pd.DataFrame()

        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
        df.to_csv(RESULTS_FILE, index=False)
        st.success("✅ 結果が記録されました！")
