import streamlit as st
import pandas as pd
from datetime import datetime
import os

from utils.calc_ecp import calculate_next_bet

st.markdown("## 📝 勝敗入力フォーム", unsafe_allow_html=True)
st.markdown("🎯 <b>AI予想をベースに入力</b>", unsafe_allow_html=True)

競艇場一覧 = ["若松", "芦屋", "唐津", "福岡", "大村", "住之江", "尼崎", "鳴門", "丸亀", "児島",
           "宮島", "徳山", "下関", "浜名湖", "蒲郡", "常滑", "津", "三国", "びわこ"]

式別一覧 = ["単勝", "複勝", "2連単", "3連単", "2連複", "3連複", "拡連複"]

if 'initial_fund' not in st.session_state:
    st.session_state.initial_fund = 5000
if 'reserve_fund' not in st.session_state:
    st.session_state.reserve_fund = 0

csv_path = "results.csv"
if os.path.exists(csv_path):
    try:
        df = pd.read_csv(csv_path)
    except pd.errors.EmptyDataError:
        df = pd.DataFrame(columns=["日付", "競艇場", "式別", "賭け内容", "賭け金", "的中", "波", "ステップ"])
else:
    df = pd.DataFrame(columns=["日付", "競艇場", "式別", "賭け内容", "賭け金", "的中", "波", "ステップ"])

with st.form("bet_form"):
    col1, col2 = st.columns(2)
    with col1:
        place = st.selectbox("📍 競艇場", options=競艇場一覧)
    with col2:
        bet_type = st.selectbox("📘 式別", options=式別一覧)

    bet_content = st.text_input("📝 投票内容（例：1-3-4）")

    records = df.to_dict(orient="records")
    bet_amount, wave, step, st.session_state.reserve_fund = calculate_next_bet(
        records, st.session_state.initial_fund, st.session_state.reserve_fund
    )

    if bet_amount is None:
        st.error("⚠️ ベット資金が不足しています。残高をリセットしてください。")
    else:
        st.markdown(f"""
        💰 <span style='font-size:18px;'>自動賭け金（ECP方式）</span> ： <b>{bet_amount}円</b><br>
        <span style='color:gray;'>← この金額で登録されます</span>
        """, unsafe_allow_html=True)

    hit = st.radio("🎯 結果は？", options=["的中", "不的中"], horizontal=True)

    submitted = st.form_submit_button("✅ 登録する")
    if submitted and bet_amount is not None:
        today = datetime.now().strftime("%Y-%m-%d")
        result = {
            "日付": today,
            "競艇場": place,
            "式別": bet_type,
            "賭け内容": bet_content,
            "賭け金": bet_amount,
            "的中": True if hit == "的中" else False,
            "波": wave,
            "ステップ": step
        }

        new_df = pd.DataFrame([result])
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_csv(csv_path, index=False)
        st.success("✅ 勝敗が記録されました。")
