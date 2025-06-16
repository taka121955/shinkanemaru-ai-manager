import streamlit as st
from datetime import datetime
import pytz
import pandas as pd

# 現在時刻（日本時間）
japan_time = datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y/%m/%d %H:%M:%S')
st.markdown(f"<h4 style='text-align:center;'>🕰️ 現在時刻： {japan_time}</h4>", unsafe_allow_html=True)

# タイトル
st.markdown("<h2 style='text-align:center;'>💼 現在の資金ステータス</h2>", unsafe_allow_html=True)

# データ
items = [
    ("🎯 目標金額", "🏆 勝率", "10,000円", "70%"),
    ("💰 準備資金", "🎯 的中率", "10,000円", "85%"),
    ("📊 積立資金", "💹 回収率", "0円", "125%"),
    ("🧾 総収支", "📅 計測日数", "+4,800円", "15日"),
    ("📈 開始日", "📋 ベット回数", "2025/06/01", "40回"),
    ("🎯 的中回数", "📉 平均回収率", "23回", "121%")
]

# 表形式で項目→値→項目→値の構成（エクセル風）
data = []
for left, right, left_val, right_val in items:
    data.append([left, right])
    data.append([left_val, right_val])

df = pd.DataFrame(data, columns=["項目①", "項目②"])
st.dataframe(df, use_container_width=True)

# メニュー一覧
st.markdown("<h3 style='text-align:center;'>🗂️ メニュー一覧</h3>", unsafe_allow_html=True)
menu_data = [
    ["① AI予想", "② 勝敗入力", "③ 統計データ"],
    ["④ 結果履歴", "⑤ 開催結果", "⑥ 設定"]
]
menu_df = pd.DataFrame(menu_data, columns=["MENU①", "MENU②", "MENU③"])
st.dataframe(menu_df, use_container_width=True)

# 制作者表示
st.markdown("<div style='text-align:center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
