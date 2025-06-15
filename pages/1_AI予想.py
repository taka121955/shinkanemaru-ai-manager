# pages/page1_ai_prediction.py

import streamlit as st
import pandas as pd
from datetime import datetime

# AI予想（仮）データ：上位10件（丸数字表示）
ai_predictions = [
    {"競艇場": "唐津", "式別": "2連単", "投票内容": "1-5", "的中率": "84%"},
    {"競艇場": "若松", "式別": "3連単", "投票内容": "4-5-6", "的中率": "82%"},
    {"競艇場": "住之江", "式別": "単勝", "投票内容": "3", "的中率": "81%"},
    {"競艇場": "丸亀", "式別": "2連単", "投票内容": "2-1", "的中率": "80%"},
    {"競艇場": "平和島", "式別": "3連単", "投票内容": "3-2-6", "的中率": "79%"},
    {"競艇場": "福岡", "式別": "2連単", "投票内容": "1-2", "的中率": "77%"},
    {"競艇場": "常滑", "式別": "単勝", "投票内容": "4", "的中率": "76%"},
    {"競艇場": "芦屋", "式別": "3連単", "投票内容": "5-6-1", "的中率": "75%"},
    {"競艇場": "尼崎", "式別": "3連単", "投票内容": "6-4-3", "的中率": "74%"},
    {"競艇場": "津", "式別": "単勝", "投票内容": "2", "的中率": "73%"},
]

# セッションに保存（②へ連携用）
st.session_state["ai_predictions"] = ai_predictions

# 丸数字のインデックス
maru_numbers = ['①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩']
df = pd.DataFrame(ai_predictions)
df.index = maru_numbers

# タイトル
st.markdown("### 📉 本日のAI予想（上位10件）")
st.markdown(f"🕓 現在の時刻： `{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}`")

# 表スタイル（Excel風）
st.dataframe(
    df.style.set_table_styles([
        {'selector': 'th', 'props': [('font-size', '18px'), ('text-align', 'center')]},
        {'selector': 'td', 'props': [('font-size', '16px')]}
    ]),
    height=520,
    use_container_width=True
)

# 案内
st.info("👉 ページ②で、上記の①〜⑩を選択し内容を反映できます。")
