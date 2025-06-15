import streamlit as st
from datetime import datetime

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide")

# トップページ専用画面
jst = datetime.utcnow().astimezone()
st.markdown(f"### 🕒 現在時刻（日本時間）：{jst.strftime('%Y/%m/%d %H:%M:%S')}")

st.markdown("""
### 💼 新金丸法 × AI資金マネージャー

- 上のメニューから各ページに移動できます
- ①〜⑥の予測や入力、統計情報を活用してください

---
""")

st.markdown("制作者：小島崇彦")
