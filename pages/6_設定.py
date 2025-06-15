# pages/page6_funds_setting.py

import streamlit as st

st.markdown("## 💰 各種資金の設定")

st.markdown("### 🎯 目標金額")
goal_amount = st.number_input("目標金額を入力してください（円）", min_value=0, step=100, format="%d")

st.markdown("### 🪙 準備金額（初期資金）")
initial_fund = st.number_input("準備金額を入力してください（円）", min_value=0, step=100, format="%d")

st.markdown("### 📦 積立金額（AIによる繰越資金）")
reserve_fund = st.number_input("積立金額を入力してください（円）", min_value=0, step=100, format="%d")

if st.button("✅ 登録"):
    st.success(f"✅ 登録完了：目標 {goal_amount:,}円｜準備金 {initial_fund:,}円｜積立金 {reserve_fund:,}円")
    # 今後セッション保持 or CSV保存処理を追加可能
