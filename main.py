# ===== 📁 メニュー一覧（見た目だけボタン風） =====
st.markdown("<h3 style='text-align: center;'>📁 メニュー一覧</h3>", unsafe_allow_html=True)

menu_list = [
    "① AI予想 🧠", "② 勝敗入力 ✍️", "③ 統計データ 📊",
    "④ 結果履歴 📁", "⑤ 開催結果 🏁", "⑥ 設定 ⚙️",
    "⑦ 場別予想 🏟️", "⑧ 総合評価 📊", "⑨ 特別分析 💡"
]

button_style = """
display: inline-block;
background-color: #f1f3f6;
border: 2px solid #ccc;
border-radius: 10px;
padding: 18px 0;
margin: 10px;
font-size: 18px;
font-weight: bold;
text-align: center;
width: 180px;
height: 60px;
"""

for i in range(0, 9, 3):
    cols = st.columns(3)
    for j in range(3):
        idx = i + j
        with cols[j]:
            st.markdown(
                f"<div style='{button_style}'>{menu_list[idx]}</div>",
                unsafe_allow_html=True
            )
