# main.py
import streamlit as st
import datetime
import pandas as pd

# 📅 日付と現在時刻
now = datetime.datetime.now()
weekday_jp = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"][now.weekday()]
today_str = now.strftime("%Y/%m/%d %H:%M:%S")

# 🕒 曜日＋現在時刻（中央揃え）
st.markdown(f"<h3 style='text-align:center'>{weekday_jp}</h3>", unsafe_allow_html=True)
st.markdown(f"<h4 style='text-align:center'>🕰️ 現在時刻：{today_str}</h4>", unsafe_allow_html=True)

# 💼 資金ステータス
st.markdown("### 💼 <span style='font-size:20px'>現在の資金ステータス</span>", unsafe_allow_html=True)

status_df = pd.DataFrame({
    "項目①": ["🎯 目標金額", "💰 準備資金", "📊 積立資金", "🧾 総収支", "📈 開始日"],
    "値①": ["10,000円", "10,000円", "0円", "+4,800円", "2025/06/01"],
    "項目②": ["🏆 勝率", "🎯 的中率", "✅ 回収率", "📅 計測日数", "📋 ベット回数"],
    "値②": ["70%", "85%", "125%", "15日", "40回"]
})
st.table(status_df)

# 📁 メニュー一覧 表形式で中央表示
st.markdown("## 📁 メニュー一覧", unsafe_allow_html=True)

menu_df = pd.DataFrame({
    "MENU①": ["① AI予想", "④ 結果履歴"],
    "MENU②": ["② 勝敗入力", "⑤ 開催結果"],
    "MENU③": ["③ 統計データ", "⑥ 設定"]
})
st.table(menu_df)
