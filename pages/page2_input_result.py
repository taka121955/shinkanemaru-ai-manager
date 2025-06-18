import streamlit as st
import pandas as pd
from datetime import datetime
import os
import sys

# ECP計算モジュールを読み込み
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from calc_ecp import calculate_ecp_amounts

def show_page():
    st.set_page_config(page_title="② 勝敗入力", layout="centered")
    st.title("② 勝敗入力")

    # データ取得（①のスプレッドシート）
    csv_url = "https://docs.google.com/spreadsheets/d/1yfzSSgqA-1x2z-MF7xKnCMbFBJvb-7Kq4c84XSmRROg/export?format=csv&gid=1462109758"
    try:
        df = pd.read_csv(csv_url)
        df["的中率"] = df["的中率"].str.replace("%", "").astype(float)
        df_sorted = df.sort_values(by="的中率", ascending=False).head(10).reset_index(drop=True)
    except Exception as e:
        st.error(f"データ取得に失敗しました：{e}")
        return

    # 番号選択（1〜10）
    st.markdown("### 🔢 ページ①で選んだ番号を選択")
    番号 = st.selectbox("番号を選択", options=list(range(1, 11)))

    # 番号に該当するデータ取得
    selected = df_sorted.iloc[番号 - 1]

    # 結果（ラジオボタン）
    st.markdown("### 🎯 勝敗を選択")
    結果 = st.radio("的中 or 外れ", ["的中", "外れ"], horizontal=True)

    # 時刻・金額（ECP方式：第一波）
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    賭け金 = calculate_ecp_amounts(100)[0]  # 第一波100円基準

    # 保存処理
    if st.button("✅ 登録"):
        new_data = {
            "日時": now,
            "番号": 番号,
            "競艇場": selected["競艇場"],
            "レース番号": selected["レース番号"],
            "式別": selected["式別"],
            "投票内容": selected["投票内容"],
            "的中率": selected["的中率"],
            "結果": 結果,
            "金額": 賭け金
        }

        result_path = "results.csv"
        if os.path.exists(result_path):
            df_old = pd.read_csv(result_path)
            df_new = pd.concat([df_old, pd.DataFrame([new_data])], ignore_index=True)
        else:
            df_new = pd.DataFrame([new_data])

        df_new.to_csv(result_path, index=False)
        st.success("記録を保存しました ✅")

# ページ実行
show_page()
