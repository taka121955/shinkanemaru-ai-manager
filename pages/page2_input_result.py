import streamlit as st
from datetime import datetime
from utils.calc_ecp import calculate_next_bet  # 修正済みモジュールが必要

# セッション初期化
if "records" not in st.session_state:
    st.session_state.records = []

st.markdown("## ② 🎯 ECP戦略に基づく 勝敗入力")

# 入力フォーム
date = st.date_input("日付", datetime.today())
race_no = st.selectbox("レース番号（例：1R）", [f"{i}R" for i in range(1, 13)])
stadium = st.selectbox("競艇場名", ["住之江", "戸田", "丸亀", "芦屋", "鳴門", "福岡", "浜名湖"])
odds = st.number_input("オッズ（例：3.5）", min_value=1.5, step=0.1)
result = st.radio("結果", ["不的中", "的中"])

# 自動賭け金計算
try:
    next_bet = calculate_next_bet(st.session_state.records, odds)
except Exception as e:
    next_bet = 0
    st.warning(f"⚠️ 賭け金計算に失敗しました: {e}")

st.number_input("賭け金（自動）", value=next_bet, step=100, disabled=True)

# 記録処理
if st.button("📩 記録する"):
    st.session_state.records.append({
        "日付": date.strftime("%Y/%m/%d"),
        "競艇場": stadium,
        "レース": race_no,
        "オッズ": odds,
        "的中": result == "的中",
        "賭け金": next_bet
    })
    st.success("✅ 記録しました")

# ページ遷移ナビゲーション（下部）
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.page_link("pages/page1_ai_prediction.py", label="① AI予想")
with col2:
    st.page_link("pages/page2_input_result.py", label="② 勝敗入力")
with col3:
    st.page_link("pages/page3_statistics.py", label="③ 統計データ")
with col4:
    st.page_link("pages/page4_record_result.py", label="④ 結果履歴")
