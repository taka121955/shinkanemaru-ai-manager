import streamlit as st
from datetime import datetime
from utils.ecp import get_next_bet_amount, update_ecp
from utils.ai_predictor import get_ai_predictions
import pandas as pd

# 日本時間を太字・大きめで表示
japan_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"<h2 style='font-size:22px; font-weight:bold;'>🕒 日本時間：{japan_time}</h2>", unsafe_allow_html=True)

# AI予想（的中率 × 勝率重視）
st.markdown("### 🧠 AI予想（的中率 × 勝率重視）")
ai_predictions = get_ai_predictions()

if ai_predictions:
    for pred in ai_predictions:
        try:
            st.markdown(
                f"🏟️ {pred['場']} 🎯 {pred['レース']}R\n"
                f"📊 式別：{pred['式別']}　🎯 買い目：{pred['艇番']}\n"
                f"🧠 スコア：{pred['score']}"
            )
        except KeyError as e:
            st.error(f"⚠️ 必要な情報が欠けています：{e}")
else:
    st.info("🤖 現在、AI予想データが見つかりませんでした。")
