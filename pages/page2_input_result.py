import streamlit as st
import pandas as pd
from datetime import datetime
import os
import sys

# ✅ utils内のECP計算モジュールを読み込む
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from calc_ecp import calculate_ecp_amounts

def show_page():
    st.set_page_config(page_title="② 勝敗入力", layout="centered")
    st.title("② 勝敗入力")

    # ✅ CSVファイル名
    csv_file = "results.csv"

    st.subheader("📅 日付・レース情報")

    today = datetime.today().strftime("%Y/%m/%d")
    selected_date = st.date_input("日付", value=pd.to_datetime(today), key="date")

    selected_place = st.selectbox("競艇場名", ["唐津", "若松", "住之江", "丸亀", "児島", "徳山", "平和島", "蒲郡"])
    selected_race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])

    bet_type = st.selectbox("🎯 式別", ["単勝", "2連複", "2連単", "3連複", "3連単"])

    st.subheader("🎲 投票内容")
    col1, col2, col3 = st.columns(3)
    first = col1.selectbox("1着", ["", "1", "2", "3", "4", "5", "6"])
    second = col2.selectbox("2着", ["", "1", "2", "3", "4", "5", "6"])
    third = col3.selectbox("3着", ["", "1", "2", "3", "4", "5", "6"])

    result = st.radio("✅ 結果", ["的中", "外れ"])

    # ✅ 自動金額（ECP金丸法）
    try:
        amounts = calculate_ecp_amounts(mode="1300")
        bet_amount = sum(amounts)
        st.info(f"💴 賭け金額（ECP法）： {bet_amount} 円")
    except Exception as e:
        st.error(f"ECP金額計算に失敗しました：{e}")
        bet_amount = 0

    if st.button("保存"):
        vote = "-".join(filter(None, [first, second, third]))
        new_data = {
            "日付": selected_date.strftime("%Y/%m/%d"),
            "競艇場": selected_place,
            "レース": selected_race,
            "式別": bet_type,
            "投票内容": vote,
            "金額": bet_amount,
            "結果": result
        }

        # 既存CSVがあれば読み込み・追加、なければ新規作成
        if os.path.exists(csv_file):
            df = pd.read_csv(csv_file)
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        else:
            df = pd.DataFrame([new_data])

        df.to_csv(csv_file, index=False, encoding="utf-8-sig")
        st.success("✅ 勝敗結果を保存しました！")

# 🔁 実行
show_page()
