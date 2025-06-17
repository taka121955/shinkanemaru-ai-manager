# pages/page6_settings.py

import streamlit as st

st.set_page_config(page_title="⑥ 設定", layout="centered")

def show_page():
    st.title("⚙️ 設定ページ")

    st.markdown("#### 🧭 アプリの基本設定を行うページです")

    st.markdown("---")

    # 📌 初期資金や目標金額の入力（未保存：表示目的）
    col1, col2 = st.columns(2)

    with col1:
        goal = st.text_input("🎯 目標金額（例：100000）", value="100000")
    with col2:
        base = st.text_input("💰 初期資金（例：10000）", value="10000")

    st.markdown("---")

    # 🔔 通知設定（仮UI）
    st.markdown("#### 🔔 通知設定（※今後実装）")
    email_notify = st.checkbox("📧 メール通知を有効にする", value=True)
    line_notify = st.checkbox("💬 LINE通知を有効にする", value=False)

    st.markdown("---")

    # 💾 保存ボタン（仮）
    if st.button("💾 設定を保存"):
        st.success("✅ 設定内容を保存しました（仮処理）")

    st.markdown("※ 本設定は現時点では保存機能はありません。今後のアップデートで外部ファイル保存またはDB連携予定です。")
