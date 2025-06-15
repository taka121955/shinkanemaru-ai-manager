import streamlit as st
from datetime import datetime
import random

# タイトル大きく・中央・アイコン付き
st.markdown("<h2 style='text-align:center;'>🎯 <span style='font-size:32px;'>本日のAI予想</span><br><span style='font-size:22px;'>(的中率重視)</span></h2>", unsafe_allow_html=True)

# 時刻を太字・見やすく
now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"<p style='text-align:center; font-size:16px;'>🕒 <b>現在時刻：</b>{now}</p>", unsafe_allow_html=True)

# 予想データ表示（中央揃え、太字、行間広め）
st.markdown("<div style='padding: 0 10px;'>", unsafe_allow_html=True)
for i in range(1, 6):
    jcd = f"{random.randint(1, 24):02}"
    式別 = random.choice(["3連単", "2連単", "単勝"])
    if 式別 == "3連単":
        予想 = f"{random.randint(1,6)}-{random.randint(1,6)}-{random.randint(1,6)}"
    elif 式別 == "2連単":
        予想 = f"{random.randint(1,6)}-{random.randint(1,6)}"
    else:
        予想 = f"{random.randint(1,6)}"
    的中率 = random.randint(75, 95)
    st.markdown(f"""
    <div style='font-size:18px; line-height:1.8;'>
        <b>{i}. 競艇場 {jcd}</b> ｜ <b>{式別}</b>：<span style='color:#005bbb; font-weight:bold;'>{予想}</span>
        （的中率：<span style='color:#d9534f;'>{的中率}%</span>）
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 注意書き
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("※この予想は仮のAIロジックによるものです。本番AIモデルは近日導入予定です。")
