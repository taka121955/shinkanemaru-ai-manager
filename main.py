import streamlit as st
from datetime import datetime

from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_boat_results import show_page as show_page5
from pages.page6_settings import show_page as show_page6

# ✅ サイドバー非表示＆中央レイアウト
st.set_page_config(
    page_title="新金丸法 × AI資金マネージャー",
    layout="wide",  # ← wide に変更
    initial_sidebar_state="collapsed"
)

# ✅ 現在時刻
jst = datetime.utcnow().astimezone()
st.markdown(f"<h3 style='text-align: center;'>🕒 現在時刻（日本時間）：{jst.strftime('%Y/%m/%d %H:%M:%S')}</h3>", unsafe_allow_html=True)

# ✅ 資金状況表示
st.markdown("""
<div style='text-align: center; font-size: 18px;'>
🎯 目標金額：10000円　💰 初期資金：5000円　📊 累積立資金：7200円
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ✅ 横並びボタン 2段3列（スマホ横幅対応）
# ボタンはHTML + st.markdown + unsafe_allow_htmlで制御

st.markdown("""
<div style="text-align:center;">
    <div style="display:flex; justify-content:center; gap:10px; flex-wrap:wrap;">
        <form action="?page=1"><button>①AI予想</button></form>
        <form action="?page=2"><button>②勝敗入力</button></form>
        <form action="?page=3"><button>③統計データ</button></form>
        <form action="?page=4"><button>④結果履歴</button></form>
        <form action="?page=5"><button>⑤競艇結果</button></form>
        <form action="?page=6"><button>⑥設定</button></form>
    </div>
</div>
""", unsafe_allow_html=True)

# ✅ ページ切り替え制御
page = st.query_params.get("page", "1")

if page == "1":
    show_page1()
elif page == "2":
    show_page2()
elif page == "3":
    show_page3()
elif page == "4":
    show_page4()
elif page == "5":
    show_page5()
elif page == "6":
    show_page6()

# ✅ フッター
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
