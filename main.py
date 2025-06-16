import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(layout="centered")

# 📌 現在時刻
now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"### ⏰ 現在時刻：{now}")

# 🎯 資金ステータステーブル（行番号非表示）
status_data = {
    "項目": ["🎯 目標金額", "💰 準備資金", "📊 積立資金"],
    "金額": ["10,000円", "10,000円", "0円"],
    "項目2": ["🏆 勝率", "🎯 的中率", "💹 回収率"],
    "数値": ["70%", "85%", "125%"]
}
status_df = pd.DataFrame(status_data)
st.markdown("## 💼 <b>現在の資金ステータス</b>", unsafe_allow_html=True)
st.dataframe(status_df, use_container_width=True, hide_index=True)

# 📁 メニュー（操作不要の固定表示）
menu_data = {
    "0": ["① AI予想", "④ 結果履歴"],
    "1": ["② 勝敗入力", "⑤ 開催結果"],
    "2": ["③ 統計データ", "⑥ 設定"]
}
menu_df = pd.DataFrame(menu_data)
st.markdown("## 📁 <b>メニュー選択</b>", unsafe_allow_html=True)
st.dataframe(menu_df, use_container_width=True, hide_index=True)

# 🖋 制作者名
st.markdown("---")
st.markdown("### 制作者：小島崇彦")
