import streamlit as st
import pandas as pd
from datetime import datetime
import os
import sys

# 🔧 utils フォルダの calc_ecp を読み込むためのパス追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
from calc_ecp import calculate_ecp_amount

def show_page():
    st.set_page_config(page_title="② 勝敗入力", layout="centered")
    st.title("② 勝敗入力")

    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    st.markdown(f"🕒 現在時刻（日本時間）： `{now}`")

    st.markdown("### 🎯 勝敗結果を入力")

    # 勝敗データの入力欄
    number = st.selectbox("番号（AI予想の番号）", list(range(1, 11)))
    result = st.radio("結果", ["的中", "外れ"])
    wave = st.selectbox("波（第何波）", [1, 2, 3])

    # 金丸法ECPによる金額の自動計算
    try:
        amount = calculate_ecp_amount(wave)
        st.success(f"💰 金額（自動計算）：{amount:,}円")
    except Exception as e:
        st.error(f"金額の計算に失敗しました：{e}")
        amount = 0

    # 登録ボタン
    if st.button("✅ 登録"):
        new_data = {
            "時刻": now,
            "番号": number,
            "結果": result,
            "波": wave,
            "金額": amount
        }

        try:
            csv_path = "results.csv"
            if os.path.exists(csv_path):
                df = pd.read_csv(csv_path)
                df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            else:
                df = pd.DataFrame([new_data])

            df.to_csv(csv_path, index=False)
            st.success("記録しました！")
        except Exception as e:
            st.error(f"保存に失敗しました：{e}")

# 呼び出し
show_page()
