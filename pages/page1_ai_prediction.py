import streamlit as st
import datetime
from utils.ai_prediction import generate_predictions

st.markdown("## ①AI予想")

# 日本時間表示
jst = datetime.timezone(datetime.timedelta(hours=9))
now = datetime.datetime.now(jst)
st.markdown(f"### 🕰️ 現在時刻（日本時間）： {now.strftime('%Y/%m/%d %H:%M:%S')}")

# 予想データ生成
predictions = generate_predictions()

# ✅ オッズの降順でソート（修正点）
predictions.sort(key=lambda x: x["オッズ"], reverse=True)

# 上位5件のみ表示
top_predictions = predictions[:5]

# 表示
st.markdown("### 🎯 AI予想（上位5件）")
st.table(top_predictions)

# ページ移動ボタン（下部）
st.markdown("---")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("①AI予想"):
        st.experimental_rerun()
with col2:
    if st.button("②勝敗入力"):
        st.switch_page("pages/page2_input_result.py")
with col3:
    if st.button("③統計データ"):
        st.switch_page("pages/page3_statistics.py")
with col4:
    if st.button("④結果履歴"):
        st.switch_page("pages/page4_record_result.py")
with col5:
    if st.button("⑤競艇結果"):
        st.switch_page("pages/page5_boat_results.py")
