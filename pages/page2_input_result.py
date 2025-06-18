import streamlit as st
import pandas as pd
from datetime import datetime
import os
import sys

# ✅ utils ディレクトリをパスに追加
current_dir = os.path.dirname(os.path.abspath(__file__))
utils_path = os.path.abspath(os.path.join(current_dir, "..", "utils"))
if utils_path not in sys.path:
    sys.path.append(utils_path)

# ✅ calc_ecp から関数を正しくインポート
from calc_ecp import calculate_ecp_amount

def show_page():
    st.set_page_config(page_title="② 勝敗入力", layout="centered")
    st.title("② 勝敗入力")

    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    st.markdown(f"🕒 現在時刻（日本時間）： `{now}`")

    st.markdown("### 🎯 勝敗結果を入力")

    number = st.selectbox("番号（AI予想の番号）", list(range(1, 11)))
    result = st.radio("結果", ["的中", "外れ"])
    wave = st.selectbox("波（第何波）", [1, 2, 3])

    try:
        amount = calculate_ecp_amount(wave)
        st.success(f"💰 金額（自動計算）：{amount:,}円")
    except Exception as e:
        st.error(f"金額の計算に失敗しました：{e}")
        amount = 0

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
            st.success("✅ 記録しました")
        except Exception as e:
            st.error(f"保存エラー：{e}")

show_page()
