import streamlit as st

def show_page():
    st.markdown("## ⑥ 設定 ⚙️")

    # 📌 AI予想モードの設定
    st.subheader("📌AI予想モードの設定")
    mode = st.selectbox("予想モードを選択", ["的中率重視", "勝率重視"])

    # 💰 初期資金・目標金額設定
    st.subheader("💰 初期資金・目標金額設定")
    initial_fund = st.number_input("💵 初期資金（円）", min_value=0, step=100, value=10000)
    goal_amount = st.number_input("🎯 目標金額（円）", min_value=0, step=100, value=10000)

    # 🪙 軍資金（初期状態では初期資金と同じ扱い）
    war_fund = initial_fund

    # 📩 通知設定
    st.subheader("📩 通知設定（将来対応予定）")
    email_notify = st.checkbox("📧 メール通知を有効にする")
    line_notify = st.checkbox("💬 LINE通知を有効にする")

    # ⚠️ その他
    st.subheader("⚠️ その他")

    # ✅ 登録ボタン
    if st.button("✅ 設定を登録する"):
        st.success("✅ 設定が登録されました！")
        st.markdown("---")
        st.markdown("### ✅ 登録内容")
        st.write("🧠 AI予想モード：", mode)
        st.write("💵 初期資金：", f"{initial_fund:,} 円")
        st.write("🎯 目標金額：", f"{goal_amount:,} 円")
        st.write("🪙 軍資金（累積）：", f"{war_fund:,} 円")
        st.write("📧 メール通知：", "有効" if email_notify else "無効")
        st.write("💬 LINE通知：", "有効" if line_notify else "無効")
