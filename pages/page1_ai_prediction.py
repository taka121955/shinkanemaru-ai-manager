import streamlit as st
import pandas as pd
from utils.ai_prediction import generate_predictions

def show_page():
    st.title("①AI予想")
    st.markdown("## 🧠 本日のAIによる予想（上位5件）")

    try:
        predictions = generate_predictions()
        df = pd.DataFrame(predictions)
        df_sorted = df.sort_values(by="確率", ascending=False).head(5)

        st.dataframe(df_sorted.reset_index(drop=True))
    except Exception as e:
        st.error(f"予想の生成中にエラーが発生しました: {e}")
