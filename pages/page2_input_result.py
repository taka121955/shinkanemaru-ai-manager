# pages/page2_input_result.py

import streamlit as st
import pandas as pd
import os

def show_page():
    st.set_page_config(page_title="② 勝敗入力", layout="centered")

    st.markdown("## ② 勝敗入力")

    # ai_predictions.csv 読み込み
    ai_data = None
    csv_path = "ai_predictions.csv"

    if os.path.exists(csv_path):
        try:
            ai_data = pd.read_csv(csv_path)
        except Exception as e:
            st.warning(f"⚠️ データ読み込みエラー: {e}")
    else:
        st.warning("①のデータ（ai_predictions.csv）が見つからないか、読み込みに失敗しました。")

    # 日付
    st.subheader("📅 日付・レース情報")
    date = st.date_input("日付", format="YYYY/MM/DD")

    # プルダウン選択肢
    boat_places = ai_data["競艇場"].unique().tolist() if ai_data is not None else []
    race_numbers = ai_data["レース"].unique().tolist() if ai_data is not None else []

    boat_place = st.selectbox("競艇場名", options=boat_places if boat_places else ["選択肢なし"])
    race_number = st.selectbox("レース番号", options=race_numbers if race_numbers else ["選択肢なし"])

    # 式別
    bet_type = st.selectbox("🎯 式別", ["単勝", "2連複", "2連単", "3連複", "3連単"])

    # ベット内容
    st.subheader("🎲 ベット内容")
    col1, col2, col3 = st.columns(3)
    choice1 = col1.selectbox("1着", ["-", "1", "2", "3", "4", "5", "6"])
    choice2 = col2.selectbox("2着", ["-", "1", "2", "3", "4", "5", "6"])
    choice3 = col3.selectbox("3着", ["-", "1", "2", "3", "4", "5", "6"])

    bet_amount = st.number_input("💰 賭け金額（円）", min_value=0, step=100)

    # 結果（的中 or 外れ）
    st.subheader("✅ 結果")
    result = st.radio("的中", ["的中", "外れ"])

    # 登録ボタン
    if st.button("登録"):
        st.success("✅ 登録が完了しました（※保存処理は仮実装）")
