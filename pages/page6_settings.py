import streamlit as st

def show_page():
    st.markdown("## ⑥ 設定 ⚙️")

    st.markdown("### 📌 AI予想モードの設定")
    prediction_mode = st.selectbox("予想モードを選択", ["的中率重視", "勝率重視"])

    st.markdown("### 💰 初期資金・目標金額設定")
    initial_fund = st.number_input("💵 初期資金（円）", min_value=0, value=10000, step=100)
    target_fund = st.number_input("🎯 目標金額（円）", min_value=0, value=30000, step=100)

    st.markdown("### 📧 通知設定（将来対応予定）")
    st.checkbox("📩 メール通知を有効にする", value=False, disabled=True)
    st.checkbox("💬 LINE通知を有効にする", value=False, disabled=True)

    st.markdown("### ⚠️ その他")
    if st.button("🔄 初期状態にリセット"):
        st.warning("※ この機能は現在未実装です。")

    st.success("設定は保存されません（デモモード）")
