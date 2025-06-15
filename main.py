import streamlit as st
from datetime import datetime

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide", initial_sidebar_state="collapsed")

# 現在時刻
jst = datetime.utcnow().astimezone()
st.markdown(f"<h3 style='text-align: center;'>🕒 現在時刻（日本時間）：{jst.strftime('%Y/%m/%d %H:%M:%S')}</h3>", unsafe_allow_html=True)

# タイトル
st.markdown("""
<div style='text-align: center; font-size: 24px; font-weight: bold;'>💼 新金丸法 × AI資金マネージャー</div>
""", unsafe_allow_html=True)

# 機能案内
st.markdown("""
### 📘 このアプリの使い方
- 左の「ページ」から各機能へ移動できます
- ①〜⑥の予測・入力・集計が使えます
- このトップページはメイン用です
""")

# フッター
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
