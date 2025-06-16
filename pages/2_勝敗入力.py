import streamlit as st

st.markdown("## 📝 勝敗入力フォーム")

# 🔢 予想番号の選択
predict_number = st.selectbox("🎯 登録する予想番号（①〜⑩）", list(range(1, 11)), format_func=lambda x: f"予想 {x}")

# 🏁 競艇場
race = st.selectbox("🏁 競艇場：", ["唐津", "若松", "住之江", "丸亀", "平和島", "福岡", "常滑", "芦屋", "尼崎", "津"])

# 📄 レース番号
race_no = st.selectbox("📄 レース番号（1〜12）", list(range(1, 13)))

# 📘 式別
style = st.selectbox("📘 式別：", ["単勝", "2連単", "3連単"])

# ✏️ 投票内容
vote = st.text_input("✏️ 投票内容：", value="")

# 💰 ECP方式賭け金（固定）
bet = 100
st.markdown(f"💰 自動賭け金（ECP方式）：<span style='color:green;'>{bet}円</span>", unsafe_allow_html=True)
st.info("この金額で登録されます")

# 🎯 結果（的中 or 不的中）
st.markdown("🎯 結果は？")
result = st.radio("結果を選択", ["的中", "不的中"])

# ✅ 登録ボタン
if st.button("✅ 登録する"):
    st.success(
        f"""✅ 登録完了！

🔢 予想番号：{predict_number}
🏁 競艇場：{race}（{race_no}R）
📘 式別：{style}
✏️ 投票内容：{vote}
💰 賭け金：{bet}円
🎯 結果：{result}
"""
    )
