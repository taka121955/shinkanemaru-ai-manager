import streamlit as st
from utils.calc_ecp import calculate_next_bet
from datetime import datetime

def show_page():
    st.markdown("## 📝 勝敗入力")

    # 現在時刻表示（参考）
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    st.markdown(f"🕒 入力時刻：`{now}`")

    # 競艇場名（プルダウン）全場対応
    jyo = st.selectbox("🚤 競艇場名を選択", [
        "桐生", "戸田", "江戸川", "平和島", "多摩川",
        "浜名湖", "蒲郡", "常滑", "津",
        "三国", "びわこ", "住之江", "尼崎",
        "鳴門", "丸亀", "児島", "宮島", "徳山",
        "下関", "若松", "芦屋", "福岡", "唐津", "大村"
    ])

    # 式別（プルダウン）
    shikibetsu = st.selectbox("📘 式別を選択", ["単勝", "2連単", "3連単"])

    # 賭け内容（簡単な入力欄）
    bet_detail = st.text_input("🎯 賭け内容（例：1-2-3）")

    # オッズ入力（仮）
    odds = st.number_input("📈 オッズ（例：2.5）", min_value=1.0, step=0.1)

    # 勝敗履歴（仮：まだ未実装、空リスト）
    records = []

    # 賭金の自動計算（ECPロジック）
    bet_amount = calculate_next_bet(records, odds)

    # 表示
    st.markdown("---")
    st.success(f"💰 ECP方式による次回賭金額：`{int(bet_amount)}円`")
    st.caption("※履歴が記録されると自動で増減します（現在は仮値）")

    # 登録ボタン（今後CSV保存などに拡張可）
    if st.button("✅ この内容で登録（まだ保存は未実装）"):
        st.info("現在は表示のみです。保存機能は今後追加予定です。")
