import streamlit as st
import pandas as pd
import os
from datetime import date

st.set_page_config(page_title="② 勝敗入力", layout="centered")
st.markdown("## ② 勝敗入力")

# ファイルの存在確認と読み込み
if os.path.exists("ai_predictions.csv"):
    df = pd.read_csv("ai_predictions.csv")

    # 予想選択用のセレクトボックス
    prediction_options = [f"{i+1}. {row['競艇場']} {row['レース']} {row['式別']} {row['予想']}" for i, row in df.iterrows()]
    selected_index = st.selectbox("①のAI予想から選択", options=list(range(len(prediction_options))), format_func=lambda x: prediction_options[x])

    # 選択行データを取得
    selected_row = df.iloc[selected_index]

    st.markdown("### 📅 日付・レース情報")
    date_input = st.date_input("日付", value=date.today())
    
    stadium = st.selectbox("競艇場名", options=sorted(df["競艇場"].unique()), index=sorted(df["競艇場"].unique()).index(selected_row["競艇場"]))
    race_number = st.selectbox("レース番号", options=[f"{i}R" for i in range(1, 13)], index=int(str(selected_row["レース"]).replace("R", "")) - 1)

    st.markdown("### 🎯 式別")
    formula = st.selectbox("式別", ["単勝", "複勝", "2連単", "2連複", "3連単", "3連複"], index=["単勝", "複勝", "2連単", "2連複", "3連単", "3連複"].index(selected_row["式別"]))

    st.markdown("### 🎲 ベット内容")
    # 分割して入力欄
    try:
        n1, n2, n3 = selected_row["予想"].split("-")
    except:
        n1, n2, n3 = "", "", ""

    col1, col2, col3 = st.columns(3)
    first = col1.selectbox("1着", [str(i) for i in range(1, 7)], index=int(n1)-1 if n1.isdigit() else 0)
    second = col2.selectbox("2着", [str(i) for i in range(1, 7)], index=int(n2)-1 if n2.isdigit() else 0)
    third = col3.selectbox("3着", [str(i) for i in range(1, 7)], index=int(n3)-1 if n3.isdigit() else 0)

    st.markdown("### 💸 賭け金額（円）")
    amount = st.number_input("賭け金額", min_value=0, value=int(selected_row["金額"]))

    st.markdown("### ✅ 結果")
    result = st.radio("的中", ["的中", "はずれ"])

    st.success("🔁 ①のデータを連動し、編集も可能です。必要に応じて入力し直してください。")
else:
    st.warning("①のデータ（ai_predictions.csv）が見つからないか、読み込みに失敗しました。")
