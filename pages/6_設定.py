# 📄 pages/page6_funds_setting.py
import streamlit as st
import json
import os

DATA_FILE = "funds_data.json"

def save_funds(goal, reserve, saving):
    data = {
        "目標金額": goal,
        "準備金額": reserve,
        "積立金額": saving
    }
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_funds():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"目標金額": 0, "準備金額": 0, "積立金額": 0}

def show_page():
    st.markdown("### 💰 資金設定ページ")

    current = load_funds()

    st.markdown("#### 🎯 現在の設定")
    st.markdown(f"- 🎯 目標金額：**{current['目標金額']:,}円**")
    st.markdown(f"- 💼 準備金額：**{current['準備金額']:,}円**")
    st.markdown(f"- 📦 積立金額：**{current['積立金額']:,}円**")

    st.markdown("---")
    st.markdown("#### ✍️ 新しく設定する")

    goal = st.number_input("🎯 目標金額を入力", value=current['目標金額'], step=1000)
    reserve = st.number_input("💼 準備金額を入力", value=current['準備金額'], step=1000)
    saving = st.number_input("📦 積立金額を入力", value=current['積立金額'], step=1000)

    if st.button("✅ セットする"):
        save_funds(goal, reserve, saving)
        st.success("✅ 資金情報を更新しました！")
