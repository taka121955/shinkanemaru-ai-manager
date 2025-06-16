import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

# 現在時刻（日本時間）
now = datetime.now(pytz.timezone("Asia/Tokyo")).strftime('%Y/%m/%d %H:%M:%S')
st.markdown(f"<h4 style='text-align:center;'>🕰️ 現在時刻： {now}</h4>", unsafe_allow_html=True)

# 見出し（小さめ）
st.markdown("<h5 style='text-align:center;'>💼 現在の資金ステータス</h5>", unsafe_allow_html=True)

# 表データ（縦並び）
data = {
    "項目①": ["🎯 目標金額", "10,000円",
             "💰 準備資金", "10,000円",
             "📊 積立資金", "0円",
             "🧾 総収支", "+4,800円",
             "📈 開始日", "2025/06/01",
             "🎯 的中回数", "23回"],

    "項目②": ["🏆 勝率", "70%",
             "🎯 的中率", "85%",
             "💹 回収率", "125%",
             "📅 計測日数", "15日",
             "📋 ベット回数", "40回",
             "📈 平均回収率", "121%"]
}

df = pd.DataFrame(data)
st.markdown(df.to_html(index=False, justify="center", border=1), unsafe_allow_html=True)

# メニュー
st.markdown("<h5 style='text-align:center;'>📋 メニュー一覧</h5>", unsafe_allow_html=True)

menu_df = pd.DataFrame({
    "MENU①": ["① AI予想", "④ 結果履歴"],
    "MENU②": ["② 勝敗入力", "⑤ 開催結果"],
    "MENU③": ["③ 統計データ", "⑥ 設定"]
})
st.markdown(menu_df.to_html(index=False, justify="center", border=1), unsafe_allow_html=True)

# 制作者名
st.markdown("<div style='text-align:center; padding-top:10px;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
