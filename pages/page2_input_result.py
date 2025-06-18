import streamlit as st
from utils.calc_ecp import calculate_ecp_amount

def show_page():
    st.markdown("## ② 勝敗入力")

    # 入力項目
    venue = st.text_input("🎯 競艇場名（例：唐津）")
    race_number = st.text_input("🎯 レース番号（例：1R）")

    win = st.radio("勝敗", ["的中", "不的中"])
    odds = st.number_input("オッズ", min_value=1.0, max_value=100.0, value=1.5, step=0.1)

    st.markdown("💰 **ベット金額（ECP方式で自動計算）**")

    fund_mode = st.radio("資金モード", ["1300円", "3900円", "10000円"])

    # 自動金額計算（第1波のみ表示）
    ecp_map = {
        "1300円": [100, 300, 900],
        "3900円": [300, 900, 2700],
        "10000円": [1300, 2600, 6100]
    }

    if fund_mode in ecp_map:
        try:
            amount = ecp_map[fund_mode][0]  # 第1波のみ
            st.markdown(f"🧮 **自動ベット金額（AI指示）**  \n 👉 指示金額：**:green[{amount}円]**（ECP第1波）")
        except Exception as e:
            st.error("ベット金額の計算に失敗しました。")
    else:
        st.warning("資金モードを選択してください。")

    if st.button("登録する"):
        st.success("✅ 登録が完了しました（※保存処理は未実装）")
