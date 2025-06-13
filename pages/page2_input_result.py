import streamlit as st
import pandas as pd
from datetime import datetime
import os

# CSVファイルパス
CSV_PATH = "shinkanemaru_ai_manager/results.csv"

# 初期CSVが存在しない場合は作成
if not os.path.exists(CSV_PATH):
    df_init = pd.DataFrame(columns=["日時", "競艇場", "レース", "式別", "買い目", "賭金", "払戻", "的中"])
    df_init.to_csv(CSV_PATH, index=False)

st.subheader("② 勝敗入力")

# 入力フォーム
with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        boat_place = st.text_input("競艇場名", placeholder="例: 住之江")
        race_number = st.text_input("レース番号", placeholder="例: 1R")
        bet_type = st.selectbox("式別", ["3連単", "3連複", "2連単", "2連複", "単勝", "複勝"])
    with col2:
        bet = st.text_input("買い目", placeholder="例: 1-2-3")
        bet_amount = st.number_input("賭金（円）", step=100, min_value=0)
        payout = st.number_input("払戻（円）", step=100, min_value=0)

    submitted = st.form_submit_button("結果を記録")

# 送信時の処理
if submitted:
    hit = payout > 0
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_data = {
        "日時": now,
        "競艇場": boat_place,
        "レース": race_number,
        "式別": bet_type,
        "買い目": bet,
        "賭金": bet_amount,
        "払戻": payout,
        "的中": "◯" if hit else "×"
    }

    df = pd.read_csv(CSV_PATH)
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv(CSV_PATH, index=False)
    st.success("結果を記録しました！")

# 最新5件を表示
st.markdown("#### 🔍 最近の入力結果")
df_latest = pd.read_csv(CSV_PATH).tail(5)
st.dataframe(df_latest, use_container_width=True)
