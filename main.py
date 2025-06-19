if menu == "🏠 メインページ":
    st.markdown("## 📊 今日のステータス", unsafe_allow_html=True)

    # ▼ ステータス仮データ（後で自動化可能）
    accuracy = "85%"
    win_text = "3勝2敗"
    wins = 3
    losses = 2
    fund_now = 10000
    fund_goal = 10000
    stack = "+4,800円"
    win_rate = "70%"
    return_rate = "125%"

    # ▼ 勝敗色（青 or 赤）
    win_color = "#007bff" if wins > losses else "#dc3545"

    # ▼ 目標達成で点滅演出
    flash_html = ""
    if fund_now >= fund_goal:
        flash_html = """
        <div style='text-align:center; font-size:26px; font-weight:bold; animation: flash 1s infinite;'>
            ✨ <span style='color:gold;'>目標達成！</span> ✨
        </div>
        <style>
        @keyframes flash {
            0% {color: gold;}
            50% {color: orange;}
            100% {color: gold;}
        }
        </style>
        """

    # ▼ Excel風テーブル
    html_table = f"""
    {flash_html}
    <style>
    .excel-table {{
        width: 90%;
        margin: auto;
        border-collapse: collapse;
        font-size: 18px;
    }}
    .excel-table td {{
        border: 1px solid #999;
        padding: 8px 14px;
        text-align: left;
        font-weight: bold;
    }}
    .excel-table tr:nth-child(even) {{ background-color: #f9f9f9; }}
    </style>

    <table class="excel-table">
        <tr><td>🎯 的中率</td><td>{accuracy}</td></tr>
        <tr><td>📈 勝敗</td><td style='color:{win_color};'>{win_text}</td></tr>
        <tr><td>💰 積立金</td><td>{stack}</td></tr>
        <tr><td>🏆 勝率</td><td>{win_rate}</td></tr>
        <tr><td>✅ 回収率</td><td>{return_rate}</td></tr>
        <tr><td>🎒 軍資金</td><td>{fund_now:,}円</td></tr>
    </table>
    """
    st.markdown(html_table, unsafe_allow_html=True)

    # ▼ メニュー一覧（ボタン風）
    st.markdown("### 📁 メニュー一覧")
    buttons = [
        "① AI予想", "② 勝敗入力", "③ 統計データ",
        "④ 結果履歴", "⑤ 開催結果", "⑥ 設定",
        "⑦ 場別予想", "⑧ 総合評価", "⑨ 特別分析"
    ]
    btn_row = ""
    for b in buttons:
        btn_row += f"<a href='#' style='display:inline-block; margin:5px; padding:10px 20px; background-color:#f0f0f0; border-radius:6px; border:1px solid #ccc; text-decoration:none; font-weight:bold;'>{b}</a>"
    st.markdown(f"<div style='text-align:center;'>{btn_row}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.info("左のメニューからページを選んでください。")
