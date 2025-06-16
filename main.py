import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

# 日本時間で時刻を取得
japan_time = datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"<h4 style='text-align:center;'>🕰️ 現在時刻： {japan_time}</h4>", unsafe_allow_html=True)

# ステータス見出し
st.markdown("<h5 style='text-align:center;'>💼 現在の資金ステータス</h5>", unsafe_allow_html=True)

# 表データ（2列ずつ並べる）
data = {
    "項目①": ["🎯 目標金額", "💰 準備資金", "📊 積立資金", "🧾 総収支", "📈 開始日", "🎯 的中回数"],
    "値①": ["10,000円", "10,000円", "0円", "+4,800円", "2025/06/01", "23回"],
    "項目②": ["🏆 勝率", "🎯 的中率", "💹 回収率", "📅 計測日数", "📋 ベット回数", "📈 平均回収率"],
    "値②": ["70%", "85%", "125%", "15日", "40回", "121%"]
}
df = pd.DataFrame(data)

# 表をエクセル風・中央表示で
st.markdown(df.to_html(index=False, justify="center", border=1), unsafe_allow_html=True)

# メニュー見出し（少し小さく）
st.markdown("<h5 style='text-align:center;'>📋 メニュー一覧</h5>", unsafe_allow_html=True)

menu_df = pd.DataFrame({
    "MENU①": ["① AI予想", "④ 結果履歴"],
    "MENU②": ["② 勝敗入力", "⑤ 開催結果"],
    "MENU③": ["③ 統計データ", "⑥ 設定"]
})
st.markdown(menu_df.to_html(index=False, justify="center", border=1), unsafe_allow_html=True)

# 制作者名
st.markdown("<div style='text-align:center; padding-top:1rem;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
