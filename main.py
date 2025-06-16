import streamlit as st
from datetime import datetime
import pytz

st.set_page_config(layout="wide")

# 日本時間の現在時刻を中央上部に表示（太字・大きめ）
japan_time = datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y/%m/%d %H:%M:%S")
st.markdown(
    f"<h2 style='text-align: center; font-weight: bold;'>現在時刻：{japan_time}</h2>",
    unsafe_allow_html=True
)

st.markdown("---")

# 表タイトル（中央・太字・やや大きめ）
st.markdown("<h3 style='text-align: center; font-weight: bold;'>現在の資金ステータス</h3>", unsafe_allow_html=True)

# 2列×6行の表を2段（項目 → 数字）で中央に表示
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <div style='border: 2px solid #ccc; padding: 20px; font-weight: bold; font-size: 18px; text-align: center;'>
        🎯 目標金額<br>10000円<br><br>
        💰 準備資金<br>10000円<br><br>
        📊 積立資金<br>0円<br><br>
        📈 開始日<br>2025/06/01<br><br>
        📋 ベット回数<br>36回<br><br>
        🧮 総収支<br>+4,800円
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='border: 2px solid #ccc; padding: 20px; font-weight: bold; font-size: 18px; text-align: center;'>
        🏆 勝率<br>70%<br><br>
        🎯 的中率<br>85%<br><br>
        💹 回収率<br>125%<br><br>
        📆 計測日数<br>15日<br><br>
        🎯 的中回数<br>23回<br><br>
        📉 平均回収率<br>121%
    </div>
    """, unsafe_allow_html=True)

# フッター（制作者）
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>制作者：小島崇彦</p>", unsafe_allow_html=True)
