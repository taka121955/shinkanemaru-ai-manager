import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="② 勝敗入力", layout="centered")

def show_page():
    st.title("② 勝敗入力")

    # 自動連動用データ読み込み
    try:
        df_pred = pd.read_csv("ai_predictions.csv")
        selected_row = st.selectbox("🔗 ①のAI予想から選択（任意）", ["---"] + df_pred.index.astype(str).tolist())

        if selected_row != "---":
            row = df_pred.loc[int(selected_row)]
            place = row["競艇場"]
            race = row["レース"]
            bet_type = row["式別"]
            bet_content = row["予想"]
            amount = row["金額"]
        else:
            place = race = bet_type = bet_content = ""
            amount = 0
    except:
        st.warning("①のデータ（ai_predictions.csv）が見つかりません。")
        place = race = bet_type = bet_content = ""
        amount = 0

    st.markdown("#### 📅 日付・レース情報")
    date_input = st.date_input("日付", value=date.today())
    place_input = st.text_input("競艇場名", value=place)
    race_input = st.text_input("レース番号（例: 12R）", value=race)
    bet_type_input = st.selectbox("🎯 式別", ["単勝", "2連単", "3連単", "2連複", "3連複"], index=0 if bet_type == "" else ["単勝", "2連単", "3連単", "2連複", "3連複"].index(bet_type))

    st.markdown("#### 🎲 ベット内容")
    col1, col2, col3 = st.columns(3)
    first = col1.selectbox("1着", list(range(1, 7)))
    second = col2.selectbox("2着", list(range(1, 7)))
    third = col3.selectbox("3着", list(range(1, 7)))

    bet_content_input = f"{first}-{second}-{third}" if bet_type_input in ["3連単", "3連複"] else f"{first}-{second}" if bet_type_input in ["2連単", "2連複"] else str(first)

    amount_input = st.number_input("💸 賭け金額（円）", min_value=0, step=100, value=int(amount) if amount != "" else 0)

    result = st.radio("🟩 結果", ["的中", "ハズレ"])

    if st.button("✅ 保存"):
        new_row = {
            "日付": date_input.strftime("%Y-%m-%d"),
            "競艇場": place_input,
            "レース番号": race_input,
            "式別": bet_type_input,
            "ベット内容": bet_content_input,
            "賭け金額": amount_input,
            "結果": result
        }

        try:
            df = pd.read_csv("results.csv")
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        except FileNotFoundError:
            df = pd.DataFrame([new_row])

        df.to_csv("results.csv", index=False)
        st.success("保存しました！")
