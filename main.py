import streamlit as st
import pandas as pd
from datetime import datetime

# 🕐 現在時刻（中央表示）
now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"<h5 style='text-align:center;'>🕐 現在時刻：{now}</h5>", unsafe_allow_html=True)

# ✅ 資金ステータス（項目の下に数値表示：2列 × 3行 × 2段）
left_labels = ["🎯 目標金額", "💰 準備資金", "📊 積立資金"]
left_values = ["10,000円", "5,000円", "2,300円"]
right_labels = ["🏆 勝率", "🎯 的中率", "💹 回収率"]
right_values = ["70%", "65%", "115%"]

st.markdown("### 💼 現在の資金ステータス")
st.markdown(
    f"""
    <table style="width:100%; text-align:center; font-size:18px; border-collapse:collapse;">
      <tr>
        <th>{left_labels[0]}</th><th>{right_labels[0]}</th>
      </tr>
      <tr>
        <td>{left_values[0]}</td><td>{right_values[0]}</td>
      </tr>
      <tr>
        <th>{left_labels[1]}</th><th>{right_labels[1]}</th>
      </tr>
      <tr>
        <td>{left_values[1]}</td><td>{right_values[1]}</td>
      </tr>
      <tr>
        <th>{left_labels[2]}</th><th>{right_labels[2]}</th>
      </tr>
      <tr>
        <td>{left_values[2]}</td><td>{right_values[2]}</td>
      </tr>
    </table>
    """,
    unsafe_allow_html=True
)

# ✅ メニュー（2段構成）
st.markdown("### 📁 メニュー選択")
st.markdown(
    """
    <style>
      .menu-table td {
        padding: 10px 20px;
        text-align: center;
        border: 1px solid #ccc;
        font-size: 16px;
      }
    </style>
    <table class='menu-table'>
      <tr>
        <td>① AI予想</td><td>② 勝敗入力</td><td>③ 統計データ</td>
      </tr>
      <tr>
        <td>④ 結果履歴</td><td>⑤ 競艇結果</td><td>⑥ ComingSoon</td>
      </tr>
    </table>
    """,
    unsafe_allow_html=True
)

# ✅ 制作者
st.markdown("---")
st.markdown("制作者：小島崇彦")
