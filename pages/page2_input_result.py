import streamlit as st
import pandas as pd
from datetime import datetime
import os

def show_page():
    st.set_page_config(page_title="② 勝敗入力", layout="centered")
    st.title("② 勝敗入力")

    # ✅ CSV読み込み（①と連動）
    csv_path = "ai_predictions.csv"
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)

        st.subheader("📅 日付・レース情報")

        today = datetime.today().strftime("%Y/%m/%d")
        st.date_input("日付", value=pd.to_datetime(today), key="date")

        # プルダウン用データ
        place_list = sorted(df["競艇場"].dropna().unique())
        race_list = sorted(df["レース"].dropna().unique())

        selected_place = st.selectbox("競艇場名", place_list)
        selected_race = st.selectbox("レース番号", race_list)

        # 式別
        bet_type = st.selectbox("🎯 式別", ["単勝", "2連複", "2連単", "3連複", "3連単"])

        st.subheader("🎲 ベット内容")
        col1, col2, col3 = st.columns(3)
        first = col1.selectbox("1着", ["", "1", "2", "3", "4", "5", "6"])
        second = col2.selectbox("2着", ["", "1", "2", "3", "4", "5", "6"])
        third = col3.selectbox("3着", ["", "1", "2", "3", "4", "5", "6"])

        amount = st.number_input("💴 賭け金額（円）", min_value=0, step=100)

        result = st.radio("✅ 結果", ["的中", "外れ"])

        if st.button("保存"):
            st.success(f"{selected_place} {selected_race} を記録しました ✅")
    else:
        st.warning("①のデータ（`ai_predictions.csv`）が見つからないか、読み込みに失敗しました。")
