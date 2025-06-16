import pandas as pd
import streamlit as st
from datetime import datetime
from pandas.errors import EmptyDataError

st.title("📊 今日の結果まとめ")

try:
    df = pd.read_csv("results.csv")
    if df.empty:
        st.warning("results.csv は空です。勝敗入力を先に行ってください。")
    else:
        # 通常処理へ進む（集計など）
        ...
except FileNotFoundError:
    st.error("results.csv が見つかりません。")
except EmptyDataError:
    st.error("results.csv が空のため、読み込めません。")
