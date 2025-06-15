import streamlit as st
import pandas as pd
from datetime import datetime
from utils.calc_ecp import calculate_ecp_amount  # ECP関数を読み込み

st.markdown("### ✍️ 勝敗入力")

# --- 競艇場リスト（全国24場） ---
boat_places = [
    "桐生", "戸田", "江戸川", "平和島", "多摩川", "浜名湖", "蒲郡", "常滑", "津", "三国",
    "びわこ", "住之江", "尼崎", "鳴門", "丸亀", "児島", "宮島", "徳山", "下関", "若松",
    "芦屋", "福岡", "唐津", "大村"
]

# --- 式別リスト ---
bet_types = ["単勝", "複勝", "2連複", "2連単", "3連複", "3連単"]

# --- 入力フォーム ---
with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        place = st.selectbox("競艇場", boat_places)
        race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
        bet_type = st.selectbox("式別", bet_types)

    with col2:
        # シンプルな賭け内容生成（最大3つまで選択）
        st.markdown("##### 賭け内容（艇番号）")
        num1 = st.selectbox("1着", range(1, 7))
        num2 = st.selectbox("2着", range(1, 7))
        num3 = st.selectbox("3着", range(1, 7))
        if bet_type in ["3連単", "3連複"]:
            bet = f"{num1}-{num2}-{num3}"
        elif bet_type in ["2連単", "2連複"]:
            bet = f"{num1}-{num2}"
        else:
            bet = f"{num1}"

        result = st.radio("結果", ["的中", "外れ"])
        payout = st.number_input("払戻金額（的中時のみ）", min_value=0, step=100)

    # --- ECP方式による賭け金の自動提案 ---
    amount = calculate_ecp_amount()  # ECP方式で金額取得
    st.info(f"💴 本日の推奨賭け金（ECP方式）：{amount:,}円")

    submitted = st.form_submit_button("✅ 記録する")

# --- 保存処理 ---
if submitted:
    new_row = {
        "日時": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "競艇場": place,
        "レース": race,
        "式別": bet_type,
        "賭け内容": bet,
        "賭け金額": amount,
        "結果": result,
        "払戻金額": payout if result == "的中" else 0
    }

    try:
        df = pd.read_csv("results.csv")
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    except:
        df = pd.DataFrame([new_row])

    df.to_csv("results.csv", index=False)
    st.success("✅ 記録が保存されました！")

    with st.expander("📋 最新の入力内容"):
        st.write(pd.DataFrame([new_row]))
