import streamlit as st
import pandas as pd
import os

RESULTS_FILE = "results.csv"  # 正しいファイルパスに修正

def show_page():
    st.markdown("## ② 勝敗入力（デバッグ版）")

    # 入力フォーム
    st.write("以下の情報を入力してください。")
    col1, col2 = st.columns(2)
    with col1:
        venue = st.text_input("🎯 競艇場名（例：唐津）")
        race_number = st.text_input("🎯 レース番号（例：1R）")
    with col2:
        bet_amount = st.number_input("💴 賭け金額", min_value=100, step=100)
        odds = st.number_input("📈 オッズ", min_value=1.0, step=0.1)

    result = st.radio("🎯 結果", ["的中", "不的中"])

    if st.button("✅ 登録"):
        if venue and race_number and bet_amount > 0:
            payout = bet_amount * odds if result == "的中" else 0
            new_row = {
                "競艇場": venue,
                "レース番号": race_number,
                "賭け金額": bet_amount,
                "結果": result,
                "オッズ": odds,
                "払戻": payout
            }

            if os.path.exists(RESULTS_FILE):
                df = pd.read_csv(RESULTS_FILE)
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            else:
                df = pd.DataFrame([new_row])

            df.to_csv(RESULTS_FILE, index=False)
            st.success("✅ 勝敗情報を保存しました。")
        else:
            st.error("❌ 全ての項目を入力してください。")

    # 既存データの表示（デバッグ確認用）
    if os.path.exists(RESULTS_FILE):
        st.markdown("---")
        st.markdown("### 🗂 登録済みデータ（確認用）")
        df = pd.read_csv(RESULTS_FILE)
        st.dataframe(df)
    else:
        st.warning("📂 現在、保存されているデータはありません。")
