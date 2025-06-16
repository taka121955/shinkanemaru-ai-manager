import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

# タイトル（現在時刻）
now = datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"<h3 style='text-align:center;'>🕰️ 現在時刻：{now}</h3>", unsafe_allow_html=True)

# 資金ステータスタイトル
st.markdown("<h2 style='text-align:center;'>💼 現在の資金ステータス</h2>", unsafe_allow_html=True)

# 資金ステータス表（2x12表示）
status_data = {
    "項目①": ["🎯 目標金額", "💰 準備資金", "📊 積立資金", "🧾 総収支", "📈 開始日", "🎯 的中回数"],
    "値①": ["10,000円", "10,000円", "0円", "+4,800円", "2025/06/01", "23回"],
    "項目②": ["🏆 勝率", "🎯 的中率", "💹 回収率", "📅 計測日数", "📋 ベット回数", "📈 平均回収率"],
    "値②": ["70%", "85%", "125%", "15日", "40回", "121%"]
}
df_status = pd.DataFrame(status_data)

# 表を中央＆Excel風に
st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
st.dataframe(df_status.style.set_properties(**{
    'text-align': 'center',
    'font-size': '18px',
    'font-weight': 'bold'
}), use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# メニュー一覧タイトル
st.markdown("<h2 style='text-align:center;'>📋 メニュー一覧</h2>", unsafe_allow_html=True)

# メニュー表
menu_data = {
    "MENU①": ["① AI予想", "④ 結果履歴"],
    "MENU②": ["② 勝敗入力", "⑤ 開催結果"],
    "MENU③": ["③ 統計データ", "⑥ 設定"]
}
df_menu = pd.DataFrame(menu_data)

# 表を中央に表示
st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
st.dataframe(df_menu.style.set_properties(**{
    'text-align': 'center',
    'font-size': '18px',
    'font-weight': 'bold'
}), use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# 制作者表記
st.markdown("<p style='text-align:center; font-size: 16px;'>制作者：小島崇彦</p>", unsafe_allow_html=True)
