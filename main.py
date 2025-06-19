if menu == "🏠 メインページ":
    st.markdown("## 📊 今日のステータス", unsafe_allow_html=True)

    # ===== ステータス変数（今後動的に置き換え可能）=====
    accuracy = "85%"
    win_loss = "3勝2敗"
    wins = 3
    losses = 2
    stack = "+4,800円"
    win_rate = "70%"
    return_rate = "125%"
    funds = 10000  # 現在の軍資金
    goal = 10000   # 目標金額

    # ===== 勝敗色（勝ち：青、負け：赤）=====
    win_color = "#007bff" if wins > losses else "#dc3545"

    # ===== 目標達成時：点滅する演出 =====
    flash_html = ""
    if funds >= goal:
        flash_html = """
        <div style="text-align:center; font-size:28px; font-weight:bold; animation: flash 1s infinite;">
            ✨ 目標達成！ ✨
        </div>
        <style>
        @keyframes flash {
            0% {color: gold;}
            50% {color: orange;}
            100% {color: gold;}
        }
        </style>
        """

    html = f"""
    {flash_html}
    <div style='text-align: center; font-size: 24px; font-weight: bold; line-height: 2;'>
        🎯 的中率：<span>{accuracy}</span><br>
        📈 勝敗：<span style='color:{win_color};'>{win_loss}</span><br>
        💰 積立金：<span>{stack}</span><br>
        🏆 勝率：<span>{win_rate}</span><br>
        ✅ 回収率：<span>{return_rate}</span><br>
        🎒 軍資金：<span>{funds:,}円</span><br>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

    st.markdown("---")
    st.info("左のメニューからページを選んでください。")
