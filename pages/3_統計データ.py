import streamlit as st
import pandas as pd

def show_page():
    st.markdown("### 📊 統計データ")
    st.markdown("ここでは、勝率・回収率・的中率などの成績統計を表示します。")

    try:
        df = pd.read_csv("results.csv")

        if df.empty:
            st.warning("データがありません。勝敗入力を先に行ってください。")
            return

        # 有効データのみ抽出
        df = df.dropna(subset=["勝敗", "金額"])
        df["金額"] = pd.to_numeric(df["金額"], errors="coerce")
        df = df.dropna(subset=["金額"])

        total_bets = len(df)
        total_wins = (df["勝敗"] == "◯").sum()
        total_spent = df["金額"].sum()
        total_return = df[df["勝敗"] == "◯"]["払戻金"].sum() if "払戻金" in df.columns else 0

        # 勝率・回収率・的中率を計算
        win_rate = total_wins / total_bets * 100 if total_bets else 0
        hit_rate = win_rate  # 同じ意味で使用されることが多いため
        payout_rate = total_return / total_spent * 100 if total_spent else 0

        st.metric("🎯 勝率", f"{win_rate:.1f}%")
        st.metric("💹 回収率", f"{payout_rate:.1f}%")
        st.metric("✅ 的中率", f"{hit_rate:.1f}%")
        st.write("---")

        # オプションでデータ表示
        if st.checkbox("📄 元データを表示する"):
            st.dataframe(df)

    except FileNotFoundError:
        st.error("results.csv が見つかりません。")
