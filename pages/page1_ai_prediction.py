import streamlit as st
import pandas as pd
from datetime import datetime

def show_page():
    st.set_page_config(page_title="① AI予想", layout="centered")
    st.title("① AI予想")

    # 現在時刻の表示（日本時間）
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    st.markdown(f"🕒 現在時刻（日本時間）： `{now}`")

    try:
        # ✅ GoogleスプレッドシートのCSV URL（シート2）
        csv_url = "https://docs.google.com/spreadsheets/d/1yfzSSgqA-1x2z-MF7xKnCMbFBJvb-7Kq4c84XSmRROg/export?format=csv&gid=1462109758"
        df = pd.read_csv(csv_url)

        # 的中率：%を除去 → 数値化 → ソート → %表記に戻す
        df["的中率"] = df["的中率"].str.replace("%", "").astype(float)
        df_sorted = df.sort_values(by="的中率", ascending=False).head(10).reset_index(drop=True)
        df_sorted["的中率"] = df_sorted["的中率"].astype(int).astype(str) + "%"

        # 番号列（1〜10）を付与
        df_sorted.index += 1
        df_sorted.index.name = "番号"

        # 表示
        st.markdown("### 🎯 本日のAI予想（的中率トップ10）")
        st.table(df_sorted)

    except Exception as e:
        st.error(f"データの取得に失敗しました：{e}")

# ✅ 関数実行
show_page()
