import streamlit as st
from datetime import date
from utils.calc_ecp import calculate_next_bet

# --- セッション状態 ---
if "results" not in st.session_state:
    st.session_state["results"] = []
if "initial_fund" not in st.session_state:
    st.session_state["initial_fund"] = 10000
if "target_amount" not in st.session_state:
    st.session_state["target_amount"] = 20000

# --- タイトル ---
st.title("② ECP戦略に基づく 勝敗入力")

# --- 入力欄 ---
col1, col2 = st.columns(2)
with col1:
    input_date = st.date_input("日付", value=date.today())
    race_number = st.text_input("レース番号（例：1R）")
with col2:
    place = st.text_input("競艇場名（例：住之江）")
    odds = st.number_input("オッズ（例：3.5）", min_value=1.0, step=0.1)

# --- 賭け金（ECP自動計算） ---
try:
    wager = calculate_next_bet(
        st.session_state["results"],
        st.session_state["initial_fund"],
        st.session_state["target_amount"]
    )
except Exception as e:
    st.error(f"⚠️ 考察金計算に失敗しました: {e}")
    wager = 0

st.number_input("賭け金（自動）", min_value=0, step=100, value=wager, key="wager")

# --- 記録処理 ---
if st.button("📥 記録する"):
    new_data = {
        "date": input_date.strftime("%Y/%m/%d"),
        "place": place,
        "race": race_number,
        "wager": st.session_state["wager"],
        "odds": odds,
        "hit": None  # 勝敗はまだ未確定
    }
    st.session_state["results"].append(new_data)
    st.success("✅ 記録しました")

# --- ナビゲーション ---
st.markdown("---")
colA, colB, colC = st.columns(3)
with colA:
    if st.button("⬅️ ① AI予想"):
        st.switch_page("pages/page1_ai_prediction.py")
with colB:
    if st.button("📊 ③ 統計"):
        st.switch_page("pages/page3_statistics.py")
with colC:
    if st.button("📋 ④ 結果履歴"):
        st.switch_page("pages/page4_record_result.py")
