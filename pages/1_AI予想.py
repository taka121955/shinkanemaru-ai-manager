import streamlit as st
import random

st.title("📈 本日のAI予想（仮）")

# 仮の予想生成
競艇場名 = random.choice(["住之江", "丸亀", "芦屋", "唐津", "蒲郡"])
式別 = random.choice(["3連単", "2連単", "単勝"])
if 式別 == "3連単":
    賭け内容 = f"{random.randint(1,6)}-{random.randint(1,6)}-{random.randint(1,6)}"
elif 式別 == "2連単":
    賭け内容 = f"{random.randint(1,6)}-{random.randint(1,6)}"
else:
    賭け内容 = f"{random.randint(1,6)}"
的中率 = random.randint(75, 95)

# セッションに保存
st.session_state["last_prediction"] = {
    "競艇場": 競艇場名,
    "式別": 式別,
    "内容": 賭け内容
}

st.markdown(f"""
### ✅ AI予想内容：
- 競艇場：**{競艇場名}**
- 式別：**{式別}**
- 賭け内容：**{賭け内容}**
- 的中率：**{的中率}%**

👉 ページ②でこの内容が自動反映されます。
""")
