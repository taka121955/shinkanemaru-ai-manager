import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
from utils.calc_ecp import calculate_ecp_amount  # 正しい相対パスに注意

def get_japan_time():
    jst = pytz.timezone("Asia/Tokyo")
    return datetime.now(jst).strftime("%Y/%m/%d %H:%M:%S")

def show_page():
    st.set_page_config(page_title="② 勝敗入力", layout="centered")
    st.title("② 勝敗入力")

    now = get_japan_time()
    st.markdown(f"🕒 現在時刻（日本時間）： `{now}`")

    st.subheader("🎲 勝敗結果の入力")

    # 選択肢
    venue = st.selectbox("競艇場", ["唐津", "住之江", "若松", "丸亀", "児島"])
    race_no = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
    result = st.radio("結果", ["的中", "外れ"])

    # ECP計算金額の表示
    amount = calculate_ecp_amount(result_type=result)
    st.success(f"💰 次回の自動賭け金額（ECP）: {amount}円")

    if st.button("記録する"):
        st.info("✅ 勝敗データを保存しました（仮機能）")
