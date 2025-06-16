import streamlit as st
import pandas as pd
from datetime import datetime

# 現在時刻の表示
now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"🕐 **現在時刻：{now}**")

# データ表示（表形式）
data = {
    "項目": ["🎯 目標金額", "💰 準備資金", "📊 積立資金"],
    "金額": ["10,000円", "5,000円", "2,300円"],
    "項目2": ["🏆 勝率", "🎯 的中率", "💹 回収率"],
    "数値": ["70%", "65%", "115%"]
}
df = pd.DataFrame(data)
st.markdown("### 💼 現在の資金ステータス")
st.dataframe(df, use_container_width=True)

# メニュー選択
menu = st.radio("📁 メニュー選択", ["①AI予想", "②勝敗入力", "③統計データ", "④結果履歴", "⑤競艇結果"])

# フッター
st.markdown("---")
st.markdown("制作者：小島崇彦")
