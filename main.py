import streamlit as st
import datetime
import json
import os
import pandas as pd

# 📁 ファイルパス
FUNDS_FILE = "utils/funds.json"
RESULTS_FILE = "results.csv"

# 🔄 資金データの読み込み
def load_funds():
    if os.path.exists(FUNDS_FILE):
        with open(FUNDS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"target": 0, "reserve": 0, "savings": 0}

# 📊 統計データの読み込み
def calculate_statistics():
    if os.path.exists(RESULTS_FILE):
        df = pd.read_csv(RESULTS_FILE)
        total = len(df)
        wins = len(df[df["結果"] == "的中"])
        total_bet = df["賭け金"].sum()
        total_return = df["払戻"].sum()
        if total == 0:
            return 0.0, 0.0, 0.0
        win_rate = wins / total * 100
        hit_rate = wins / total * 100
        recovery = (total_return / total_bet) * 100 if total_bet > 0 else 0
        return round(win_rate, 1), round(hit_rate, 1), round(recovery, 1)
    else:
        return 0.0, 0.0, 0.0

# ✅ データ取得
funds = load_funds()
win_rate, hit_rate, recovery = calculate_statistics()

# 🌐 ページ構成
st.set_page_config(page_title="資金マネージャー", layout="centered")
st.markdown("<style>body { background-color: #fff9db; }</style>", unsafe_allow_html=True)

# 💰 資金状況と統計データ（左右表示）
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"🎯 目標金額：<span style='color:blue; font-size:20px;'>{funds['target']:,}円</span>", unsafe_allow_html=True)
    st.markdown(f"💼 準備金額：<span style='color:green; font-size:20px;'>{funds['reserve']:,}円</span>", unsafe_allow_html=True)
    st.markdown(f"📦 積立金額：<span style='color:orange; font-size:20px;'>{funds['savings']:,}円</span>", unsafe_allow_html=True)
with col2:
    st.markdown(f"🏆 勝率：<span style='color:blue; font-size:20px;'>{win_rate:.1f}%</span>", unsafe_allow_html=True)
    st.markdown(f"🎯 的中率：<span style='color:green; font-size:20px;'>{hit_rate:.1f}%</span>", unsafe_allow_html=True)
    st.markdown(f"💹 回収率：<span style='color:orange; font-size:20px;'>{recovery:.1f}%</span>", unsafe_allow_html=True)

# ⏰ 現在時刻（中央表示）
japan_time = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
st.markdown(
    f"<div style='text-align:center; font-size:22px; font-weight:bold;'>⏰ 現在時刻：<span style='color:#007f00;'>{japan_time.strftime('%Y/%m/%d %H:%M:%S')}</span></div>",
    unsafe_allow_html=True
)

# 📂 メニュー（ボタン式）
st.markdown("### 📁 メニュー")
menu = ["①AI予想", "②勝敗入力", "③統計データ", "④結果履歴", "⑤競艇結果", "⑥資金設定"]
for item in menu:
    st.button(item, use_container_width=True)

# 🖊 制作者名
st.markdown("---")
st.markdown("#### 制作：小島崇彦")
