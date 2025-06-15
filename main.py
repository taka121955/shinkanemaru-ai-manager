import streamlit as st
import datetime
import os
import json

# ページ設定と背景色
st.set_page_config(page_title="資金マネージャー", layout="centered")
st.markdown("<style>body { background-color: #fff9db; }</style>", unsafe_allow_html=True)

# ⏰ 現在時刻の表示（中央・太字・日本時間）
japan_time = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
st.markdown(f"<h4 style='text-align: center;'>⏰ <span style='color: green;'>現在時刻：{japan_time.strftime('%Y/%m/%d %H:%M:%S')}</span></h4>", unsafe_allow_html=True)

# 🗂️ メニュー表示（3×2配置）
st.markdown("### 📁 メニュー（表示専用）")
col1, col2 = st.columns(2)

with col1:
    st.button("①AI予想", use_container_width=True)
    st.button("③統計データ", use_container_width=True)
    st.button("⑤競艇結果", use_container_width=True)

with col2:
    st.button("②勝敗入力", use_container_width=True)
    st.button("④結果履歴", use_container_width=True)
    st.button("⑥資金設定", use_container_width=True)

# 📂 資金データ読み込み
def load_funds():
    if os.path.exists("utils/funds.json"):
        with open("utils/funds.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {"target": 0, "reserve": 0, "savings": 0}

funds = load_funds()

# 💰 現在の資金状況
st.markdown("---")
st.markdown("### 💰 現在の資金状況")
st.markdown(f"🎯 <b>目標金額：</b> <span style='color:blue;'>{funds['target']:,}円</span>", unsafe_allow_html=True)
st.markdown(f"💼 <b>準備金額：</b> <span style='color:green;'>{funds['reserve']:,}円</span>", unsafe_allow_html=True)
st.markdown(f"📦 <b>積立金額：</b> <span style='color:orange;'>{funds['savings']:,}円</span>", unsafe_allow_html=True)

# 🖋️ 制作者情報
st.markdown("---")
st.markdown("#### 制作：小島崇彦")
