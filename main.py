import streamlit as st
import pandas as pd

# メニュー表示用データ
menu_items = [
    ["① AI予想", "② 勝敗入力", "③ 統計データ"],
    ["④ 結果履歴", "⑤ 競艇結果", "⑥ 設定"]
]

# 表示スタイル
st.markdown("### 📁 メニュー選択")
menu_df = pd.DataFrame(menu_items)

# エクセル風・太字・大きめ・中央揃え
st.dataframe(
    menu_df.style.set_properties(**{
        'font-weight': 'bold',
        'font-size': '16px',
        'text-align': 'center'
    }),
    height=130
)
