import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="📝 勝敗入力", layout="wide")
st.title("📝 勝敗入力フォーム（エクセル風 UI）")

# 仮のAI予想データ（今後は自動生成に置換可能）
data = [
    {"No": i+1, "競艇場":場, "レース":r, "式別":s, "投票":t, "的中率":p, "金額": 100, "結果": ""}
    for i, (場, r, s, t, p) in enumerate([
        ("唐津", "12R", "2連単", "1-5", "84%"),
        ("若松", "11R", "3連単", "4-5-6", "82%"),
        ("住之江", "10R", "単勝", "3", "81%"),
        ("丸亀", "9R", "2連単", "2-1", "80%"),
        ("平和島", "8R", "3連単", "3-2-6", "79%"),
        ("福岡", "7R", "2連単", "1-2", "77%"),
        ("常滑", "6R", "単勝", "4", "76%"),
        ("芦屋", "5R", "3連単", "5-6-1", "75%"),
        ("尼崎", "4R", "3連単", "6-4-3", "74%"),
        ("津",   "3R", "単勝", "2", "73%"),
    ])
]

df = pd.DataFrame(data)

# 結果列だけ編集可能（的中 or 不的中）
edited_df = st.data_editor(
    df,
    column_config={
        "結果": st.column_config.SelectboxColumn(
            label="結果",
            options=["", "的中", "不的中"],
            help="このレースの結果を選択してください",
        )
    },
    num_rows="fixed",
    use_container_width=True
)

# 登録ボタン（仮処理）
if st.button("✅ この内容で登録"):
    st.success("📥 勝敗登録が完了しました（仮処理）")
    st.dataframe(edited_df)
    # 保存機能（例：CSV保存やGSheet送信）など今後追加可
