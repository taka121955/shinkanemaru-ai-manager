import streamlit as st
import datetime
import json
import os

# ページ設定と背景色
st.set_page_config(page_title="資金マネージャー", layout="centered")
st.markdown("<style>body { background-color: #fff9db; }</style>", unsafe_allow_html=True)

# 🔄 資金データの読み込み
def load_funds():
    if os.path.exists("utils/funds.json"):
        with open("utils/funds.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {"target": 0, "reserve": 0, "savings": 0}

funds = load_funds()

# 💰 現在の資金状況（最上部、大きく）
st.markdown("### 💰 <b>現在の資金状況</b>", unsafe_allow_html=True)
st.markdown(f"<h4>🎯 目標金額：<span style='color:blue;'>{funds['target']:,}円</span></h4>", unsafe_allow_html=True)
st.markdown(f"<h4>💼 準備金額：<span style='color:green;'>{funds['reserve']:,}円</span></h4>", unsafe_allow_html=True)
st.markdown(f"<h4>📦 積立金額：<span style='color:orange;'>{funds['savings']:,}円</span></h4>", unsafe_allow_html=True)

# ⏰ 現在時刻
japan_time = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
st.markdown(f"<p style='text-align: center; font-size:18px;'>⏰ 現在時刻：<span style='color:green;'>{japan_time.strftime('%Y/%m/%d %H:%M:%S')}</span></p>", unsafe_allow_html=True)

# 📂 メニュー項目
st.markdown("### 📁 メニュー（表示専用）")
st.button("①AI予想", use_container_width=True)
st.button("②勝敗入力", use_container_width=True)
st.button("③統計データ", use_container_width=True)
st.button("④結果履歴", use_container_width=True)
st.button("⑤競艇結果", use_container_width=True)
st.button("⑥資金設定", use_container_width=True)

# 📌 制作者表記
st.markdown("---")
st.markdown("#### 制作：小島崇彦")
