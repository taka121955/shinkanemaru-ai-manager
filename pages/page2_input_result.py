import streamlit as st
from datetime import date
from utils.calc_ecp import calculate_next_bet  # ECPロジック用関数

# 初期化
if "results" not in st.session_state:
    st.session_state["results"] = []
if "initial_fund" not in st.session_state:
    st.session_state["initial_fund"] = 10000
if "target_amount" not in st.session_state:
    st.session_state["target_amount"] = 20000

# 📄 ページタイトル
st.title("② 勝敗入力")

# 入力フォーム
st.write("### 🎯 ECP戦略に基づく勝敗入力")

col1, col2 = st.columns(2)
with col1:
    selected_date = st.date_input("日付", value=date.today())
    race_number = st.text_input("レース番号（例：1R）")
with col2:
    place = st.text_input("競艇場名（例：住之江）")
    odds = st.number_input("オッズ（例：3.5）", min_value=0.0, step=0.1)

# ECPに基づいた次の賭け金を自動算出
past_results = st.session_state["results"]
next_bet = calculate_next_bet(past_results, st.session_state["initial_fund"], st.session_state["target_amount"])

# 自動表示
st.number_input("賭け金（円）", min_value=0, step=100, value=next_bet, key="wager")

# 記録処理
if st.button("📥 記録する"):
    record = {
        "date": selected_date.strftime("%Y/%m/%d"),
        "place": place,
        "race": race_number,
        "wager": st.session_state["wager"],
        "odds": odds
    }
    st.session_state["results"].append(record)
    st.success("✅ 記録しました！")

# ナビゲーション
st.markdown("---")
col_nav1, col_nav2, col_nav3 = st.columns(3)
with col_nav1:
    if st.button("⬅️ ① AI予想", use_container_width=True):
        st.switch_page("pages/page1_ai_prediction.py")
with col_nav2:
    if st.button("📊 ③ 統計へ", use_container_width=True):
        st.switch_page("pages/page3_statistics.py")
with col_nav3:
    if st.button("📋 ④ 結果履歴", use_container_width=True):
        st.switch_page("pages/page4_record_result.py")
