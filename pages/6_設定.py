# pages/page6_settings.py

import streamlit as st

st.set_page_config(page_title="⑥ 設定", layout="centered")

def show_page():
    st.title("⚙️ 設定ページ")

    st.markdown("#### 🧭 アプリの基本設定を行うページです")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        goal = st.text_input("🎯 目標金額（例：100000）", value="100000")
    with col2:
        base = st.text_input("💰 初期資金（例：10000）", value="10000")

    st.markdown("#### 🔔 通知設定（今後対応）")
    email_notify = st.checkbox("📧 メール通知を有効にする", value=True)
    line_notify = st.checkbox("💬 LINE通知を有効にする", value=False)

    if st.button("💾 設定を保存"):
        st.success("✅ 設定内容を保存しました（※仮処理）")

    st.markdown("※ 現時点では保存されません。今後、CSVまたはDB対応予定です。")
