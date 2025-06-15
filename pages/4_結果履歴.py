# pages/page4_record_result.py

import streamlit as st
import pandas as pd

st.markdown("## 📖 結果履歴")

csv_path = "results.csv"

try:
    df = pd.read_csv(csv_path)

    if df.empty:
        st.info("まだ登録された記録がありません。")
    else:
        df_display = df.copy()
        df_display.index += 1
        df_display = df_display.rename_axis("No.")
        df_display = df_display.rename(columns={
            "日付": "🗓 日付",
            "競艇場": "🚩 競艇場",
            "式別": "📘 式別",
            "投票内容": "✏️ 投票内容",
            "賭け金": "💰 賭け金",
            "的中": "🎯 的中",
            "オッズ": "📈 オッズ",
        })

        st.dataframe(df_display, use_container_width=True)

except FileNotFoundError:
    st.warning("結果ファイルが見つかりません。まだ登録されていない可能性があります。")
except pd.errors.EmptyDataError:
    st.warning("結果ファイルが空です。")
