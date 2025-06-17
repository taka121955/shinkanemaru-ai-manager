# pages/page4_record_result.py

import streamlit as st
import pandas as pd
import os

# ✅ ページ設定（タイトルとレイアウト）
st.set_page_config(page_title="④ 結果履歴", layout="centered")

def show_page():
    st.title("📜 結果履歴")

    st.markdown("#### 📄 過去に入力された勝敗データ一覧")

    # CSVファイル名
    csv_path = "results.csv"

    # ファイルが存在しない場合
    if not os.path.exists(csv_path):
        st.warning("📂 結果データ（results.csv）がまだ存在しません。")
        st.info("勝敗入力ページからレース結果を登録すると、ここに一覧が表示されます。")
        return

    try:
        # CSV読み込み
        df = pd.read_csv(csv_path)

        if df.empty:
            st.info("📭 結果データはまだ登録されていません。")
        else:
            st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
