import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

# 初期化
if 'records' not in st.session_state:
    st.session_state.records = []

# 勝敗入力フォーム
st.header("📝 勝敗入力")

# 競艇場選択（プルダウン）
places = ["若松", "住之江", "丸亀", "蒲郡", "大村"]
place = st.selectbox("競艇場", places)

# レース番号選択（プルダウン）
race_number = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])

# オッズ入力（1.5以上のみ）
odds = st.number_input("オッズ", min_value=1.5, step=0.1)

# 賭金入力
amount = st.number_input("賭金", min_value=100, step=100)

# 的中 / 不的中選択
result = st.radio("的中", ["的中", "不的中"])

# 登録ボタン
if st.button("記録"):
    win = result == "的中"
    profit = int(amount * (odds - 1)) if win else -amount

    japan_time = datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.records.append({
        "日付": japan_time,
        "競艇場": place,
        "レース": race_number,
        "オッズ": odds,
        "賭金": amount,
        "的中": result,
        "収支": profit
    })
    st.success("✅ 記録を保存しました。")

# 履歴表示
if st.session_state.records:
    df = pd.DataFrame(st.session_state.records)
    st.subheader("📊 勝敗履歴")
    st.dataframe(df)
