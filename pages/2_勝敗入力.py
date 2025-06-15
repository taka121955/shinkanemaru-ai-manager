# pages/page2_input_result.py

import streamlit as st
import pandas as pd
from utils.calc_ecp import get_ecp_wave_distribution, calculate_next_bet

st.markdown("## 📝 勝敗入力フォーム")

# ✅ ① ページ①のAI予想から番号で連動
ai_predictions = st.session_state.get("ai_predictions", [])
maru_numbers = ['①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩']

selected_number = st.selectbox("🎯 登録する予想番号（①〜⑩）", maru_numbers)

# 初期値
selected_prediction = ai_predictions[maru_numbers.index(selected_number)] if ai_predictions else {
    "競艇場": "", "式別": "", "投票内容": "", "的中率": "0%"}

# 競艇場・式別・投票内容自動反映（入力不可）
st.markdown(f"🚩 競艇場： `{selected_prediction['競艇場']}`")
st.markdown(f"📘 式別： `{selected_prediction['式別']}`")
st.markdown(f"✏️ 投票内容： `{selected_prediction['投票内容']}`")

# ✅ ② ECP方式：賭け金計算（履歴仮：なし）
initial_fund = 10000
reserve_fund = 0
bet_amount, wave, step, reserve = calculate_next_bet([], initial_fund, reserve_fund)
st.markdown(f"💰 自動賭け金（ECP方式） ： **{bet_amount}円**")

# ✅ ③ 的中 or 不的中
result = st.radio("🎯 結果は？", ["的中", "不的中"], horizontal=True)

# ✅ ④ 登録ボタン
if st.button("✅ 登録する"):
    st.success(f"{selected_prediction['競艇場']}の予想（{selected_prediction['投票内容']}）を登録しました。")
