import streamlit as st
import json
import os

# 保存先ファイルパス
DATA_FILE = "utils/funds.json"

# 💾 保存関数
def save_funds(goal, reserve, saving):
    data = {
        "target": goal,
        "reserve": reserve,
        "savings": saving
    }
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 🔁 読み込み関数
def load_funds():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"target": 0, "reserve": 0, "savings": 0}

# 🎯 ページタイトル
st.set_page_config(page_title="資金設定", layout="centered")
st.markdown("<style>body { background-color: #fff9db; }</style>", unsafe_allow_html=True)

# 📊 現在値の読み込み
funds = load_funds()
st.markdown("## 💼 資金設定")
goal = st.number_input("🎯 目標金額", value=funds["target"], step=100)
reserve = st.number_input("💼 準備金額", value=funds["reserve"], step=100)
saving = st.number_input("📦 積立金額", value=funds["savings"], step=100)

# ✅ セットボタン
if st.button("💾 この内容でセットする", use_container_width=True):
    save_funds(goal, reserve, saving)
    st.success("✅ 資金データを保存しました！")
