import streamlit as st
from datetime import datetime

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# セッション初期化
st.session_state.setdefault("目標金額", 0)
st.session_state.setdefault("準備金額", 0)
st.session_state.setdefault("積立金額", 0)

# ヘッダー：現在時刻
st.markdown(f"### ⏰ 現在時刻：{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}")

# タイトル
st.markdown("## 🧠 新金丸法 × AI資金マネージャー")

# ページ選択ダミーボタン（見た目用）
st.markdown("#### 📄 メニュー")
cols = st.columns(3)
with cols[0]: st.button("① AI予想", disabled=True)
with cols[1]: st.button("② 勝敗入力", disabled=True)
with cols[2]: st.button("③ 統計データ", disabled=True)

cols2 = st.columns(3)
with cols2[0]: st.button("④ 結果履歴", disabled=True)
with cols2[1]: st.button("⑤ 競艇結果", disabled=True)
with cols2[2]: st.button("⑥ 資金設定", disabled=True)

# 資金情報表示（連動）
st.markdown("---")
st.markdown(f"🎯 <strong>目標金額：</strong> <span style='color:blue;font-size:22px;'>{st.session_state['目標金額']:,}円</span>", unsafe_allow_html=True)
st.markdown(f"💰 <strong>準備金額：</strong> <span style='color:green;font-size:22px;'>{st.session_state['準備金額']:,}円</span>", unsafe_allow_html=True)
st.markdown(f"📦 <strong>積立金額：</strong> <span style='color:orange;font-size:22px;'>{st.session_state['積立金額']:,}円</span>", unsafe_allow_html=True)
st.markdown("---")

# フッター
st.markdown("##### 制作者：小島崇彦")
