import streamlit as st
import pandas as pd
import os

# ✅ 最初に書く！
st.set_page_config(page_title="② 勝敗入力", layout="centered")

def show_page():
    st.title("② 勝敗入力")

    # 🔽 初期化
    predictions_df = None
    race_options = []
    place_options = []

    # 🔽 CSV読み込み（存在すれば）
    csv_path = "ai_predictions.csv"
    if os.path.exists(csv_path):
        try:
            predictions_df = pd.read_csv(csv_path)
            race_options = predictions_df["レース番号"].unique().tolist()
            place_options = predictions_df["競艇場"].unique().tolist()
        except Exception as e:
            st.warning(f"CSV読み込みに失敗しました: {e}")
    else:
        st.warning("①のデータ（ai_predictions.csv）が見つからないか、読み込みに失敗しました。")

    st.subheader("📅 日付・レース情報")

    # 🔽 日付
    date = st.date_input("日付")

    # 🔽 競艇場名（CSV連動 or 手動）
    race_place = st.selectbox("競艇場名", place_options if place_options else ["びわこ", "住之江", "丸亀", "若松", "蒲郡", "芦屋", "徳山", "唐津", "平和島"])

    # 🔽 レース番号（CSV連動 or 手動）
    race_no = st.selectbox("レース番号", race_options if race_options else [f"{i}R" for i in range(1, 13)])

    # 🔽 式別
    shikibetsu = st.selectbox("🎯 式別", ["単勝", "2連複", "2連単", "3連複", "3連単"])

    # 🔽 ベット内容
    st.subheader("🎲 ベット内容")
    col1, col2, col3 = st.columns(3)
    bet1 = col1.selectbox("1着", list(range(1, 7)))
    bet2 = col2.selectbox("2着", list(range(1, 7)))
    bet3 = col3.selectbox("3着", list(range(1, 7)))

    # 🔽 金額
    amount = st.number_input("💰 賭け金額（円）", min_value=0, step=100)

    # 🔽 結果
    result = st.radio("✅ 結果", ["的中", "外れ"])

    # 🔽 保存処理（仮）
    if st.button("💾 登録"):
        st.success("勝敗結果を保存しました（仮処理）")
