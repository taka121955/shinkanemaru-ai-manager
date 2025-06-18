import streamlit as st
import pandas as pd

CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTOvDnRZFO5SRIubHRTYOfEovEtKD-JJUDT1aymSssv6I7Rh4Km4S4KpR4I0gAIzGE0XMcc8c3Edh-s/pub?gid=1462109758&single=true&output=csv"

def show_page():
    st.markdown("## ② 勝敗入力")

    try:
        df = pd.read_csv(CSV_URL)
        df["番号"] = df["番号"].astype(int)
    except Exception as e:
        st.error("❌ AI予想データの読み込みに失敗しました")
        return

    # 🔢 番号選択
    selected_number = st.radio("🔢 番号を選択（ページ①と連動）", df["番号"].tolist())

    # 対応する行を抽出
    row = df[df["番号"] == selected_number].iloc[0]

    # 自動反映データ
    venue = row["競艇場"]
    race_number = row["レース番号"]
    betting_type = row["式別"]
    betting_content = row["投票内容"]
    accuracy = float(row["的中率"].replace("%", ""))
    odds = max(round(10 / accuracy, 2), 1.5)

    # フォーム表示（自動反映）
    st.text_input("🎡 競艇場名", value=venue, disabled=True)
    st.text_input("🏁 レース番号", value=race_number, disabled=True)
    st.text_input("🎫 式別", value=betting_type, disabled=True)
    st.text_input("📌 投票内容", value=betting_content, disabled=True)
    st.number_input("📈 オッズ（自動計算）", value=odds, step=0.1, disabled=True)

    # 勝敗選択
    result = st.radio("🎯 勝敗", ["的中", "不的中"])

    # ベット金額を自動算出（簡易ロジック）
    if odds >= 8.0:
        bet = 300
    elif odds >= 5.0:
        bet = 600
    else:
        bet = 900

    st.markdown(f"💴 **自動ベット金額（AI指示）**： **:green[{bet}円]**")

    if st.button("✅ 登録する"):
        st.success("✅ 勝敗結果を登録しました（※保存処理は未実装）")
