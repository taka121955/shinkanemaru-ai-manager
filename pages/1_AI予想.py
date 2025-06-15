import streamlit as st
from datetime import datetime
import random

# 競艇場番号 → 名前変換辞書
jcd_names = {
    "01": "桐生", "02": "戸田", "03": "江戸川", "04": "平和島", "05": "多摩川",
    "06": "浜名湖", "07": "蒲郡", "08": "常滑", "09": "津", "10": "三国",
    "11": "びわこ", "12": "住之江", "13": "尼崎", "14": "鳴門", "15": "丸亀",
    "16": "児島", "17": "宮島", "18": "徳山", "19": "下関", "20": "若松",
    "21": "芦屋", "22": "福岡", "23": "唐津", "24": "大村"
}

# 現在時刻（強調表示）
now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"""
<div style="text-align: center; font-size: 28px; font-weight: bold;">
🕒 現在時刻（日本時間）：{now}
</div>
""", unsafe_allow_html=True)

# タイトル
st.markdown("## 🎯 本日のAI予想（的中率重視）")

# CSS（表スタイル）
st.markdown("""
<style>
.excel-table {
    border-collapse: collapse;
    width: 100%;
    max-width: 700px;
    margin: 20px auto;
    font-size: 17px;
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

# 予想生成（@st.cache_data は不要）
def generate_predictions():
    data = []
    for _ in range(5):
        jcd = f"{random.randint(1, 24):02}"
        場名 = jcd_names.get(jcd, f"場{jcd}")
        式別 = random.choice(["3連単", "2連単", "単勝"])
        if 式別 == "3連単":
            予想 = f"{random.randint(1,6)}-{random.randint(1,6)}-{random.randint(1,6)}"
        elif 式別 == "2連単":
            予想 = f"{random.randint(1,6)}-{random.randint(1,6)}"
        else:
            予想 = f"{random.randint(1,6)}"
        的中率 = f"{random.randint(80, 95)}%"
        data.append((場名, 式別, 予想, 的中率))
    return data

# 表HTML出力
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

# フッター注釈
st.caption("※仮AI予想です。正式版は後日連携予定です。")
