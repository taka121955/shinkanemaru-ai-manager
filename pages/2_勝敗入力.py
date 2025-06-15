import streamlit as st

st.title("✍️ 勝敗入力フォーム")

# 候補リスト
競艇場リスト = ["住之江", "丸亀", "芦屋", "唐津", "蒲郡", "大村", "若松", "平和島", "戸田", "児島"]
式別リスト = ["3連単", "2連単", "単勝"]

# セッションから読み込み（あれば）
予想 = st.session_state.get("last_prediction", {})

st.markdown("### 🎯 AI予想をベースに入力")

col1, col2 = st.columns(2)

with col1:
    競艇場 = st.selectbox("競艇場", 競艇場リスト, index=競艇場リスト.index(予想.get("競艇場", 競艇場リスト[0])))

with col2:
    式別 = st.selectbox("式別", 式別リスト, index=式別リスト.index(予想.get("式別", 式別リスト[0])))

賭け内容 = st.text_input("賭け内容（例：1-3-4）", value=予想.get("内容", ""))

# ECPに基づく自動賭金（ここでは仮に100円固定）
賭金 = 100
st.markdown(f"💰 自動賭金（ECP方式）：**{賭金}円**")

if st.button("✅ 登録する"):
    st.success(f"登録完了：{競艇場}｜{式別}｜{賭け内容}｜{賭金}円")
