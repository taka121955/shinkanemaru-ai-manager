import streamlit as st
import pandas as pd
from datetime import datetime

def show_page():
    st.set_page_config(page_title="① AI予想", layout="centered")
    st.title("① AI予想")

    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    st.markdown(f"🕒 現在時刻（日本時間）： `{now}`")

    try:
        # ✅ Googleスプレッドシートの「シート2（全レース予想）」から取得
        csv_url = "https://docs.google.com/spreadsheets/d/1yfzSSgqA-1x2z-MF7xKnCMbFBJvb-7Kq4c84XSmRROg/export?format=csv&gid=1462109758"
        df = pd.read_csv(csv_url)

        # 的中率列を数値化し、ソート（上位10件）
        df["的中率"] = df["的中率"].str.replace("%", "").astype(float)
        df_sorted = df.sort_values(by="的中率", ascending=False).head(10).reset_index(drop=True)

        # 番号付与（1〜10）
        df_sorted.index += 1
        df_sorted.index.name = "番号"

        # 表示
        st.markdown("### 🎯 本日のAI予想（的中率トップ10）")
        st.table(df_sorted)

    except Exception as e:
        st.error(f"データの取得に失敗しました：{e}")

# ←呼び出しを忘れるとページが表示されません
show_page()
