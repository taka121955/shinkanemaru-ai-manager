import pandas as pd
from datetime import datetime
import pytz
import streamlit as st

# --- 現在時刻（日本時間） ---
jst = pytz.timezone("Asia/Tokyo")
now = datetime.now(jst).strftime("%Y/%m/%d %H:%M:%S")
st.markdown(
    f"<h3 style='text-align: center;'>🕰️ 現在時刻： {now}</h3>",
    unsafe_allow_html=True
)

# --- ステータス見出し ---
st.markdown(
    "<h4 style='text-align: center;'>💼 現在の資金ステータス</h4>",
    unsafe_allow_html=True
)

# --- 現在の資金ステータス（2列×12行） ---
status_data = [
    ["🎯 目標金額", "10,000円", "🏆 勝率", "70%"],
    ["💰 準備資金", "10,000円", "🎯 的中率", "85%"],
    ["📊 積立資金", "0円", "💹 回収率", "125%"],
    ["🧾 総収支", "+4,800円", "📅 計測日数", "15日"],
    ["📈 開始日", "2025/06/01", "📋 ベット回数", "40回"],
    ["🎯 的中回数", "23回", "📉 平均回収率", "121%"]
]
df_status = pd.DataFrame(status_data, columns=["項目①", "値①", "項目②", "値②"])
st.dataframe(df_status, use_container_width=True)

# --- メニュー見出し（やや小さめ） ---
st.markdown(
    "<h5 style='text-align: center;'>📋 メニュー一覧</h5>",
    unsafe_allow_html=True
)

# --- メニュー（2行×3列） ---
menu_data = [
    ["① AI予想", "② 勝敗入力", "③ 統計データ"],
    ["④ 結果履歴", "⑤ 開催結果", "⑥ 設定"]
]
df_menu = pd.DataFrame(menu_data, columns=["MENU①", "MENU②", "MENU③"])
st.dataframe(df_menu, use_container_width=True)

# --- 制作者名（下部に中央寄せ） ---
st.markdown(
    "<p style='text-align: center;'>制作者：小島崇彦</p>",
    unsafe_allow_html=True
)
