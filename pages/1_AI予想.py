import streamlit as st
from datetime import datetime
import random

st.title("🎯 本日のAI予想（的中率重視）")

# 現在時刻の表示
now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"🕒 現在時刻： `{now}`")

# CSS：エクセル風テーブル
st.markdown("""
<style>
.excel-table {
    border-collapse: collapse;
    width: 100%;
    max-width: 600px;
    margin: 20px auto;
    font-size: 16px;
}
.excel-table th, .excel-table td {
    border: 1px solid #4a90e2;
    padding: 10px;
    text-align: center;
}
.excel-table th {
    background-color: #e6f0ff;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# 予想生成
@st.cache_data
def generate_predictions():
    data = []
    for i in range(1, 6):
        jcd = f"{random.randint(1, 24):02}"
        式別 = random.choice(["3連単", "2連単", "単勝"])
        if 式別 == "3連単":
            予想 = f"{random.randint(1,6)}-{random.randint(1,6)}-{random.randint(1,6)}"
        elif 式別 == "2連単":
            予想 = f"{random.randint(1,6)}-{random.randint(1,6)}"
        else:
            予想 = f"{random.randint(1,6)}"
        的中率 = f"{random.randint(75, 95)}%"
        data.append((jcd, 式別, 予想, 的中率))
    return data

# 表形式で表示
rows = generate_predictions()
table_html = """
<table class="excel-table">
<thead>
<tr><th>競艇場</th><th>式別</th><th>予想</th><th>的中率</th></tr>
</thead><tbody>
"""
for row in rows:
    table_html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>"
table_html += "</tbody></table>"

st.markdown(table_html, unsafe_allow_html=True)

st.caption("※仮AI予想です。正式版は後日連携予定です。")
