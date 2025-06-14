import streamlit as st
import pandas as pd
import os

st.subheader("📋 結果履歴（全記録）")

file_path = "results.csv"

# ファイルが存在しない場合
if not os.path.exists(file_path):
    st.warning("記録ファイルが存在しません。")
    st.stop()

# CSV読み込み
df = pd.read_csv(file_path)

if df.empty:
    st.info("まだ記録がありません。")
    st.stop()

# 数値変換と計算列
df["払戻金"] = pd.to_numeric(df["払戻金"], errors="coerce").fillna(0)
df["賭金"] = pd.to_numeric(df["賭金"], errors="coerce").fillna(0)
df["利益"] = df["払戻金"] - df["賭金"]
df["的中"] = df["払戻金"] > 0

# 日付の降順に並べ替え
df = df.sort_values(by="日付", ascending=False)

# 表示
st.dataframe(df[["日付", "競艇場", "レース", "賭金", "払戻金", "利益", "的中"]], use_container_width=True)

# クリアボタン
if st.button("🧹 すべての記録をクリア（注意）"):
    df.drop(df.index, inplace=True)
    df.to_csv(file_path, index=False)
    st.success("すべての記録を削除しました。")
    st.experimental_rerun()
