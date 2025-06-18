import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

# Googleスプレッドシートのシート2（AI予想一覧）URL（CSV形式）
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTOvDnRZFO5SRIubHRTYOfEovEtKD-JJUDT1aymSssv6I7Rh4Km4S4KpR4I0gAIzGE0XMcc8c3Edh-s/pub?gid=1462109758&single=true&output=csv"

def show_page():
    st.set_page_config(page_title="⑦ 全レース予想", layout="centered")
    st.markdown("## ⑦ 本日の全レース\n### AI予想")

    # ✅ 日本時間の現在時刻を表示
    now_jst = datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y/%m/%d %H:%M:%S")
    st.markdown(f"🕒 現在時刻（日本時間） ： <span style='color: green;'>{now_jst}</span>", unsafe_allow_html=True)

    try:
        df = pd.read_csv(CSV_URL)

        st.subheader("📋 すべてのAI予想")
        st.dataframe(df, use_container_width=True)

        st.subheader("🏆 的中率トップ10")
        df_sorted = df.copy()
        df_sorted["的中率"] = df_sorted["的中率"].str.replace("%", "").astype(float)
        df_sorted = df_sorted.sort_values(by="的中率", ascending=False).head(10)
        df_sorted.insert(0, "番号", range(1, 11))  # 番号列を付ける

        st.table(df_sorted)

        # 🔽 ページ①用データ保存（クラウド環境では機能しない可能性あり）
        df_sorted.to_csv("ai_predictions.csv", index=False)
        st.success("✅ ページ①用の上位10件データを保存しました")

    except Exception as e:
        st.error(f"❌ データの取得に失敗しました：{e}")

# 最後に必ず呼び出し
show_page()
