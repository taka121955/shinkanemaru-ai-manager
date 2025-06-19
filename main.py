if menu == "🏠 メインページ":
    st.markdown("## 📊 今日のステータス")

    status_data = {
        "項目": ["🎯 的中率", "📈 勝敗", "💰 積立金", "🏆 勝率", "✅ 回収率", "🎒 軍資金"],
        "値": ["85%", "3勝2敗", "+4,800円", "70%", "125%", "10,000円"]
    }

    df_status = pd.DataFrame(status_data)

    # 表を中央に表示
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.table(df_status)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.info("左のメニューからページを選んでください。")
