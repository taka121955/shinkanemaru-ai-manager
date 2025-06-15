import streamlit as st
from datetime import datetime
from pages.page1_ai_prediction import show_ai_prediction

# --- ページ設定 ---
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide", initial_sidebar_state="collapsed")

# --- クエリでページ取得 ---
query_params = st.query_params
page = query_params.get("page", ["main"])[0]  # デフォルトは main

# --- ページ①〜⑥の場合、該当ページだけを表示（メインは非表示） ---
if page == "1":
    show_ai_prediction()
elif page == "2":
    st.markdown("② 勝敗入力ページ（準備中）")
elif page == "3":
    st.markdown("③ 統計データページ（準備中）")
elif page == "4":
    st.markdown("④ 結果履歴ページ（準備中）")
elif page == "5":
    st.markdown("⑤ 競艇結果ページ（準備中）")
elif page == "6":
    st.markdown("⑥ 設定ページ（準備中）")

# --- メインページ（page==mainのとき） ---
elif page == "main":
    # --- 現在時刻 ---
    jst = datetime.utcnow().astimezone()
    st.markdown(f"<h3 style='text-align: center;'>🕒 現在時刻（日本時間）：{jst.strftime('%Y/%m/%d %H:%M:%S')}</h3>", unsafe_allow_html=True)

    # --- 資金情報 ---
    st.markdown("""
    <div style='text-align: center; font-size: 18px;'>
    🎯 目標金額：10000円　💰 初期資金：5000円　📊 累積立資金：7200円
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    # --- ボタンスタイルと配置 ---
    st.markdown("""
    <style>
    .button-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 12px;
        margin-bottom: 30px;
    }
    .button-container form {
        margin: 0;
    }
    .button-container button {
        width: 150px;
        height: 60px;
        font-size: 17px;
        font-weight: bold;
        border: 2px solid #4a90e2;
        background-color: #e6f0ff;
        border-radius: 8px;
        color: #003366;
        cursor: pointer;
        transition: 0.2s;
    }
    .button-container button:hover {
        background-color: #d0e4ff;
        transform: scale(1.03);
    }
    </style>

    <div class="button-container">
        <form action='?page=1' method='get'><button>①AI予想</button></form>
        <form action='?page=2' method='get'><button>②勝敗入力</button></form>
        <form action='?page=3' method='get'><button>③統計データ</button></form>
        <form action='?page=4' method='get'><button>④結果履歴</button></form>
        <form action='?page=5' method='get'><button>⑤競艇結果</button></form>
        <form action='?page=6' method='get'><button>⑥設定</button></form>
    </div>
    """, unsafe_allow_html=True)

# --- フッター（全ページ共通） ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
