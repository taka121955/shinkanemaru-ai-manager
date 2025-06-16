import streamlit as st
import pandas as pd
from datetime import datetime

# 📅 現在の日時（日本時間）
now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"### 🕒 現在時刻： {now}")

# 📊 資金ステータス（2列×3行）
status_df = pd.DataFrame({
    "項目": ["🎯 目標金額", "💰 準備資金", "📊 積立資金"],
    "金額": ["10,000円", "10,000円", "0円"],
    "項目2": ["🏆 勝率", "🎯 的中率", "💹 回収率"],
    "数値": ["70%", "85%", "125%"]
})
st.markdown("## 💼 現在の資金ステータス")
st.dataframe(status_df, use_container_width=True)

# 📂 メニュー（2行×3列）
menu_df = pd.DataFrame([
    ["① AI予想", "② 勝敗入力", "③ 統計データ"],
    ["④ 結果履歴", "⑤ 開催結果", "⑥ 設定"]
])
st.markdown("## 📂 メニュー選択")
st.dataframe(menu_df, use_container_width=True)

# 制作者名
st.markdown("---")
st.markdown("### 制作者：小島崇彦")
