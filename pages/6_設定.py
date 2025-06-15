import streamlit as st
import os
import json

funds_file = "utils/funds.json"

# 初期化用のデフォルト値
default_funds = {"target": 0, "reserve": 0, "savings": 0}

# 保存関数
def save_funds(data):
    os.makedirs("utils", exist_ok=True)
    with open(funds_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 読み込み関数
def load_funds():
    if os.path.exists(funds_file):
        with open(funds_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return default_funds

# ページタイトル
st.title("⑥ 資金設定")

# 現在の資金情報を読み込み
funds = load_funds()

# フォーム
with st.form("fund_settings_form"):
    target = st.number_input("🎯 目標金額", min_value=0, value=funds["target"], step=1000)
    reserve = st.number_input("💼 準備金額", min_value=0, value=funds["reserve"], step=1000)
    savings = st.number_input("📦 積立金額", min_value=0, value=funds["savings"], step=1000)
    submitted = st.form_submit_button("💾 セットする")
    if submitted:
        new_data = {"target": target, "reserve": reserve, "savings": savings}
        save_funds(new_data)
        st.success("✅ 資金情報を保存しました！")

# 🔴 クリアボタン（資金データ初期化）
if st.button("🧹 資金情報をクリア（リセット）", type="primary"):
    save_funds(default_funds)
    st.warning("⚠️ 資金情報を初期化しました。")
