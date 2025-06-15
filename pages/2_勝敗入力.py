import streamlit as st
import pandas as pd
from datetime import datetime
import os

from utils.calc_ecp import calculate_next_bet

st.markdown("## 📝 勝敗入力フォーム")
st.markdown("🎯 **AI予想をベースに入力**")

競艇場一覧 = ["若松", "芦屋", "唐津", "福岡", "大村", "住之江", "尼崎", "鳴門", "丸亀", "児島",
           "宮島", "徳山", "下関", "若松", "芦屋", "唐津", "浜名湖", "蒲郡", "常滑", "津",
           "三国", "びわこ", "住之江", "尼崎", "鳴門", "丸亀", "児島", "宮島", "徳山", "下関"]

式別一覧 = ["単勝", "複勝", "2連単", "3連単", "2連複", "3連複", "拡連複"]

# 初期資金・積立金（セッションステートで保持）
if 'initial_fund' not in st.session_state:
    st.session_state.initial_fund = 5000
if 'reserve_fund' not in st.session_state:
    st.session_state.reserve_fund = 0

# CSVファイルの読み込み
csv_path = "results.csv"
if os.path.exists(csv_path):
    try:
        df = pd.read_csv(csv_path)
    except pd.errors.EmptyDataError:
        df = pd.DataFrame(columns=["日付", "競艇場", "式別", "賭け内容", "賭け金", "的中", "波", "ステップ"])
else:
    df = pd.DataFrame(columns=["日付", "競艇場", "式別", "賭け内容", "賭け金", "的中", "波", "ステップ"])

# 勝敗入力フォーム
with st.form("bet_form"):
    col1, col2 = st.columns(2)
    with col1:
        place = st.selectbox("競艇場", options=競艇場一覧)
    with col2:
        bet_type = st.selectbox("式別", options=式別一覧)

    bet_content = st.text_input("反省内容（例：1-3-4）")

    # 直近データからECP方式の金額を計算
    records = df.to_dict(orient="records")
    bet_amount, wave, step, st.session_state.reserve_fund = calculate_next_bet(
        records, st.session_state.initial_fund, st.session_state.reserve_fund
    )

    if bet_amount is None:
        st.error("⚠️ ベット資金が不足しています。残高をリセットしてください。")
    else:
        st.markdown(f"💰 自動ハイハイ金（ECP方式） ： **{bet_amount}円**")

    hit = st.radio("的中しましたか？", options=["はい", "いいえ"])

    submitted = st.form_submit_button("✅ 登録する")
    if submitted and bet_amount is not None:
        today = datetime.now().strftime("%Y-%m-%d")
        result = {
            "日付": today,
            "競艇場": place,
            "式別": bet_type,
            "賭け内容": bet_content,
            "賭け金": bet_amount,
            "的中": True if hit == "はい" else False,
            "波": wave,
            "ステップ": step
        }

        new_df = pd.DataFrame([result])
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_csv(csv_path, index=False)
        st.success("✅ 勝敗が記録されました。")
