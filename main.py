import streamlit as st
import datetime
import json
import os
import pandas as pd

# ページ設定と背景色
st.set_page_config(page_title="資金マネージャー", layout="centered")
st.markdown("<style>body { background-color: #fff9db; }</style>", unsafe_allow_html=True)

# 📂 結果CSVパス
RESULTS_FILE = "results.csv"

# 🔄 資金データの読み込み
def load_funds():
    if os.path.exists("utils/funds.json"):
        with open("utils/funds.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {"target": 0, "reserve": 0, "savings": 0}

# 📊 成績データの集計
def calculate_stats():
    if not os.path.exists(RESULTS_FILE) or os.path.getsize(RESULTS_FILE) == 0:
        return 0, 0, 0

    df = pd.read_csv(RESULTS_FILE)
    total = len(df)
    if total == 0:
        return 0, 0, 0

    wins = df[df["結果"] == "的中"]
    win_rate = round(len(wins) / total * 100, 1)
    hit_rate = round(df["的中率"].astype(str).str.replace('%', '').astype(float).mean(), 1)
    recovery = round(wins["払戻"].sum() / df["賭け金"].sum() * 100, 1) if df["賭け金"].sum() > 0 else 0
    return win_rate, hit_rate, recovery

funds = load_funds()
win_rate, hit_rate, recovery = calculate_stats()

# 💰 現在の資金状況と成績表示（2列構成）
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"<h3>🎯 目標金額：<span style='color:blue;'>{funds['target']:,}円</span></h3>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<h3>🏆 勝率：<span style='color:blue;'>{win_rate}%</span></h3>", unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    st.markdown(f"<h3>💼 準備金額：<span style='color:green;'>{funds['reserve']:,}円</span></h3>", unsafe_allow_html=True)
with col4:
    st.markdown(f"<h3>🎯 的中率：<span style='color:green;'>{hit_rate}%</span></h3>", unsafe_allow_html=True)

col5, col6 = st.columns(2)
with col5:
    st.markdown(f"<h3>📦 積立金額：<span style='color:orange;'>{funds['savings']:,}円</span></h3>", unsafe_allow_html=True)
with col6:
    st.markdown(f"<h3>💹 回収率：<span style='color:orange;'>{recovery}%</span></h3>", unsafe_allow_html=True)

# ⏰ 現在時刻（日本時間）
japan_time = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
st.markdown(
    f"<div style='text-align:center; font-size:24px; font-weight:bold;'>⏰ 現在時刻：<span style='color:#007f00;'>{japan_time.strftime('%Y/%m/%d %H:%M:%S')}</span></div>",
    unsafe_allow_html=True
)

# 📂 メニュー（表示専用）
st.markdown("### 📁 メニュー")
st.button("①AI予想", use_container_width=True)
st.button("②勝敗入力", use_container_width=True)
st.button("③統計データ", use_container_width=True)
st.button("④結果履歴", use_container_width=True)
st.button("⑤競艇結果", use_container_width=True)
st.button("⑥資金設定", use_container_width=True)

# 📌 制作者表記
st.markdown("---")
st.markdown("#### 制作：小島崇彦")
