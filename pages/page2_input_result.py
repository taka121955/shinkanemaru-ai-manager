import streamlit as st
import pandas as pd
from datetime import datetime
import os
import sys

# ECP計算用ファイルの読み込み（相対パス）
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from calc_ecp import calculate_ecp_amounts

def show_page():
    st.set_page_config(page_title="② 勝敗入力", layout="centered")
    st.title("② 勝敗入力")

    # スプレッドシート（① AI予想から）CSVとして読み込み
    csv_url = "https://docs.google.com/spreadsheets/d/1yfzSSgqA-1x2z-MF7xKnCMbFBJvb-7Kq4c84XSmRROg/export?format=csv&gid=1462109758"
    try:
        df = pd.read_csv(csv_url)
        df["的中率"] = df["的中率"].str.replace("%", "").astype(float)
        df_sorted = df.sort_values(by="的中率", ascending=False).head(10).reset_index(drop=True)
    except Exception as e:
        st.error(f"データ取得失敗：{e}")
        return

    # 番号リスト（1〜10）
    st.markdown("### ① で選んだ番号を選択してください")
   番号 = st.selectbox("番号を選択", options=list(range(1, 11)))

    # 番号に対応する行データ取得
    selected = df_sorted.iloc[番号 - 1]

    # 勝敗入力（ボタン式）
    st.markdown("### 結果を選択")
    結果 = st.radio("的中 or 外れ", ["的中", "外れ"], horizontal=True)

    # 日付
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    # ECP方式で金額を自動算出（第一波金額100円と仮定）
    賭け金 = calculate_ecp_amounts(100)[0]  # [100, 300, 900] → 第一波：100円

    # 登録ボタン
    if st.button("✅ 登録する"):
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

        # CSVに追記保存
        result_path = "results.csv"
        if os.path.exists(result_path):
            df_old = pd.read_csv(result_path)
            df_new = pd.concat([df_old, pd.DataFrame([new_data])], ignore_index=True)
        else:
            df_new = pd.DataFrame([new_data])

        df_new.to_csv(result_path, index=False)
        st.success("登録が完了しました ✅")

# 呼び出し
show_page()
