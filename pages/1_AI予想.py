import streamlit as st
from datetime import datetime
import random

st.title("🎯 本日のAI予想（的中率重視）")

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f"🕒 現在時刻：{now}")

# 仮予想データ（本番はAI接続へ）
for i in range(1, 6):
    race = f"競艇場 {random.randint(1,24):02}"
    式別 = random.choice(["3連単", "2連単", "単勝"])
    if 式別 == "3連単":
        予想 = f"{random.randint(1,6)}-{random.randint(1,6)}-{random.randint(1,6)}"
    elif 式別 == "2連単":
        予想 = f"{random.randint(1,6)}-{random.randint(1,6)}"
    else:
        予想 = f"{random.randint(1,6)}"
    的中率 = random.randint(70, 95)
    st.markdown(f"**{i}. {race}｜{式別}：{予想}（的中率：{的中率}％）**")

st.caption("※仮AI予想です。正式版は後日連携予定です。")
