import streamlit as st
from datetime import datetime

# タイトルと現在時刻（日本時間）
st.markdown("## 🕰️ 現在時刻： " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

# アプリタイトル
st.markdown("### 💼 新金丸法 × AI資金マネージャー")
st.markdown("##### 以下のページ番号をご確認ください")

# ページメニュー（ボタン風に見せるだけ）
cols = st.columns(3)
with cols[0]:
    st.markdown("#### 🟦① AI予想", unsafe_allow_html=True)
with cols[1]:
    st.markdown("#### 🟦② 勝敗入力", unsafe_allow_html=True)
with cols[2]:
    st.markdown("#### 🟦③ 統計データ", unsafe_allow_html=True)

cols2 = st.columns(3)
with cols2[0]:
    st.markdown("#### 🟦④ 結果履歴", unsafe_allow_html=True)
with cols2[1]:
    st.markdown("#### 🟦⑤ 競艇結果", unsafe_allow_html=True)
with cols2[2]:
    st.markdown("#### 🟦⑥ 資金設定", unsafe_allow_html=True)

st.markdown("---")

# 目標金額・準備金額・積立金額（中央に大きく表示）
st.markdown("""
<div style='text-align:center'>
    <p style='font-size:22px;'>🎯 <strong>目標金額</strong>：<span style='color:blue;'>50,000円</span></p>
    <p style='font-size:22px;'>💰 <strong>準備金額</strong>：<span style='color:green;'>10,000円</span></p>
    <p style='font-size:22px;'>📦 <strong>積立金額</strong>：<span style='color:orange;'>3,000円</span></p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("###### 制作者：小島崇彦")
