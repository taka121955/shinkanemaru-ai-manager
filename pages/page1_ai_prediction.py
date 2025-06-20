import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

def show_page():
    st.markdown("## 🎯 本日のAI予想（的中率トップ10）")

    # 日本時間の現在時刻
    japan_time = datetime.now(pytz.timezone("Asia/Tokyo"))
    formatted_time = japan_time.strftime("%Y/%m/%d %H:%M:%S")
    st.write(f"🕒 現在時刻（日本時間）： `{formatted_time}`")

    # 仮のAI予想データ（必要に応じてCSVやAPIから取得可）
    data = [
        {"順位": 1, "競艇場": "唐津", "レース番号": "1R", "式別": "2連単", "投票内容": "5-2", "的中率": "89.0%"},
        {"順位": 3, "競艇場": "住之江", "レース番号": "3R", "式別": "3連単", "投票内容": "6-3-3", "的中率": "82.0%"},
        {"順位": 2, "競艇場": "若松", "レース番号": "2R", "式別": "2連単", "投票内容": "1-6", "的中率": "70.0%"},
    ]

    df = pd.DataFrame(data)
    df.index = [1, 2, 3]  # 表示用の番号振り直し
    st.table(df)
