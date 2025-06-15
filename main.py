import streamlit as st
from datetime import datetime

# ✅ サイドバー非表示＆ワイド表示
st.set_page_config(
    page_title="新金丸法 × AI資金マネージャー",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ✅ 上部：現在時刻と資金情報
jst = datetime.utcnow().astimezone()
st.markdown(f"<h3 style='text-align: center;'>🕒 現在時刻（日本時間）：{jst.strftime('%Y/%m/%d %H:%M:%S')}</h3>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; font-size: 18px;'>
🎯 目標金額：10000円　💰 初期資金：5000円　📊 累積立資金：7200円
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ✅ ボタン（2段 × 3列）レイアウト
row1 = st.columns(3)
row2 = st.columns(3)

with row1[0]:
    st.button("①AI予想")
with row1[1]:
    st.button("②勝敗入力")
with row1[2]:
    st.button("③統計データ")

with row2[0]:
    st.button("④結果履歴")
with row2[1]:
    st.button("⑤競艇結果")
with row2[2]:
    st.button("⑥設定")

# ✅ 下のページ表示をすべてカット（非表示）

# ✅ フッターだけ表示
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
