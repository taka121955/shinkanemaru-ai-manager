import streamlit as st
from datetime import datetime
from streamlit_extras.switch_page_button import switch_page

# タイトル非表示に設定（全ページで統一）
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide")

# 現在時刻（日本時間）
now = datetime.now()
japan_time = now.strftime("%Y/%m/%d %H:%M")
st.markdown(f"### 🕒 現在時刻（日本時間）：**{japan_time}**")

# 目標金額・初期資金・累積資金の表示
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("🎯 **目標金額**")
    st.session_state.setdefault("target_amount", 10000)
    st.number_input("目標金額", key="target_amount_input", value=st.session_state["target_amount"], step=100, format="%d")
    st.session_state["target_amount"] = st.session_state["target_amount_input"]

with col2:
    st.markdown("💰 **初期資金**")
    st.session_state.setdefault("initial_fund", 5000)
    st.number_input("初期資金", key="initial_fund_input", value=st.session_state["initial_fund"], step=100, format="%d")
    st.session_state["initial_fund"] = st.session_state["initial_fund_input"]

with col3:
    st.markdown("📊 **累積資金**")
    st.session_state.setdefault("cumulative_fund", 0)
    st.write(f"### ¥{st.session_state['cumulative_fund']}")

st.markdown("---")

# ページ説明
st.markdown("## 新金丸法 × AI予想資金マネージャー")

st.info("⬇️ 下のボタンから各ページに移動できます。")

# ページ下部ナビゲーション
st.markdown("---")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("① AI予想"):
        switch_page("page1_ai_prediction")
with col2:
    if st.button("② 勝敗入力"):
        switch_page("page2_input_result")
with col3:
    if st.button("③ 統計データ"):
        switch_page("page3_statistics")
with col4:
    if st.button("④ 結果履歴"):
        switch_page("page4_record_result")
with col5:
    if st.button("⑤ レース結果"):
        switch_page("page5_boat_results")

# 制作者表記
st.markdown("---")
st.markdown("### 制作者：小島崇彦")
