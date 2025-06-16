import streamlit as st
import pandas as pd

# 表示データを DataFrame にまとめる
data = {
    "項目": ["🎯 目標金額", "💰 準備資金", "📊 積立資金"],
    "金額": ["10,000円", "5,000円", "2,300円"],
    "項目2": ["🏆 勝率", "🎯 的中率", "💹 回収率"],
    "数値": ["70%", "65%", "115%"]
}

df = pd.DataFrame(data)

# 表風に表示（スタイル指定も可能）
st.markdown("### 💼 現在の資金ステータス")
st.dataframe(df.style.set_properties(**{
    'text-align': 'left',
    'border': '1px solid #ccc',
    'padding': '8px'
}), use_container_width=True)
