import streamlit as st
import pandas as pd
from datetime import datetime
from utils.calc_ecp import calculate_next_bet

# CSVファイルのパス（Streamlit Cloud対応の相対パスに修正）
CSV_PATH = "results.csv"

# ページ選択用セッションステート初期化
if "page" not in st.session_state:
    st.session_state.page = "main"

# 現在時刻（日本時間）
now = datetime.utcnow().astimezone()
japan_time = now.strftime("%Y/%m/%d %H:%M:%S")

# 累積資金の初期化
if "total_profit" not in st.session_state:
    st.session_state.total_profit = 0

# ✅ CSVファイルの読み込み（なければ作成）
if not hasattr(st, "df_loaded"):
    try:
        df_init = pd.read_csv(CSV_PATH)
    except FileNotFoundError:
        df_init = pd.DataFrame(columns=["日付", "競艇場", "レース", "賭金", "払戻金"])
        df_init.to_csv(CSV_PATH, index=False)
    st.df_loaded = df_init
else:
    df_init = st.df_loaded

# 💰 累積計算
total_bet = df_init["賭金"].sum()
total_return = df_init["払戻金"].sum()
st.session_state.total_profit = total_return - total_bet

# 🎯 固定設定
initial_funds = 10000
target_funds = 10000

# 🎛 メイン画面
if st.session_state.page == "main":
    st.markdown("### 🕓 現在時刻（日本時間）")
    st.markdown(f"## {japan_time}")

    st.markdown(f"🎯 目標金額： {target_funds}円")
    st.markdown(f"💰 初期資金： {initial_funds}円")
    st.markdown(f"📊 累積金額： {st.session_state.total_profit}円")

    # ページ切り替えボタン（整列）
    col1, col2 = st.columns(2)
    with col1:
        if st.button("①AI予想"):
            st.session_state.page = "page1"
        if st.button("②勝敗入力"):
            st.session_state.page = "page2"
        if st.button("③統計データ"):
            st.session_state.page = "page3"
    with col2:
        if st.button("④結果履歴"):
            st.session_state.page = "page4"
        if st.button("⑤競艇結果"):
            st.session_state.page = "page5"

    st.markdown("🟩 メインページです")

# 🔁 各ページ切り替え
elif st.session_state.page == "page1":
    from pages import page1_ai_prediction as page
    page.show()
elif st.session_state.page == "page2":
    from pages import page2_input_result as page
    page.show()
elif st.session_state.page == "page3":
    from pages import page3_statistics as page
    page.show()
elif st.session_state.page == "page4":
    from pages import page4_record_result as page
    page.show()
elif st.session_state.page == "page5":
    from pages import page5_boat_results as page
    page.show()

# 👤 制作者
st.markdown("---")
st.markdown("👤 制作者：小島崇彦")
