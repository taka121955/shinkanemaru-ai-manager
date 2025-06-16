import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

# 日本時間で現在時刻を取得
japan_time = datetime.now(pytz.timezone('Asia/Tokyo')).strftime("%Y/%m/%d %H:%M:%S")

# タイトル表示（中央揃え・太字・大きめ）
st.markdown(f"<h2 style='text-align: center; font-weight: bold;'>🕰️ 現在時刻：{japan_time}</h2>", unsafe_allow_html=True)

# ステータスタイトル（少し控えめ）
st.markdown("<h3 style='text-align: center; font-weight: bold;'>💼 現在の資金ステータス</h3>", unsafe_allow_html=True)

# データフレーム（2列×12項目）作成
status_data = {
    "項目①": ["🎯 目標金額", "💰 準備資金", "📊 積立資金", "🧾 総収支", "📈 開始日", "🎯 的中回数"],
    "値①": ["10,000円", "10,000円", "0円", "+4,800円", "2025/06/01", "23回"],
    "項目②": ["🏆 勝率", "🎯 的中率", "💹 回収率", "📅 計測日数", "📋 ベット回数", "📈 平均回収率"],
    "値②": ["70%", "85%", "125%", "15日", "40回", "121%"]
}
df_status = pd.DataFrame(status_data)

# 表表示（エクセル風に中央寄せ）
st.markdown("""
<style>
    .center-table {
        margin-left: auto;
        margin-right: auto;
        font-size: 17px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)
st.markdown(df_status.style.set_table_attributes("class='center-table'").hide(axis="index").to_html(), unsafe_allow_html=True)

# メニュー見出し（やや控えめ）
st.markdown("<h3 style='text-align: center; font-weight: bold;'>📋 メニュー一覧</h3>", unsafe_allow_html=True)

# メニュー表（2行×3列）
menu_data = {
    "MENU①": ["① AI予想", "④ 結果履歴"],
    "MENU②": ["② 勝敗入力", "⑤ 開催結果"],
    "MENU③": ["③ 統計データ", "⑥ 設定"]
}
df_menu = pd.DataFrame(menu_data)

# メニュー表示（中央寄せ・枠あり）
st.markdown(df_menu.style.set_table_attributes("class='center-table'").hide(axis="index").to_html(), unsafe_allow_html=True)

# 制作者表示
st.markdown("<p style='text-align: center;'>制作者：小島崇彦</p>", unsafe_allow_html=True)
