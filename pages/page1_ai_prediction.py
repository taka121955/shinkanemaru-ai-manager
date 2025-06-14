import streamlit as st
from datetime import datetime
from utils.ai_prediction import generate_predictions

st.markdown("### ①AI予想")

# 現在時刻（日本時間）
japan_time = datetime.utcnow().timestamp() + 9 * 60 * 60
now = datetime.fromtimestamp(japan_time).strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"🕰 **現在時刻（日本時間）** ： `{now}`")

st.markdown("🎯 **AI予想（上位5件）**")

# 予想取得
predictions = generate_predictions()

# ✅ 「確率」順に並べ替え
predictions.sort(key=lambda x: x["確率"], reverse=True)

# 表形式で表示
st.table(predictions[:5])

# ナビゲーションボタン
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("① AI予想"):
        st.experimental_set_query_params(page="page1_ai_prediction")
with col2:
    if st.button("② 勝敗入力"):
        st.experimental_set_query_params(page="page2_input_result")
with col3:
    if st.button("③ 統計データ"):
        st.experimental_set_query_params(page="page3_statistics")
with col4:
    if st.button("④ 結果履歴"):
        st.experimental_set_query_params(page="page4_record_result")
