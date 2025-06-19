# ===== 📁 メニュー一覧（美しく整列） =====
st.markdown("### 📁 メニュー一覧")

menu_labels = [
    "① AI予想", "② 勝敗入力", "③ 統計データ",
    "④ 結果履歴", "⑤ 開催結果", "⑥ 設定",
    "⑦ 場別予想", "⑧ 総合評価", "⑨ 特別分析"
]

# 表形式で3列配置
styled_buttons = ""
for i, label in enumerate(menu_labels):
    if i % 3 == 0:
        styled_buttons += "<div style='display: flex; justify-content: center; margin-bottom: 10px;'>"
    styled_buttons += f"""
        <div style='margin: 0 10px;'>
            <a href='#' style='
                display: inline-block;
                padding: 10px 20px;
                background-color: #f0f4f8;
                border-radius: 8px;
                border: 1px solid #ccc;
                text-decoration: none;
                font-weight: bold;
                color: #1a73e8;
                font-size: 16px;
                box-shadow: 1px 1px 3px rgba(0,0,0,0.1);
            '>{label}</a>
        </div>
    """
    if i % 3 == 2 or i == len(menu_labels) - 1:
        styled_buttons += "</div>"

st.markdown(styled_buttons, unsafe_allow_html=True)
