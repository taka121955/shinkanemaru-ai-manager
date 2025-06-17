import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="② 勝敗入力", layout="centered")

def show_page():
    st.markdown("## ② 勝敗入力")

    # ✅ データの読み込み（存在しない場合でも動作するようにする）
    try:
        df = pd.read_csv("ai_predictions.csv")
        options = df[["競艇場", "レース"]].drop_duplicates().reset_index(drop=True)
        options["表示"] = options["競艇場"] + " - " + options["レース"]
        selected = st.selectbox("①の予想から選択", [""] + options["表示"].tolist())

        if selected != "":
            selected_row = options[options["表示"] == selected].iloc[0]
            default_place = selected_row["競艇場"]
            default_race = selected_row["レース"]
        else:
            default_place = ""
            default_race = ""
    except Exception as e:
        st.warning("①のデータ（ai_predictions.csv）が見つからないか、読み込みに失敗しました。")
        default_place = ""
        default_race = ""

    # ✅ 入力フォーム
    st.markdown("### 📅 日付・レース情報")
    col1, col2 = st.columns(2)
    with col1:
        race_date = st.date_input("日付", date.today())
    with col2:
        place = st.text_input("競艇場名", value=default_place)

    race_number = st.text_input("レース番号（例: 12R）", value=default_race)

    bet_type = st.selectbox("🎯 式別", ["単勝", "複勝", "2連単", "2連複", "3連単", "3連複"])

    st.markdown("### 🎲 ベット内容（例: 1-2-3）")
    col1, col2, col3 = st.columns(3)
    with col1:
        first = st.selectbox("1着", [""] + [str(i) for i in range(1, 7)])
    with col2:
        second = st.selectbox("2着", [""] + [str(i) for i in range(1, 7)])
    with col3:
        third = st.selectbox("3着", [""] + [str(i) for i in range(1, 7)])

    bet_amount = st.number_input("💴 賭け金額（円）", min_value=0, step=100)

    is_win = st.checkbox("✅ 結果", value=False)
    st.write("🎯 的中" if is_win else "❌ 外れ")

    # ✅ 登録ボタン
    if st.button("登録する"):
        st.success("登録が完了しました！")
