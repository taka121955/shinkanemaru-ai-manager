import streamlit as st
import pandas as pd
from datetime import datetime

# 📌 ダミーデータ（仮予想） ※あとでAIモデルと差し替え可
data = [
    ["唐津", "1R", "2連単", "1-5", "84%"],
    ["若松", "3R", "3連単", "4-5-6", "82%"],
    ["住之江", "4R", "単勝", "3", "81%"],
    ["丸亀", "5R", "2連単", "2-1", "80%"],
    ["平和島", "6R", "3連単", "3-2-6", "79%"],
    ["福岡", "7R", "2連単", "1-2", "77%"],
    ["常滑", "8R", "単勝", "4", "76%"],
    ["芦屋", "9R", "3連単", "5-6-1", "75%"],
    ["尼崎", "10R", "3連単", "6-4-3", "74%"],
    ["津", "11R", "単勝", "2", "73%"]
]

df = pd.DataFrame(data, columns=["競艇場", "レース番号", "式別", "投票内容", "的中率"])
df.index = df.index + 1  # 番号を1始まりにする

# ⏰ 現在時刻（日本時間）
japan_time = datetime.utcnow() + pd.Timedelta(hours=9)

# ✅ 表示開始
st.markdown("## 📉 本日のAI予想（上位10件）")
st.markdown(f"⏰ <b>現在の時刻：</b> <span style='color:green;'>{japan_time.strftime('%Y/%m/%d %H:%M:%S')}</span>", unsafe_allow_html=True)
st.table(df)
