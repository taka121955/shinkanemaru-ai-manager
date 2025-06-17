import streamlit as st
import pandas as pd

def show_page():
    st.markdown("## ⑦ 出走場別12R予想 🐎")

    st.markdown("### 📅 本日の12Rレース予想（AI選定）")

    # 仮データ（例）
    data = {
        "競馬場": ["東京", "京都", "中山", "阪神", "札幌"],
        "レース番号": [12, 12, 12, 12, 12],
        "式別": ["単勝", "3連複", "馬連", "ワイド", "3連単"],
        "買い目": ["5", "3-5-8", "4-7", "2-6", "1-3-6"],
        "金額": ["1000円", "600円", "800円", "500円", "1000円"],
        "的中確率": ["82%", "67%", "74%", "71%", "69%"]
    }

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    st.markdown("※ 上記はAIによる簡易予想です（参考用）")
