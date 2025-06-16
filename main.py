import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

# 日本時間の現在時刻を取得
now = datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y/%m/%d %H:%M:%S")

# ヘッダー（現在時刻）
st.markdown(f"<h3 style='text-align: center; color: #333;'>🕰️ 現在時刻：{now}</h3>", unsafe_allow_html=True)

# サブヘッダー（資金ステータス）少し小さく
st.markdown("<h4 style='text-align: center;'>💼 現在の資金ステータス</h4>", unsafe_allow_html=True)

# ステータスデータ
left_labels = ["🎯 目標金額", "💰 準備資金", "📊 積立資金", "🧾 総収支", "📈 開始日", "🎯 的中回数"]
left_values = ["10,000円", "10,000円", "0円", "+4,800円", "2025/06/01", "23回"]
right_labels = ["🏆 勝率", "🎯 的中率", "💹 回収率", "📅 計測日数", "📋 ベット回数", "📈 平均回収率"]
right_values = ["70%", "85%", "125%", "15日", "40回", "121%"]

# 表データ作成
data = {
    "項目①": left_labels,
    "値①": left_values,
    "項目②": right_labels,
    "値②": right_values
}
df = pd.DataFrame(data)

# 表表示（エクセル風）
st.dataframe(df, use_container_width=True)

# メニュータイトル（少し小さく）
st.markdown("<h4 style='text-align: center;'>📋 メニュー一覧</h4>", unsafe_allow_html=True)

# メニューデータ
menu_data = {
    "MENU①": ["① AI予想", "④ 結果履歴"],
    "MENU②": ["② 勝敗入力", "⑤ 開催結果"],
    "MENU③": ["③ 統計データ", "⑥ 設定"]
}
menu_df = pd.DataFrame(menu_data)

# メニュー表表示
st.dataframe(menu_df, use_container_width=True)

# 制作者
st.markdown("<p style='text-align: center;'>制作者：小島崇彦</p>", unsafe_allow_html=True)
