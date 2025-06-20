import streamlit as st
import pandas as pd
import os

RESULTS_FILE = "results.csv"

def show_page():
    st.markdown("## ⑧ 今日の結果まとめ 📊")

    if not os.path.exists(RESULTS_FILE):
        st.warning("⚠️ 結果ファイルが見つかりません。")
        return

    df = pd.read_csv(RESULTS_FILE)

    if df.empty:
        st.info("📭 まだ記録がありません。")
        return

    # 列名が「競馬場」だった場合に自動で修正
    df.columns = [col.replace("競馬場", "競艇場") for col in df.columns]

    # 的中数（"結果"列が "的中" の数）をカウント
    summary = df.groupby("競艇場").agg({
        "結果": lambda x: (x == "的中").sum(),
        "払戻": "sum",
        "賭け金額": ["count", "sum"]
    })

    # 列名整理
    summary.columns = ["的中数", "回収金額", "購入数", "投資金額"]
    summary = summary.reset_index()

    # 回収率の計算
    summary["回収率"] = (summary["回収金額"] / summary["投資金額"] * 100).fillna(0).round(1).astype(str) + "%"

    # 列の順序を調整
    summary = summary[["競艇場", "的中数", "購入数", "回収金額", "投資金額", "回収率"]]

    # テーブル表示
    st.dataframe(summary, use_container_width=True)

    # 🎯 本日の集計
    total_hits = (df["結果"] == "的中").sum()
    total_bets = len(df)
    total_payout = df["払戻"].sum()
    total_invest = df["賭け金額"].sum()

    accuracy = round((total_hits / total_bets) * 100, 1) if total_bets else 0
    total_return_rate = round((total_payout / total_invest) * 100, 1) if total_invest else 0

    st.markdown("### 📌 本日の合計")
    st.markdown(f"- 🎯 総的中率：**{accuracy}%**")
    st.markdown(f"- 💰 合計回収金額：**{int(total_payout):,} 円**")
    st.markdown(f"- 💸 合計投資金額：**{int(total_invest):,} 円**")
    st.markdown(f"- 📈 トータル回収率：**{total_return_rate}%**")
