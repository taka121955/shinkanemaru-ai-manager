import streamlit as st
import pandas as pd
from datetime import datetime
import os
import sys

# ✅ utilsディレクトリをパスに追加してcalc_ecpを読み込む
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from calc_ecp import calculate_ecp_amounts

def show_page():
    st.set_page_config(page_title="② 勝敗入力", layout="centered")
    st.title("② 勝敗入力")

    # ✅ スプレッドシート連携（ページ①と同じ）
    csv_url = "https://docs.google.com/spreadsheets/d/1yfzSSgqA-1x2z-MF7xKnCMbFBJvb-7Kq4c84XSmRROg/export?format=csv&gid=1462109758"

    try:
        df = pd.read_csv(csv_url)
        df["的中率"] = df["的中率"].str.replace("%", "").astype(float)
        df_sorted = df.sort_values(by="的中率", ascending=False).head(10).reset_index(drop=True)
        df_sorted.index += 1
        df_sorted["番号"] = df_sorted.index

        st.subheader("🎯 AI予想から対象を選択")
        selected_num = st.selectbox("対象番号（ページ①と連動）", df_sorted["番号"])
        selected_row = df_sorted[df_sorted["番号"] == selected_num].iloc[0]

        st.markdown(f"**🏁 {selected_row['競艇場']} {selected_row['レース番号']} | {selected_row['式別']} | {selected_row['投票内容']}**")

        # ✅ ECPに基づく自動金額計算
        total_fund = st.number_input("💰 初期資金（円）", min_value=1000, step=1000, value=10000)
        bet_amounts = calculate_ecp_amounts(total_fund)

        st.write("💴 自動ベット金額（ECP方式）：")
        for idx, amt in enumerate(bet_amounts, 1):
            st.write(f" - 第{idx}波：{amt}円")

        # ✅ 結果入力
        result = st.radio("🎯 結果", ["的中", "外れ"])
        if st.button("✅ 記録する"):
            st.success("保存しました！（仮動作）")

    except Exception as e:
        st.error(f"データの取得に失敗しました：{e}")

# 実行
show_page()
