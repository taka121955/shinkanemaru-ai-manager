import streamlit as st
import pandas as pd
import os
from datetime import datetime
from utils.calc_ecp import calculate_next_bet

st.title("✍️ 勝敗入力フォーム")
st.markdown("🎯 **AI予想をベースに入力**")

# CSVファイル
csv_path = "results.csv"

# デフォルト資金と積立
initial_fund = st.sidebar.number_input("💰 現在残高", min_value=0, value=5000, step=100)
reserve_fund = st.sidebar.number_input("📦 積立金", min_value=0, value=0, step=100)

# データ読み込み（空対策）
if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
    df = pd.read_csv(csv_path)
    history = df.to_dict(orient="records")
else:
    df = pd.DataFrame(columns=["日付", "競艇場", "式別", "反省内容", "賭け金", "的中", "波", "ステップ"])
    history = []

# 競艇場・式別
race_name = st.selectbox("競艇場", ["住之江", "丸亀", "常滑", "福岡", "平和島", "若松", "児島", "芦屋", "蒲郡"])
bet_type = st.selectbox("式別", ["単勝", "複勝", "2連単", "3連単"])

# ECP方式でベット金額を計算
bet, wave, step, updated_reserve = calculate_next_bet(history, initial_fund, reserve_fund)

if bet is None:
    st.error("⚠️ 資金不足のためリセットが必要です。")
    st.warning("🔁 残高・積立金を初期状態に戻します。")
    st.stop()

# 入力欄
prediction = st.text_input("反省内容（例：1-3-4）")
st.markdown(f"💵 自動ハイハイ金（ECP方式）：　**{bet}円**")

# 的中チェック
hit = st.checkbox("🎯 的中した")

# 登録ボタン
if st.button("✅ 登録する"):
    new_data = {
        "日付": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "競艇場": race_name,
        "式別": bet_type,
        "反省内容": prediction,
        "賭け金": bet,
        "的中": hit,
        "波": wave,
        "ステップ": step,
    }
    df = df.append(new_data, ignore_index=True)
    df.to_csv(csv_path, index=False)
    st.success("📥 勝敗記録を登録しました！")
