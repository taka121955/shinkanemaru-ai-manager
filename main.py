if menu == "🏠 メインページ":
    st.markdown("## 🎯 現在の資金ステータス")

    st.write("以下は現在の資金状況と統計情報の概要です。")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🎯 目標金額", "100,000円")
    with col2:
        st.metric("💰 初期資金", "30,000円")
    with col3:
        st.metric("📊 累積収支", "12,000円")

    st.markdown("---")
    st.markdown("### 📁 ページ一覧")

    st.table(pd.DataFrame({
        "メニュー番号": ["①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨"],
        "ページ名": [
            "AI予想", "勝敗入力", "統計データ", "結果履歴", "開催結果",
            "設定", "場別予想", "総合評価", "特別分析"
        ]
    }))
