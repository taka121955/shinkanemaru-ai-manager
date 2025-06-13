import streamlit as st
import pandas as pd
import os

# CSVファイルパス
CSV_PATH = "shinkanemaru_ai_manager/results.csv"

st.subheader("③ 統計データ")

# ファイルが存在しない場合の対応
if not os.path.exists(CSV_PATH):
    st.warning("まだ結果が入力されていません。")
else:
    df = pd.read_csv(CSV_PATH)

    if df.empty:
        st.info("まだデータがありません。")
    else:
        total_bets = len(df)
        total_hit = df["的中"].value_counts().get("◯", 0)
        total_amount = df["賭金"].sum()
        total_return = df["払戻"].sum()
        hit_rate = (total_hit / total_bets) * 100 if total_bets > 0 else 0
        recovery_rate = (total_return / total_amount) * 100 if total_amount > 0 else 0
        win_rate = ((total_return - total_amount) / total_amount) * 100 if total_amount > 0 else 0
        profit = total_return - total_amount

        # 表示
        col1, col2 = st.columns(2)
        with col1:
            st.metric("🎯 的中率", f"{hit_rate:.2f}%")
            st.metric("📈 回収率", f"{recovery_rate:.2f}%")
        with col2:
            st.metric("💸 総賭金", f"{int(total_amount)} 円")
            st.metric("💰 総払戻", f"{int(total_return)} 円")

        st.markdown("---")
        st.metric("📊 収支", f"{int(profit)} 円")
        st.metric("📉 勝率（利益率）", f"{win_rate:.2f}%")

        # 次回賭金計算（例：ECP方式ベース）
        st.markdown("---")
        st.subheader("🔮 次回賭金（ECP計算例）")
        if profit < 0:
            next_bet = abs(int(profit)) + 100  # 損失を取り戻す＋α
            st.write(f"損失補填のため、次回賭金の目安は **{next_bet} 円** です。")
        else:
            st.write("プラス収支のため、次回も同額 or 分散投資をおすすめします。")
