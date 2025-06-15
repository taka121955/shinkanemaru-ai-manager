import streamlit as st
import pandas as pd
from datetime import datetime

RESULTS_CSV = "results.csv"

def show_page():
    st.markdown("## ② 勝敗入力")
    st.markdown("レースの結果を以下のフォームから入力してください。")

    # 入力フォーム
    with st.form("result_form"):
        date = st.date_input("📅 日付", datetime.now().date())
        location = st.text_input("🏟️ 競艇場名")
        race_no = st.text_input("🎯 レース番号")
        bet_type = st.selectbox("🎫 式別", ["単勝", "複勝", "2連単", "3連単"])
        selected_boat = st.text_input("🚤 購入した艇番")
        amount = st.number_input("💴 賭け金（円）", min_value=100, step=100)
        result = st.selectbox("✅ 結果", ["的中", "不的中"])
        payout = st.number_input("🎉 払戻金（円）", min_value=0, step=100)

        submitted = st.form_submit_button("入力を保存")

    if submitted:
        new_data = {
            "日付": date.strftime('%Y-%m-%d'),
            "競艇場": location,
            "レース番号": race_no,
            "式別": bet_type,
            "艇番": selected_boat,
            "賭け金": amount,
            "結果": result,
            "払戻金": payout
        }

        try:
            df = pd.read_csv(RESULTS_CSV)
        except FileNotFoundError:
            df = pd.DataFrame()

        df = df.append(new_data, ignore_index=True)
        df.to_csv(RESULTS_CSV, index=False)
        st.success("結果が保存されました！")
