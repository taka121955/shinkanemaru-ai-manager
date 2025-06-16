import streamlit as st

st.markdown("## 📝 勝敗入力フォーム")
st.markdown("🎯 登録する予想番号　（①〜⑩）")
predict_number = st.selectbox("①", list(range(1, 11)))

# 競艇場
race_list = ["唐津", "若松", "住之江", "丸亀", "平和島", "福岡", "常滑", "芦屋", "尼崎", "津"]
race = st.selectbox("🏁 競艇場：", race_list)

# レース番号（新規追加）
race_no = st.selectbox("📄 レース番号（1〜12）：", list(range(1, 13)))

# 式別
style = st.selectbox("📘 式別：", ["単勝", "2連単", "3連単"])

# 投票内容
vote = st.text_input("✏️ 投票内容：", value="")

# 賭け金（ECP方式で100円固定）
st.markdown("💰 自動賭け金（ECP方式）：<span style='color:green;'>100円</span>", unsafe_allow_html=True)
st.info("この金額で登録されます")

# 的中／不的中
st.markdown("🎯 結果は？")
result = st.radio("", ["🎯 的中", "⭕ 不的中"])

# 登録ボタン
if st.button("✅ 登録する"):
    st.success(f"予想{predict_number} を登録しました：{race} {race_no}R / {style} / {vote} / {result}")
