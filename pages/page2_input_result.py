import streamlit as st
import pandas as pd

def show_page():
    st.markdown("## ② 勝敗入力")

    # 🔹 AI予想データの読み込み（ページ①で保存されたCSV）
    try:
        df = pd.read_csv("ai_predictions.csv")
        df["番号"] = df["番号"].astype(int)
    except Exception as e:
        st.error(f"❌ AI予想データの読み込みに失敗しました：{e}")
        return

    # 🔢 番号選択（ページ①と連動）
    selected_number = st.radio("🔢 番号を選択（ページ①と連動）", df["番号"].tolist())

    # 🔁 選択した番号の行を抽出
    row = df[df["番号"] == selected_number].iloc[0]

    # 🎯 自動反映フィールド
    venue = row["競艇場"]
    race_number = row["レース番号"]
    betting_type = row["式別"]
    betting_content = row["投票内容"]
    raw_accuracy = float(row["的中率"].replace("%", ""))
    estimated_odds = max(round(10.0 / raw_accuracy, 2), 1.5)  # 的中率 → オッズ換算（最低1.5）

    # 📋 入力フォーム（自動表示）
    st.text_input("🎡 競艇場名", value=venue, disabled=True)
    st.text_input("🏁 レース番号", value=race_number, disabled=True)
    st.text_input("🎫 式別", value=betting_type, disabled=True)
    st.text_input("📌 投票内容", value=betting_content, disabled=True)
    st.number_input("📈 オッズ（自動換算）", value=estimated_odds, step=0.1, disabled=True)

    # ✅ 勝敗選択
    win = st.radio("🎯 勝敗", ["的中", "不的中"])

    # 💴 自動ベット金額（簡略ECP方式）
    if estimated_odds >= 8.0:
        bet_amount = 300
    elif estimated_odds >= 5.0:
        bet_amount = 600
    else:
        bet_amount = 900

    st.markdown(f"💴 **自動ベット金額（第1波）**：  **:green[{bet_amount}円]**")

    if st.button("✅ 登録する"):
        st.success("✅ 勝敗結果を登録しました（※保存処理は未実装）")
