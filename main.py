if menu == "🏠 メインページ":
    st.markdown("## 📊 今日のステータス", unsafe_allow_html=True)

    html = """
    <div style='text-align: center; font-size: 24px; font-weight: bold; line-height: 2;'>
        🎯 的中率：<span style='color:#000;'>85%</span><br>
        📈 勝敗：<span style='color:#000;'>3勝2敗</span><br>
        💰 積立金：<span style='color:#000;'>+4,800円</span><br>
        🏆 勝率：<span style='color:#000;'>70%</span><br>
        ✅ 回収率：<span style='color:#000;'>125%</span><br>
        🎒 軍資金：<span style='color:#000;'>10,000円</span><br>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

    st.markdown("---")
    st.info("左のメニューからページを選んでください。")
