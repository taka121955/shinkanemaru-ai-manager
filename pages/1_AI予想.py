import streamlit as st
from datetime import datetime
import random

st.title("🎯 本日のAI予想（的中率重視）")

now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"🕒 現在時刻： `{now}`")

# CSSスタイル追加（囲み枠）
st.markdown("""
<style>
.box {
    border: 2px solid #4a90e2;
    border-radius: 10px;
    padding: 15px;
    background-color: #f9fbff;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# 予想生成（軽量＆キャッシュ）
@st.cache_data
def generate_predictions():
    result = []
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
        line = f"{i}. 競艇場 {jcd} ｜ {式別}：{予想}（的中率：{的中率}%）"
        result.append(line)
    return result

# 囲み枠で出力
predictions = generate_predictions()
st.markdown("<div class='box'>" + "<br>".join(predictions) + "</div>", unsafe_allow_html=True)

st.caption("※仮AI予想です。正式版は後日連携予定です。")
