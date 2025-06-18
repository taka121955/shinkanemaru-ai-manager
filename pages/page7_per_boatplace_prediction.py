import streamlit as st
import pandas as pd
from datetime import datetime

# Googleスプレッドシートのシート2（AI予想一覧）URL（CSV形式）
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTOvDnRZFO5SRIubHRTYOfEovEtKD-JJUDT1aymSssv6I7Rh4Km4S4KpR4I0gAIzGE0XMcc8c3Edh-s/pub?gid=1462109758&single=true&output=csv"

def show_page():
    st.set_page_config(page_title="⑦ 全レース予想", layout="centered")
    st.title("⑦ 本日の全レースAI予想")

    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    st.markdown(f"🕒 現在時刻（日本時間）： `{now}`")

    try:
        df = pd.read_csv(CSV_URL)

        st.subheader("📋 すべてのAI予想")
        st.dataframe(df, use_container_width=True)

        st.subheader("🏆 的中率トップ10")
        df_sorted = df.copy()
        df_sorted["的中率"] = df_sorted["的中率"].str.replace("%", "").astype(float)
        df_sorted = df_sorted.sort_values(by="的中率", ascending=False).head(10)

        df_sorted.insert(0, "番号", range(1, 11))  # 番号1〜10を自動で付与
        st.table(df_sorted)

        # 🔽 ページ①用に保存（番号付き上位10件のみ）
        df_sorted.to_csv("ai_predictions.csv", index=False)

        st.success("ページ①用の上位10件データを保存しました ✅")

    except Exception as e:
        st.error(f"データの取得に失敗しました：{e}")

# 最後に必ず呼び出し
show_page()
