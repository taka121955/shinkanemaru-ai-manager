import streamlit as st
import pandas as pd
from datetime import datetime
from utils.calc_ecp import calculate_ecp_amount  # 修正済みのインポート

def show_page():
    st.set_page_config(page_title="② 勝敗入力", layout="centered")
    st.title("② 勝敗入力")

    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    st.markdown(f"🕒 現在時刻（日本時間）： `{now}`")

    st.markdown("---")
    st.markdown("### 🎯 対象レースを選択して結果を入力してください")

    # 仮のAI予想データ（①ページのトップ10と連携する前提）
    predictions = [
        {"番号": 1, "競艇場": "唐津", "レース": "1R", "式別": "2連単", "内容": "5-2", "的中率": "89%"},
        {"番号": 2, "競艇場": "住之江", "レース": "3R", "式別": "3連単", "内容": "6-3-3", "的中率": "82%"},
        {"番号": 3, "競艇場": "若松", "レース": "2R", "式別": "2連単", "内容": "1-6", "的中率": "70%"},
    ]

    options = [f"{p['番号']}: {p['競艇場']} {p['レース']} {p['内容']}" for p in predictions]
    selected = st.selectbox("🎯 番号を選択", options)

    if selected:
        selected_index = int(selected.split(":")[0]) - 1
        target = predictions[selected_index]

        st.write(f"### 対象：{target['競艇場']} {target['レース']}（{target['内容']}）")

        result = st.radio("🎲 結果", ["的中", "不的中", "未実施"], horizontal=True)

        if result in ["的中", "不的中"]:
            # 金丸法×ECPの自動金額指示
            auto_amount = calculate_ecp_amount(result == "的中", previous_losses=0)
            st.success(f"💰 自動指示金額：{auto_amount} 円")

        if st.button("✅ 登録する"):
            st.success("結果を保存しました（※データベース接続は仮）")

# 呼び出し
show_page()
