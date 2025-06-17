import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="② 勝敗入力", layout="centered")

def show_page():
    st.title("② 勝敗入力")

    # 初期化
    place = race = bet_type = bet_content = ""
    amount = 0

    # ①のAI予想データ読み込み
    try:
        df_pred = pd.read_csv("ai_predictions.csv")

        # 番号付きリスト作成
        options = [f"{i+1}. {row['競艇場']} {row['レース']}｜{row['式別']} {row['予想']}" for i, row in df_pred.iterrows()]
        selected_index = st.selectbox("🔗 ①AI予想の番号から選択", ["---"] + options)

        if selected_index != "---":
            idx = int(selected_index.split(".")[0]) - 1
            row = df_pred.iloc[idx]
            place = row["競艇場"]
            race = row["レース"]
            bet_type = row["式別"]
            bet_content = row["予想"]
            amount = int(row["金額"])
    except Exception as e:
        st.warning("①のデータ（ai_predictions.csv）が見つからないか、読み込みに失敗しました。")

    # 📅 日付・レース情報
    st.markdown("#### 📅 日付・レース情報")

    date_input = st.date_input("日付", value=date.today())

    place_list = sorted(["唐津", "若松", "住之江", "丸亀", "尼崎", "芦屋", "浜名湖", "びわこ", "平和島", "多摩川", "蒲郡", "児島", "下関", "宮島", "徳山", "鳴門", "福岡"])
    race_list = [f"{i}R" for i in range(1, 13)]

    place_input = st.selectbox("競艇場名", options=place_list, index=place_list.index(place) if place in place_list else 0)
    race_input = st.selectbox("レース番号", options=race_list, index=race_list.index(race) if race in race_list else 0)

    bet_type_list = ["単勝", "2連単", "3連単", "2連複", "3連複"]
    bet_type_input = st.selectbox("🎯 式別", bet_type_list, index=bet_type_list.index(bet_type) if bet_type in bet_type_list else 0)

    # 🎲 ベット内容
    st.markdown("#### 🎲 ベット内容")
    col1, col2, col3 = st.columns(3)
    first = col1.selectbox("1着", list(range(1, 7)))
    second = col2.selectbox("2着", list(range(1, 7)))
    third = col3.selectbox("3着", list(range(1, 7)))

    # ベット内容を式別に応じて生成
    if bet_type_input in ["3連単", "3連複"]:
        bet_content_input = f"{first}-{second}-{third}"
    elif bet_type_input in ["2連単", "2連複"]:
        bet_content_input = f"{first}-{second}"
    else:
        bet_content_input = f"{first}"

    amount_input = st.number_input("💸 賭け金額（円）", min_value=0, step=100, value=amount)

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
        st.success("✅ 保存しました！")
