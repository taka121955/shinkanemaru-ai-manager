import streamlit as st
import pandas as pd
from datetime import datetime

# ページタイトル
st.subheader("① AI予想（的中率順 上位5件）")

# 仮のAI予想データ（※後で本物に差し替え可能）
ai_predictions = [
    {"競艇場": "住之江", "レース": "1R", "式別": "3連単", "買い目": "1-3-4", "的中率": 85},
    {"競艇場": "多摩川", "レース": "2R", "式別": "2連単", "買い目": "2-5", "的中率": 81},
    {"競艇場": "浜名湖", "レース": "3R", "式別": "3連単", "買い目": "3-2-6", "的中率": 78},
    {"競艇場": "丸亀", "レース": "5R", "式別": "2連複", "買い目": "1-4", "的中率": 74},
    {"競艇場": "芦屋", "レース": "6R", "式別": "3連複", "買い目": "2-3-5", "的中率": 70},
]

# 表示（的中率順に並び替え済み）
df = pd.DataFrame(ai_predictions)
st.table(df)

# 現在日時（日本時間）
japan_time = datetime.utcnow().astimezone().strftime("%Y/%m/%d %H:%M")
st.caption(f"更新時刻（日本時間）: {japan_time}")
