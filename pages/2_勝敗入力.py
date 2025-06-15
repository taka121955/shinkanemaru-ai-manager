import streamlit as st
import pandas as pd
from datetime import datetime

st.markdown("### ✍️ 勝敗入力")

# 入力フォーム
with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        place = st.selectbox("競艇場", ["丸亀", "平和島", "常滑", "若松", "福岡"])
        race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
        bet_type = st.selectbox("式別", ["単勝", "2連単", "3連単"])
    with col2:
        bet = st.text_input("賭け内容（例：1-3、2-5-6）")
        amount = st.number_input("賭け金額（円）", min_value=100, step=100)
        result = st.radio("結果", ["的中", "外れ"])
        payout = st.number_input("払戻金額（的中時のみ）", min_value=0, step=100)

    submitted = st.form_submit_button("記録する")

# 保存処理
if submitted:
    new_row = {
        "日時": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "競艇場": place,
        "レース": race,
        "式別": bet_type,
        "賭け内容": bet,
        "賭け金額": amount,
        "結果": result,
        "払戻金額": payout if result == "的中" else 0
    }

    try:
        df = pd.read_csv("results.csv")
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    except:
        df = pd.DataFrame([new_row])

    df.to_csv("results.csv", index=False)
    st.success("✅ 記録が保存されました！")

    with st.expander("📋 最新の入力内容"):
        st.write(pd.DataFrame([new_row]))
