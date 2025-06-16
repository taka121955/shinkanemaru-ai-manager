import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

# 日本時間取得
japan_time = datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"<h4 style='text-align:center;'>🕰️ 現在時刻： {japan_time}</h4>", unsafe_allow_html=True)

# ステータスタイトル
st.markdown("<h4 style='text-align:center;'>💼 現在の資金ステータス</h4>", unsafe_allow_html=True)

# 表形式（2列縦並び構成に変換）
labels = [
    "🎯 目標金額", "10,000円",
    "💰 準備資金", "10,000円",
    "📊 積立資金", "0円",
    "🧾 総収支", "+4,800円",
    "📈 開始日", "2025/06/01",
    "🎯 的中回数", "23回",
    "🏆 勝率", "70%",
    "🎯 的中率", "85%",
    "💹 回収率", "125%",
    "📅 計測日数", "15日",
    "📋 ベット回数", "40回",
    "📈 平均回収率", "121%"
]

# 2列で並べる
col1 = labels[0::4] + labels[1::4]
col2 = labels[2::4] + labels[3::4]
data = {"項目①": col1[::2], "値①": col1[1::2], "項目②": col2[::2], "値②": col2[1::2]}
df = pd.DataFrame(data)

# 表を中央表示・囲みあり
st.markdown(df.to_html(index=False, justify="center", border=1), unsafe_allow_html=True)

# メニュー一覧タイトル
st.markdown("<h4 style='text-align:center;'>📋 メニュー一覧</h4>", unsafe_allow_html=True)

menu_df = pd.DataFrame({
    "MENU①": ["① AI予想", "④ 結果履歴"],
    "MENU②": ["② 勝敗入力", "⑤ 開催結果"],
    "MENU③": ["③ 統計データ", "⑥ 設定"]
})

st.markdown(menu_df.to_html(index=False, justify="center", border=1), unsafe_allow_html=True)

# 制作者名
st.markdown("<div style='text-align:center; padding-top: 1rem;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
