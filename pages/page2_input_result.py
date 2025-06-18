import streamlit as st
import pandas as pd

CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTOvDnRZFO5SRIubHRTYOfEovEtKD-JJUDT1aymSssv6I7Rh4Km4S4KpR4I0gAIzGE0XMcc8c3Edh-s/pub?gid=1462109758&single=true&output=csv"

def show_page():
    st.title("② 勝敗入力（デバッグ版）")

    try:
        df = pd.read_csv(CSV_URL)
        st.success("✅ データ取得成功！")
    except Exception as e:
        st.error(f"❌ CSV読み込みエラー：{e}")
        return

    if df.empty:
        st.warning("⚠️ CSVは空です。中身を確認してください。")
        return

    st.write("🔍 読み込んだデータ（最初の5行）:")
    st.dataframe(df.head())

    if "番号" not in df.columns:
        st.error("❌ 『番号』列が存在しません。Googleシートを確認してください。")
        return

    df["番号"] = pd.to_numeric(df["番号"], errors="coerce")
    nums = df["番号"].dropna().unique().tolist()

    if not nums:
        st.warning("⚠️ 有効な『番号』データが見つかりません。")
        return

    selected = st.radio("🔢 番号を選択", nums)
    row = df[df["番号"] == selected].iloc[0]

    st.write("🧾 選択されたデータ：")
    st.json(row.to_dict())

# 呼び出し必須
show_page()
