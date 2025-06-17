# pages/page3_statistics.py

import streamlit as st
import pandas as pd

# ✅ ページタイトル（サイドバー名に反映）
st.set_page_config(page_title="③ 統計データ", layout="centered")

def show_page():
    st.title("📊 統計データ")

    st.markdown("#### 📈 勝敗・回収・的中などの統計を確認できます")

    # 仮の統計データ（本番では過去入力やCSVから計算）
    stats_data = {
        "項目": [
            "総ベット回数", "的中回数", "勝率", "的中率", 
            "総収支", "平均回収率", "最高配当的中", "AI予想精度"
        ],
        "値": [
            "40回", "23回", "70%", "85%",
            "+4,800円", "121%", "28.4倍", "78.2%"
        ]
    }

    df = pd.DataFrame(stats_data)

    # 表として表示
    st.table(df)

    st.markdown("---")
    st.markdown("※ これらの数値は今後、入力履歴やAI学習と連動してリアルタイム集計予定です。")
