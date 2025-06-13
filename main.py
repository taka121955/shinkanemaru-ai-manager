from datetime import datetime
import streamlit as st
import pytz
import os
import pandas as pd

# ページ設定
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# 日本時間の現在時刻
jst = pytz.timezone("Asia/Tokyo")
now = datetime.now(jst).strftime("%Y-%m-%d %H:%M:%S")

# CSVの初期化と読み込み
csv_path = "results.csv"
if not os.path.exists(csv_path):
    df = pd.DataFrame(columns=["日付", "競艇場", "レース", "式別", "賭け金", "的中", "払戻金"])
    df.to_csv(csv_path, index=False)

# データの読み込み
df = pd.read_csv(csv_path)

# 累積資金計算
if not df.empty:
    df["損益"] = df["払戻金"] - df["賭け金"]
    cumulative = df["損益"].sum()
else:
    cumulative = 0

# ---- 上部表示 ----
st.markdown(f"<h2 style='text-align:center;'>{now}</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🎯 目標金額", "10000円")
with col2:
    st.metric("💰 初期資金", "10000円")
with col3:
    st.metric("📊 累積資金", f"{cumulative}円")

st.markdown("---")

# ---- ページ切替ボタン配置 ----
col_top = st.columns(3)
col_mid = st.columns(2)
col_bot = st.columns(2)

with col_top[1]:
    if st.button("① AI予想"):
        st.switch_page("pages/page1_ai_prediction.py")

with col_mid[0]:
    if st.button("② 勝敗入力"):
        st.switch_page("pages/page2_input_result.py")

with col_mid[1]:
    if st.button("③ 統計データ"):
        st.switch_page("pages/page3_statistics.py")

with col_bot[0]:
    if st.button("④ 結果履歴"):
        st.switch_page("pages/page4_record_result.py")

with col_bot[1]:
    if st.button("⑤ 競艇結果"):
        st.switch_page("pages/page5_boat_results.py")

st.markdown("---")
st.markdown("<div style='text-align:center;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
