import streamlit as st
from datetime import datetime
from utils.ai_prediction import generate_predictions

st.markdown("### ①AI予想")
st.markdown(f"🕰️ **現在時刻（日本時間）** ： `{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}`")

# 予想データの取得（例：AIが生成）
predictions = generate_predictions()

# 並び替え（エラー対策）
if predictions and "オッズ" in predictions[0]:
    predictions.sort(key=lambda x: x["オッズ"])

# 表示
if predictions:
    st.markdown("🎯 **AI予想（上位5件）**")
    st.table(predictions[:5])
else:
    st.warning("予想データが見つかりません")

# ページ切替ボタン
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("① AI予想"):
        st.query_params["page"] = "page1_ai_prediction"
with col2:
    if st.button("② 勝敗入力"):
        st.query_params["page"] = "page2_input_result"
with col3:
    if st.button("③ 統計データ"):
        st.query_params["page"] = "page3_statistics"
with col4:
    if st.button("④ 結果履歴"):
        st.query_params["page"] = "page4_record_result"
