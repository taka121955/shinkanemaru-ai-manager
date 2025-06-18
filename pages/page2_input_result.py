import streamlit as st

def show_page():
    st.markdown("## ② 勝敗入力")

    # 入力項目
    venue = st.text_input("🏟️ 競艇場名（例：唐津）")
    race_number = st.text_input("🎯 レース番号（例：1R）")
    win = st.radio("🎯 勝敗", ["的中", "不的中"], horizontal=True)
    odds = st.number_input("📈 オッズ", min_value=1.0, max_value=100.0, value=1.5, step=0.1)

    # 資金モード
    st.markdown("💰 **ベット金額（ECP方式で自動計算）**")
    fund_mode = st.radio("📦 資金モード", ["1300円", "3900円", "10000円"], horizontal=True)

    # ECPマップ（第1波金額）
    ecp_map = {
        "1300円": 100,
        "3900円": 300,
        "10000円": 1300
    }

    st.markdown("---")
    if fund_mode in ecp_map:
        amount = ecp_map[fund_mode]
        st.markdown(f"🧮 **自動ベット金額（第1波）**：<span style='color:green; font-size:24px; font-weight:bold;'>{amount} 円</span>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ 資金モードを選択してください。")

    # 登録ボタン
    if st.button("✅ 登録する"):
        st.success("✅ 登録が完了しました（※保存処理は未実装）")

# 最後に呼び出し
show_page()
