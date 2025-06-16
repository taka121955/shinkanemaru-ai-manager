import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

# タイトル表示（日本時間・中央・太字・小さめ）
japan_time = datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"<h4 style='text-align:center;'>🕰️ 現在時刻：{japan_time}</h4>", unsafe_allow_html=True)

# セクションタイトル（中央・小さめ）
st.markdown("<h5 style='text-align:center;'>💼 現在の資金ステータス</h5>", unsafe_allow_html=True)

# データ作成（2列 × 6行 = 12項目）
data = {
    "項目①": ["🎯 目標金額", "💰 準備資金", "📊 積立資金", "🧾 総収支", "📈 開始日", "🎯 的中回数"],
    "値①": ["10,000円", "10,000円", "0円", "+4,800円", "2025/06/01", "23回"],
    "項目②": ["🏆 勝率", "🎯 的中率", "💹 回収率", "📅 計測日数", "📋 ベット回数", "📈 平均回収率"],
    "値②": ["70%", "85%", "125%", "15日", "40回", "121%"]
}

df = pd.DataFrame(data)

# 表の表示（中央・インデックス非表示・枠付き）
st.markdown(
    df.to_html(index=False, justify='center', border=1),
    unsafe_allow_html=True
)

# メニューセクション（中央・小さめ）
st.markdown("<h5 style='text-align:center;'>📋 メニュー一覧</h5>", unsafe_allow_html=True)

menu_data = {
    "MENU①": ["① AI予想", "④ 結果履歴"],
    "MENU②": ["② 勝敗入力", "⑤ 開催結果"],
    "MENU③": ["③ 統計データ", "⑥ 設定"]
}
menu_df = pd.DataFrame(menu_data)

# メニュー表示（中央・インデックス非表示・枠付き）
st.markdown(
    menu_df.to_html(index=False, justify='center', border=1),
    unsafe_allow_html=True
)

# 制作者名（下部中央）
st.markdown("<div style='text-align:center; padding-top: 1rem;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
