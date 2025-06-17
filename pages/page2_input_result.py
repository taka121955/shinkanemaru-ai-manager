import streamlit as st
from datetime import date

# ✅ ページ設定
st.set_page_config(page_title="② 勝敗入力", layout="centered")

def show_page():
    st.markdown("## ② 勝敗入力 📝")

    # 📅 日付選択
    selected_date = st.date_input("📅 日付", value=date.today())

    # 🏁 競艇場名（例）
    boat_places = ["住之江", "戸田", "芦屋", "丸亀", "蒲郡", "大村", "若松", "唐津", "徳山", "児島"]
    boat_place = st.selectbox("🚤 競艇場名", boat_places)

    # 🏁 レース番号
    race_number = st.selectbox("🎯 レース番号（例：12R）", [f"{i}R" for i in range(1, 13)])

    # 🎲 式別
    styles = ["単勝", "2連単", "2連複", "3連単", "3連複"]
    bet_style = st.selectbox("🎲 式別", styles)

    # 🐎 ベット内容
    st.markdown("### 🔢 ベット内容（例：1-2-3）")
    col1, col2, col3 = st.columns(3)
    first = col1.selectbox("1着", list(range(1, 7)))
    second = col2.selectbox("2着", list(range(1, 7)))
    third = col3.selectbox("3着", list(range(1, 7)))

    # 💴 金額
    amount = st.number_input("💰 賭け金額（円）", min_value=0, step=100)

    # ✅ 的中 or 不的中
    result = st.radio("✅ 結果", ["的中", "不的中"])

    # 💾 入力確認
    st.markdown("---")
    if st.button("登録する"):
        st.success(f"✅ 登録完了：{selected_date} {boat_place} {race_number}（{bet_style}） {first}-{second}-{third} / {amount}円 / {result}")
