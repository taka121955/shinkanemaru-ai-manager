import streamlit as st
from datetime import datetime, timedelta

# ページ関数の読み込み（エラーにならないよう存在するページだけでもOK）
from pages.page1_ai_prediction import show_page as show_page1
from pages.page2_input_result import show_page as show_page2
from pages.page3_statistics import show_page as show_page3
from pages.page4_record_result import show_page as show_page4
from pages.page5_boat_results import show_page as show_page5
# from pages.page6_settings import show_page as show_page6  # 必要に応じて作成

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ✅ 現在の日本時間を中央に表示
jst = datetime.utcnow() + timedelta(hours=9)
st.markdown(
    f"<div style='text-align:center; font-size:26px;'>🕰 現在の時刻（日本時間）<br>{jst.strftime('%Y/%m/%d %H:%M:%S')}</div><hr>",
    unsafe_allow_html=True
)

# ✅ ページ名をセッションで管理
if "page" not in st.session_state:
    st.session_state.page = "①AI予想"

# ✅ メニューレイアウト（3列 × 2段）
st.markdown("### <div style='text-align:center;'>メニュー</div>", unsafe_allow_html=True)
menu_cols1 = st.columns(3)
with menu_cols1[0]:
    st.button("① AI予想", on_click=lambda: st.session_state.update(page="①AI予想"))
with menu_cols1[1]:
    st.button("② 勝敗入力", on_click=lambda: st.session_state.update(page="②勝敗入力"))
with menu_cols1[2]:
    st.button("③ 統計データ", on_click=lambda: st.session_state.update(page="③統計データ"))

menu_cols2 = st.columns(3)
with menu_cols2[0]:
    st.button("④ 結果履歴", on_click=lambda: st.session_state.update(page="④結果履歴"))
with menu_cols2[1]:
    st.button("⑤ 競艇結果", on_click=lambda: st.session_state.update(page="⑤競艇結果"))
with menu_cols2[2]:
    st.button("⑥ 設定", on_click=lambda: st.session_state.update(page="⑥設定"))

# ✅ ページ切り替え処理
if st.session_state.page == "①AI予想":
    show_page1()
elif st.session_state.page == "②勝敗入力":
    show_page2()
elif st.session_state.page == "③統計データ":
    show_page3()
elif st.session_state.page == "④結果履歴":
    show_page4()
elif st.session_state.page == "⑤競艇結果":
    show_page5()
elif st.session_state.page == "⑥設定":
    st.markdown("🔧 設定ページは現在準備中です。")

# ✅ フッター（中央表示）
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
