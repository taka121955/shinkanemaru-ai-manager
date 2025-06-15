import streamlit as st
import pandas as pd
import datetime

# ページ設定と背景色
st.set_page_config(page_title="AI予想", layout="centered")
st.markdown("<style>body { background-color: #fffdf5; }</style>", unsafe_allow_html=True)

# タイトル
st.markdown("## 📉 <b>本日のAI予想（上位10件）</b>", unsafe_allow_html=True)

# ⏰ 日本時間の現在時刻を表示
japan_time = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
st.markdown(
    f"⏰ <b>現在の時刻：</b> <code>{japan_time.strftime('%Y/%m/%d %H:%M:%S')}</code>",
    unsafe_allow_html=True
)

# 🔮 仮のAI予想データ（実装時は置き換え）
data = {
    "競艇場": ["唐津", "若松", "住之江", "丸亀", "平和島", "福岡", "常滑", "芦屋", "尼崎", "津"],
    "式別": ["2連単", "3連単", "単勝", "2連単", "3連単", "2連単", "単勝", "3連単", "3連単", "単勝"],
    "投票内容": ["1-5", "4-5-6", "3", "2-1", "3-2-6", "1-2", "4", "5-6-1", "6-4-3", "2"],
    "的中率": ["84%", "82%", "81%", "80%", "79%", "77%", "76%", "75%", "74%", "73%"]
}
df = pd.DataFrame(data)

# 表示
st.table(df)
