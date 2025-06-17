# pages/page2_input_result.py

import streamlit as st
import pandas as pd
from datetime import datetime

# ✅ ページタイトル設定（サイドバー名に反映）
st.set_page_config(page_title="② 勝敗入力", layout="centered")

def show_page():
    st.title("📝 勝敗結果の入力")

    st.markdown("#### 📅 レース結果を入力してください")

    # 入力フォーム
    with st.form("result_form"):
        race_date = st.date_input("開催日", value=datetime.today())
        place = st.selectbox("競艇場", ["蒲郡", "住之江", "戸田", "丸亀", "芦屋", "宮島"])
        race_no = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
        prediction = st.text_input("予想した舟券（例：1-2-3）")
        result = st.text_input("実際の結果（例：1-2-3）")
        amount = st.number_input("賭け金額（円）", min_value=0, step=100)
        is_hit = st.radio("的中しましたか？", ["的中", "外れ"])
        submitted = st.form_submit_button("✅ 登録する")

    # 登録結果を表示（データ保存処理は後ほど拡張可能）
    if submitted:
        st.success("🎉 登録が完了しました！")
        st.markdown("---")
        st.markdown("#### 登録内容（確認）")
        st.write({
            "日付": race_date.strftime("%Y-%m-%d"),
            "競艇場": place,
            "レース": race_no,
            "予想": prediction,
            "結果": result,
            "金額": f"{amount:,}円",
            "的中": is_hit
        })
