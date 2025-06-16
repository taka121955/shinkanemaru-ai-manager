import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

# 現在時刻（日本時間）
japan_time = datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"<h2 style='text-align:center; font-size:24px; font-weight:bold;'>現在時刻：{japan_time}</h2>", unsafe_allow_html=True)

# ステータスタイトル
st.markdown("<h2 style='text-align:center; font-weight:bold;'>💼 現在の資金ステータス</h2>", unsafe_allow_html=True)

# ステータス項目（2列12項目）
labels = [
    "🎯 目標金額", "🏆 勝率",
    "💰 準備資金", "🎯 的中率",
    "📊 積立資金", "💹 回収率",
    "🧮 総収支", "📅 計測日数",
    "📌 開始日", "📋 ベット回数",
    "🎯 的中回数", "📈 平均回収率"
]
values = [
    "10,000円", "70%",
    "10,000円", "85%",
    "0円", "125%",
    "+4,800円", "15日",
    "2025/06/01", "40回",
    "23回", "121%"
]

# 表データ作成（2列×6行）
rows = []
for i in range(0, len(labels), 2):
    rows.append([labels[i], values[i], labels[i+1], values[i+1]])

df_status = pd.DataFrame(rows, columns=["項目①", "値①", "項目②", "値②"])

# 表スタイルCSS
st.markdown("""
    <style>
    .dataframe {
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        margin-left: auto;
        margin-right: auto;
    }
    thead tr th {text-align: center;}
    td {text-align: center !important;}
    </style>
""", unsafe_allow_html=True)

# 表表示（資金ステータス）
st.dataframe(df_status, use_container_width=True)

# メニュー一覧
st.markdown("<h2 style='text-align:center; font-weight:bold;'>📁 メニュー一覧</h2>", unsafe_allow_html=True)

menu_labels = [
    "① AI予想", "② 勝敗入力", "③ 統計データ",
    "④ 結果履歴", "⑤ 開催結果", "⑥ 設定"
]
menu_rows = [[menu_labels[i], menu_labels[i+1], menu_labels[i+2]] for i in range(0, 6, 3)]
df_menu = pd.DataFrame(menu_rows, columns=["MENU①", "MENU②", "MENU③"])
st.dataframe(df_menu, use_container_width=True)

# フッター：制作者名
st.markdown("<div style='text-align:center; margin-top:30px;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
