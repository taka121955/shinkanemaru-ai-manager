import streamlit as st
import pandas as pd

def show_page():
    st.markdown("## ⑧ 今日の結果まとめ 📊")

    # 仮の本日成績データ（手動 or 自動連携予定）
    data = {
        "競馬場": ["東京", "京都", "阪神", "中山"],
        "的中数": [2, 1, 3, 0],
        "購入数": [3, 2, 4, 2],
        "回収金額": [3200, 1500, 4800, 0],
        "投資金額": [3000, 2000, 4000, 1500],
        "回収率": ["107%", "75%", "120%", "0%"]
    }

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    st.markdown("### 📌 本日の合計")
    total_recover = sum(df["回収金額"])
    total_invest = sum(df["投資金額"])
    total_rate = f"{round(total_recover / total_invest * 100)}%" if total_invest else "0%"

    st.markdown(f"- 🎯 総的中率： {round(df['的中数'].sum() / df['購入数'].sum() * 100)}%")
    st.markdown(f"- 💰 合計回収金額： {total_recover} 円")
    st.markdown(f"- 💸 合計投資金額： {total_invest} 円")
    st.markdown(f"- 📈 トータル回収率： {total_rate}")
