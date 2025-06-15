# main.py

import streamlit as st
from datetime import datetime
import pandas as pd
import os

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# ページタイトル
st.markdown("### 🕒 現在時刻 ：  \n<font size=5>{}</font>".format(
    datetime.now().strftime("%Y/%m/%d %H:%M:%S")
), unsafe_allow_html=True)

st.markdown("## 💼 新金丸法 × AI資金マネージャー")
st.markdown("以下のページを選択してください")

# 金額読み込み
if os.path.exists("settings.csv"):
    df = pd.read_csv("settings.csv")
    if not df.empty:
        target = df["目標金額"].values[0]
        reserve = df["準備金"].values[0]
        saving = df["積立金"].values[0]
    else:
        target, reserve, saving = 0, 0, 0
else:
    target, reserve, saving = 0, 0, 0

# 金額表示
st.markdown(f"""
### 🎯 目標金額：<span style='font-size:24px; color:green;'>{target:,}円</span>  
### 🧰 準備金額：<span style='font-size:24px; color:blue;'>{reserve:,}円</span>  
### 🏦 積立金額：<span style='font-size:24px; color:orange;'>{saving:,}円</span>
""", unsafe_allow_html=True)

# ページリンクボタン
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.page_link("pages/page1_ai_prediction.py", label="① AI予想", icon="📊")
    st.page_link("pages/page2_input_result.py", label="② 勝敗入力", icon="📝")
with col2:
    st.page_link("pages/page3_statistics.py", label="③ 統計データ", icon="📈")
    st.page_link("pages/page4_record_result.py", label="④ 勝敗履歴", icon="📋")
with col3:
    st.page_link("pages/page5_boat_results.py", label="⑤ 競艇結果", icon="🚤")
    st.page_link("pages/page6_fund_settings.py", label="⑥ 資金設定", icon="⚙️")

# 制作者名
st.markdown("<br><br><center>制作者：小島崇彦</center>", unsafe_allow_html=True)
