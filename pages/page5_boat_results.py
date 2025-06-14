import streamlit as st
from datetime import date

st.set_page_config(page_title="⑤ 競艇結果", layout="wide")

st.title("⛵ ⑤ 競艇結果")

st.info("⚙️ このページは現在準備中です。今後、公式結果データの自動取得・AI予想との比較分析などを実装予定です。")

st.markdown("---")

# 将来の機能見通し（表示だけ用意）
st.subheader("📅 対象日を選択")
selected_date = st.date_input("レース日", value=date.today())

st.subheader("📍 対象競艇場")
race_site = st.selectbox("競艇場を選択してください", [
    "住之江", "戸田", "浜名湖", "平和島", "大村", "児島", "徳山", "桐生", "唐津", "常滑"
])

st.subheader("📊 今後の機能予定")
st.markdown("""
- 公式サイトからの**レース結果取得**（スクレイピング/API）
- **AI予想との的中比較**（予想の精度確認）
- **レース動画へのリンク**
- **信頼度分析・傾向レポート**
""")
