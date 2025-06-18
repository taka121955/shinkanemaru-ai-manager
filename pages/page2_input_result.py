import streamlit as st
import pandas as pd

CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTOvDnRZFO5SRIubHRTYOfEovEtKD-JJUDT1aymSssv6I7Rh4Km4S4KpR4I0gAIzGE0XMcc8c3Edh-s/pub?gid=1462109758&single=true&output=csv"

def show_page():
    st.markdown("## ② 勝敗入力 ✍️")

    try:
        df = pd.read_csv(CSV_URL)
        df["番号"] = df["番号"].astype(int)
    except:
        st.error("❌ AI予想データの読み込みに失敗しました")
        return

    selected_number = st.radio("🔢 番号を選んで反映", df["番号"].tolist())

    # 選択行の取得
    selected_row = df[df["番号"] == selected_number].iloc[0]

    venue = selected_row["競艇場"]
    race = selected_row["レース番号"]
    style = selected_row["式別"]
    content = selected_row["投票内容"]
    acc = float(selected_row["的中率"].replace("%", ""))

    odds = round(100 / acc, 2)
    if odds < 1.5:
        odds = 1.5

    # 自動反映表示
    st.text_input("🎯 競艇場名", value=venue, disabled=True)
    st.text_input("🎯 レース番号", value=race, disabled=True)
    st.text_input("🎫 式別", value=style, disabled=True)
    st.text_input("📌 投票内容", value=content, disabled=True)
    st.number_input("📈 オッズ（自動計算）", value=odds, disabled=True)

    result = st.radio("🎯 勝敗", ["的中", "不的中"])

    # ベット金額は的中率から計算（例ロジック）
    if acc >= 85:
        bet = 100
    elif acc >= 75:
        bet = 300
    else:
        bet = 500

    st.markdown(f"💰 **AI指示ベット金額**：**:green[{bet}円]**")

    if st.button("✅ 登録する"):
        st.success("登録完了（※保存は未実装）")
