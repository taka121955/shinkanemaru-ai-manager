import streamlit as st

st.title("⑥ 設定ページ（積立・準備金など）")

# 初期化（1回目だけ）
st.session_state.setdefault("目標金額", 0)
st.session_state.setdefault("準備金額", 0)
st.session_state.setdefault("積立金額", 0)

# 表示＆入力
st.session_state["目標金額"] = st.number_input("🎯 目標金額", step=1000, value=st.session_state["目標金額"])
st.session_state["準備金額"] = st.number_input("💰 準備金額", step=1000, value=st.session_state["準備金額"])
st.session_state["積立金額"] = st.number_input("📦 積立金額", step=1000, value=st.session_state["積立金額"])

# リセット機能（クリア用）
if st.button("🔁 リセット（全て0円に戻す）", type="primary"):
    st.session_state["目標金額"] = 0
    st.session_state["準備金額"] = 0
    st.session_state["積立金額"] = 0
    st.error("🔴 金額をリセットしました（保存はされません）")
