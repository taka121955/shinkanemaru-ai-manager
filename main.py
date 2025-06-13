import streamlit as st
from datetime import datetime
import pytz

# ページ設定
st.set_page_config(page_title="競艇AI資金管理", layout="centered")

# --- ヘッダー部分（共通） ---
st.markdown("## 🕒 現在時刻（日本時間）")
jst_time = datetime.now(pytz.timezone('Asia/Tokyo'))
st.markdown(f"<h1 style='text-align: center; font-size: 36px;'>{jst_time.strftime('%Y/%m/%d %H:%M:%S')}</h1>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 🎯 目標金額：10000円")
st.markdown("### 💰 初期資金：10000円")

# 累積費用の仮表示（自動反映に後で対応）
cumulative_cost = 5000
st.markdown(f"### 📊 累積費用：{cumulative_cost}円")

# --- ページ切替ボタン（中央整列） ---
st.markdown("---")
col1, col2, col3, col4, col5 = st.columns(5)
page = None
if col1.button("① AI予想"):
    page = "ai"
elif col2.button("② 勝敗入力"):
    page = "input"
elif col3.button("③ 統計データ"):
    page = "stats"
elif col4.button("④ 勝敗履歴"):
    page = "history"
elif col5.button("⑤ 競艇結果"):
    page = "result"

st.markdown("---")

# --- 各ページ表示内容 ---
if page == "ai":
    st.markdown("## 🧠 AI予想ページ（ここにAI予想の内容を表示）")
elif page == "input":
    st.markdown("## ✍️ 勝敗入力ページ（ここに勝敗入力フォーム）")
elif page == "stats":
    st.markdown("## 📈 統計データページ（勝率・回収率など）")
elif page == "history":
    st.markdown("## 📜 勝敗履歴ページ（履歴の一覧）")
elif page == "result":
    st.markdown("## 🏁 競艇結果ページ（各レースの結果など）")
else:
    st.markdown("### ページを選択してください。")

# --- フッター ---
st.markdown("---")
st.markdown("#### 👤 制作者：小島崇彦")
