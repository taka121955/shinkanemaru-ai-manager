import streamlit as st
import pandas as pd
import os
from utils.calc_ecp import calculate_next_bet

def show():
    st.header("📊 統計データ")

    csv_file = "shinkanemaru_ai_manager/results.csv"

    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)

        total_bet = df["賭金"].sum()
        total_return = df["払戻"].sum()
        correct = df[df["的中"] == "的中"].shape[0]
        total = df.shape[0]

        accuracy = correct / total * 100 if total else 0
        win_rate = (df["収支"] > 0).mean() * 100 if total else 0
        recovery = total_return / total_bet * 100 if total_bet else 0

        next_bet = calculate_next_bet(df)

        st.markdown(f"""
        - 💼 現在の残高：{10000 + df['収支'].sum():.0f}円
        - 🎯 目標金額：20000円
        - 📄 累積損益：{df['収支'].sum():.0f}円
        - 🎯 的中率：{accuracy:.1f}%
        - 🏆 勝率：{win_rate:.1f}%
        - 💴 回収率：{recovery:.1f}%
        - 🧠 次回推奨 賭金（ECP方式）：{next_bet:.0f}円
        """)
    else:
        st.warning("まだデータが記録されていません。")
        
