# main.py

import streamlit as st
import datetime
import pandas as pd

# ページ関数読み込み
from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_today_schedule import show_page as show_page5
from pages.page6_settings import show_page as show_page6
from pages.page7_per_boatplace_prediction import show_page as show_page7
from pages.page8_summary_today import show_page as show_page8

# 📅 日付と時刻
now = datetime.datetime.now()
weekday = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"][now.weekday()]
today_str = now.strftime("%Y/%m/%d %H:%M:%S")

# ⏱️ ヘッダー表示
st.markdown(f"<h3 style='text-align:center'>{weekday}</h3>", unsafe_allow_html=True)
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

# 🎮 メニュー
st.markdown("## 📂 メニュー選択")

menu = st.radio("選択してください", [
    "① AI予想", "② 勝敗入力", "③ 統計データ", "④ 結果履歴",
    "⑤ 出走表", "⑥ 設定", "⑦ 競艇場別予想", "⑧ 本日のまとめ"
])

if menu == "① AI予想":
    show_page1()
elif menu == "② 勝敗入力":
    show_page2()
elif menu == "③ 統計データ":
    show_page3()
elif menu == "④ 結果履歴":
    show_page4()
elif menu == "⑤ 出走表":
    show_page5()
elif menu == "⑥ 設定":
    show_page6()
elif menu == "⑦ 競艇場別予想":
    show_page7()
elif menu == "⑧ 本日のまとめ":
    show_page8()
