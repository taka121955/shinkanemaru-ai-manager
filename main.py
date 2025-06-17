import streamlit as st
from datetime import datetime
from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4

# ✅ 最初に実行（set_page_config は1行目に近い場所で）
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ✅ 上部情報表示
st.markdown("### 🕒 現在時刻（日本時間）：")
now = datetime.now()
st.markdown(f"#### `{now.strftime('%Y/%m/%d %H:%M:%S')}`")

st.markdown("### 🎯 目標金額：10000円")
st.markdown("### 💰 初期資金：5000円")
st.markdown("### 📊 累積資金：0円")

# ✅ ページ切り替えメニュー
st.sidebar.title(".main")  # ← GitHubのページ名を隠す
menu = st.sidebar.radio("🔘 メニュー選択", [
    "① AI予想",
    "② 勝敗入力",
    "③ 統計データ",
    "④ 結果履歴"
])

# ✅ 選択に応じたページ表示
if menu == "① AI予想":
    show_page1()
elif menu == "② 勝敗入力":
    show_page2()
elif menu == "③ 統計データ":
    show_page3()
elif menu == "④ 結果履歴":
    show_page4()

# ✅ フッター
st.markdown("---")
st.markdown("制作者：小島崇彦")
