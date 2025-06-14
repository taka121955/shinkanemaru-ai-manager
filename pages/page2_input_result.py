import streamlit as st
from datetime import datetime

st.title("② 勝敗入力ページ")

# 初期化
if "input_history" not in st.session_state:
    st.session_state.input_history = []

# 選択肢定義
race_list = [f"{i}R" for i in range(1, 13)]
boat_places = [
    "住之江", "尼崎", "多摩川", "浜名湖", "児島", "丸亀", "若松",
    "蒲郡", "大村", "唐津", "芦屋", "戸田", "江戸川", "常滑", "津"
]

# 入力フォーム
with st.form("result_form"):
    col1, col2 = st.columns(2)
    with col1:
        date = st.date_input("📅 日付", value=datetime.now().date())
        race = st.selectbox("🏁 レース番号", race_list)
        bet_amount = st.number_input("💰 賭け金（円）", min_value=0, step=100)
    with col2:
        place = st.selectbox("🚤 競艇場名", boat_places)
        odds = st.number_input("📈 オッズ（例：3.5）", min_value=0.0, format="%.2f")

    submitted = st.form_submit_button("✅ 記録する")

    if submitted:
        if bet_amount > 0 and odds > 0:
            refund = round(bet_amount * odds)
            st.session_state.input_history.append({
                "日付": date.strftime("%Y/%m/%d"),
                "競艇場": place,
                "レース": race,
                "賭金": bet_amount,
                "オッズ": odds,
                "払戻金": refund
            })
            st.success(f"{place} {race} の結果を記録しました！")
        else:
            st.error("賭け金とオッズは0以上で入力してください。")

# 入力履歴
if st.session_state.input_history:
    st.markdown("### 📊 記録一覧")
    st.dataframe(st.session_state.input_history, use_container_width=True)
else:
    st.info("まだ記録がありません。")
