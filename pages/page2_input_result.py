import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import os

# ✅ モジュールパスに 'utils' を追加（Streamlit Cloud対策）
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from calc_ecp import calculate_ecp_amounts

def show_page():
    st.set_page_config(page_title="② 勝敗入力", layout="centered")
    st.title("② 勝敗入力")

    # ⏰ 現在時刻（日本時間）
    jst_now = datetime.utcnow().astimezone().strftime("%Y/%m/%d %H:%M:%S")
    st.markdown(f"🕒 現在時刻（日本時間）： `{jst_now}`")

    try:
        # 📥 Googleスプレッドシートのシート2（全AI予想）
        csv_url = "https://docs.google.com/spreadsheets/d/1yfzSSgqA-1x2z-MF7xKnCMbFBJvb-7Kq4c84XSmRROg/export?format=csv&gid=1462109758"
        df = pd.read_csv(csv_url)

        df["的中率"] = df["的中率"].str.replace("%", "").astype(float)
        df_sorted = df.sort_values(by="的中率", ascending=False).head(10).reset_index(drop=True)
        df_sorted.index += 1
        df_sorted["番号"] = df_sorted.index

        st.subheader("🎯 AI予想から対象を選択")
        selected_num = st.selectbox("対象番号（ページ①と連動）", df_sorted["番号"])
        selected_row = df_sorted[df_sorted["番号"] == selected_num].iloc[0]

        st.markdown(f"**🏁 {selected_row['競艇場']} {selected_row['レース番号']} | {selected_row['式別']} | {selected_row['投票内容']}**")

        total_fund = st.number_input("💰 初期資金（円）", min_value=1000, step=1000, value=10000)
        bet_amounts = calculate_ecp_amounts(total_fund)

        st.write("💴 自動ベット金額（ECP方式）：")
        for i, amount in enumerate(bet_amounts, 1):
            st.write(f"第{i}波：{amount}円")

        result = st.radio("✅ 結果", ["的中", "外れ"])

        if st.button("記録する"):
            st.success("記録が保存されました！（仮）")

    except Exception as e:
        st.error(f"データ取得または処理に失敗しました：{e}")

# 実行
show_page()
