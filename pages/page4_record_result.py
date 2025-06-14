import streamlit as st
import pandas as pd
import os

st.subheader("📋 結果履歴（全記録）")

file_path = "results.csv"

# ファイル存在チェック＋空チェック
if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
    st.warning("記録ファイルが存在しないか、空です。")
    st.stop()

try:
    df = pd.read_csv(file_path)
except pd.errors.EmptyDataError:
    st.warning("ファイルは存在しますが、中身が空です。")
    st.stop()

if df.empty:
    st.info("まだ記録がありません。")
    st.stop()

# データ整形
df["払戻金"] = pd.to_numeric(df["払戻金"], errors="coerce").fillna(0)
df["賭金"] = pd.to_numeric(df["賭金"], errors="coerce").fillna(0)
df["利益"] = df["払戻金"] - df["賭金"]
df["的中"] = df["払戻金"] > 0
df = df.sort_values(by="日付", ascending=False)

# 表示
st.dataframe(df[["日付", "競艇場", "レース", "賭金", "払戻金", "利益", "的中"]], use_container_width=True)

if st.button("🧹 すべての記録をクリア（注意）"):
    df.drop(df.index, inplace=True)
    df.to_csv(file_path, index=False)
    st.success("すべての記録を削除しました。")
    st.experimental_rerun()
