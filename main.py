import streamlit as st
from datetime import datetime
import pytz

# 日本時間を取得
def get_japan_time():
    tz_japan = pytz.timezone('Asia/Tokyo')
    return datetime.now(tz_japan).strftime("%Y/%m/%d %H:%M:%S")

# ページごとの表示関数
def show_main():
    st.markdown("<h3 style='text-align: center;'>🕒 現在時刻（日本時間）</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'>{get_japan_time()}</h3>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("🎯 **目標金額：10000円**")
    st.markdown("💰 **初期資金：10000円**")
    st.markdown("📊 **累積金額：5000円**")

def show_ai():
    st.subheader("🧠 AI予想ページ（ここにAI予想の内容を表示）")

def show_input():
    st.subheader("🎮 勝敗入力ページ（ここに入力フォームを設置）")

def show_stats():
    st.subheader("📈 統計データページ（ここにグラフや統計を表示）")

def show_results():
    st.subheader("📋 結果記録ページ（ここに履歴を表示）")

# ページ切替
st.markdown("---")
pages = {
    "①AI予想": show_ai,
    "②勝敗入力": show_input,
    "③統計データ": show_stats,
    "④結果履歴": show_results,
}
cols = st.columns(len(pages))
for i, (label, func) in enumerate(pages.items()):
    if cols[i].button(label):
        st.session_state.page = label

# 初期化
if "page" not in st.session_state:
    st.session_state.page = "①AI予想"

# 表示
st.markdown("---")
show_main()
pages[st.session_state.page]()

# 制作者
st.markdown("---")
st.markdown("👤 制作者：小島崇彦")
