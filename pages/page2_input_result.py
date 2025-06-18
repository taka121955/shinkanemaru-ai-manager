import streamlit as st
import pandas as pd
from datetime import datetime
from utils.calc_ecp import calc_ecp  # ECP方式の自動計算

def show_page():
    st.title("② 勝敗入力 📝")

    st.markdown("#### 📅 日付とレース情報の入力")

    today = datetime.now().date()
    date = st.date_input("開催日", value=today)
    place = st.text_input("競艇場名", placeholder="例：唐津")
    race = st.text_input("レース番号", placeholder="例：12R")

    st.markdown("---")
    st.markdown("#### 🎯 結果の入力")

    result = st.radio("勝敗", ["的中", "不的中"])
    odds = st.number_input("オッズ", min_value=1.0, step=0.1)
    
    # ECP方式の金額自動指示
    st.markdown("#### 💰 ベット金額（ECP方式で自動計算）")
    selected_mode = st.radio("資金モード", ["1300円", "3900円", "10000円"], horizontal=True)
    ecp_values = calc_ecp(selected_mode)
    st.write("自動ベット金額：", ecp_values)

    if st.button("登録する"):
        new_record = {
            "日付": date.strftime("%Y-%m-%d"),
            "競艇場": place,
            "レース": race,
            "勝敗": result,
            "オッズ": odds,
            "資金モード": selected_mode,
            "ECP金額": ecp_values
        }

        try:
            df = pd.read_csv("results.csv")
            df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
        except FileNotFoundError:
            df = pd.DataFrame([new_record])

        df.to_csv("results.csv", index=False)
        st.success("✅ 登録が完了しました！")

# 呼び出し
show_page()
